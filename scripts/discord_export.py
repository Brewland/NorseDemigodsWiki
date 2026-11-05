"""Export every message a Discord bot can read in a server, as source material for the FAQ.

The bot token is read from the DISCORD_BOT_TOKEN environment variable, never from a file or argument.
The bot needs View Channels and Read Message History in the server, and the Message Content intent enabled
in the Discord Developer Portal (Bot > Privileged Gateway Intents), otherwise message text comes back empty.

Usage (PowerShell, from the repository root):
    $env:DISCORD_BOT_TOKEN = "<token>"
    .\\.venv\\Scripts\\python.exe scripts\\discord_export.py [--guild <server id>] [--out discord-export] [--full]

Running it again only pulls messages sent since the previous run (message ids grow with time) and adds them to the
saved files. Edits and deletions of already saved messages are not picked up: use --full to pull everything again.

Output (git-ignored, it holds other players' messages):
    <out>/index.json             every channel and thread with its message count, or why it was skipped
    <out>/json/<name>-<id>.json  the messages of one channel or thread, oldest first
    <out>/md/<name>-<id>.md      the same messages as a readable transcript
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

API = "https://discord.com/api/v10"
USER_AGENT = "DiscordBot (https://github.com/Brewland/NorseDemigodsWiki, 1.0)"

# Channel types: https://discord.com/developers/docs/resources/channel#channel-object-channel-types
CATEGORY = 4
MESSAGE_CHANNELS = {0: "text", 2: "voice", 5: "announcement", 13: "stage"}
THREAD_PARENTS = {0, 5, 15, 16}  # text, announcement, forum, media
THREAD_TYPES = {10: "announcement thread", 11: "thread", 12: "private thread"}
FORUM_TYPES = {15: "forum", 16: "media"}

# Message types worth keeping in the transcript: default and reply.
CHAT_MESSAGE_TYPES = {0, 19}


class ApiError(Exception):
    def __init__(self, status, body):
        super().__init__(f"HTTP {status}: {body}")
        self.status = status


def api(token, path, params=None):
    url = API + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(url, headers={"Authorization": f"Bot {token}", "User-Agent": USER_AGENT})
    for attempt in range(6):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                data = json.loads(response.read())
                if response.headers.get("X-RateLimit-Remaining") == "0":
                    time.sleep(float(response.headers.get("X-RateLimit-Reset-After", "1")))
                return data
        except urllib.error.HTTPError as error:
            body = error.read().decode("utf-8", "replace")
            if error.code == 429:
                time.sleep(float(json.loads(body).get("retry_after", 1)) + 0.25)
                continue
            if error.code >= 500:
                time.sleep(2**attempt)
                continue
            raise ApiError(error.code, body) from None
        except urllib.error.URLError:
            time.sleep(2**attempt)
    raise ApiError(0, f"gave up after retries: {path}")


def pick_guild(token, guild_id):
    guilds = api(token, "/users/@me/guilds")
    if guild_id:
        match = [g for g in guilds if g["id"] == guild_id]
        if not match:
            sys.exit(f"The bot is not in server {guild_id}.")
        return match[0]
    if len(guilds) == 1:
        return guilds[0]
    print("The bot is in several servers; pass one with --guild:")
    for g in guilds:
        print(f"  {g['id']}  {g['name']}")
    sys.exit(1)


def list_threads(token, guild_id, channels):
    threads = {t["id"]: t for t in api(token, f"/guilds/{guild_id}/threads/active")["threads"]}
    skipped = []
    for channel in channels:
        if channel["type"] not in THREAD_PARENTS:
            continue
        kinds = ["public"] + (["private"] if channel["type"] == 0 else [])
        for kind in kinds:
            before = None
            while True:
                params = {"limit": 100} | ({"before": before} if before else {})
                try:
                    page = api(token, f"/channels/{channel['id']}/threads/archived/{kind}", params)
                except ApiError as error:
                    if error.status in (403, 404):
                        skipped.append(f"#{channel['name']}: archived {kind} threads ({error.status})")
                        break
                    raise
                for thread in page["threads"]:
                    threads[thread["id"]] = thread
                if not page.get("has_more") or not page["threads"]:
                    break
                before = page["threads"][-1]["thread_metadata"]["archive_timestamp"]
    return list(threads.values()), skipped


def fetch_messages(token, channel_id, after=None):
    """All messages of a channel, or only those newer than message id `after`, oldest first."""
    messages = []
    cursor = after
    while True:
        if after:
            params = {"limit": 100, "after": cursor}
        else:
            params = {"limit": 100} | ({"before": cursor} if cursor else {})
        page = api(token, f"/channels/{channel_id}/messages", params)
        messages.extend(page)
        if len(page) < 100:
            break
        ids = [int(m["id"]) for m in page]
        cursor = str(max(ids) if after else min(ids))
    messages.sort(key=lambda m: int(m["id"]))
    return messages


def load_previous(json_dir, channel_id):
    """Messages saved by an earlier run for this channel or thread (found by id, so renames are fine)."""
    for path in json_dir.glob(f"*-{channel_id}.json"):
        return path, json.loads(path.read_text(encoding="utf-8"))["messages"]
    return None, []


def simplify(message):
    author = message["author"]
    return {
        "id": message["id"],
        "type": message["type"],
        "timestamp": message["timestamp"],
        "edited": message.get("edited_timestamp"),
        "author": author.get("global_name") or author["username"],
        "author_id": author["id"],
        "bot": author.get("bot", False),
        "content": message.get("content", ""),
        "reply_to": (message.get("message_reference") or {}).get("message_id"),
        "attachments": [a["url"] for a in message.get("attachments", [])],
        "embeds": [
            {k: e[k] for k in ("title", "description", "url") if e.get(k)}
            for e in message.get("embeds", [])
            if e.get("title") or e.get("description")
        ],
    }


def slug(name):
    return re.sub(r"[^\w-]+", "-", name.lower()).strip("-") or "channel"


def to_markdown(entry, messages):
    by_id = {m["id"]: m for m in messages}
    lines = [f"# {entry['label']}", ""]
    if entry.get("topic"):
        lines += [f"> {entry['topic']}", ""]
    for m in messages:
        if m["type"] not in CHAT_MESSAGE_TYPES and not m["content"]:
            continue
        stamp = datetime.fromisoformat(m["timestamp"]).strftime("%Y-%m-%d %H:%M")
        lines.append(f"**{m['author']}**{' (bot)' if m['bot'] else ''} · {stamp} · `{m['id']}`")
        if m["reply_to"]:
            parent = by_id.get(m["reply_to"])
            if parent:
                snippet = " ".join(parent["content"].split())[:80]
                lines.append(f"> replying to **{parent['author']}**: {snippet}")
            else:
                lines.append(f"> replying to message `{m['reply_to']}`")
        if m["content"]:
            lines.append(m["content"])
        for e in m["embeds"]:
            lines.append(f"[embed] {e.get('title', '')} {e.get('description', '')}".strip())
        for url in m["attachments"]:
            lines.append(f"[attachment] {url}")
        lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--guild", help="server id (only needed if the bot is in several servers)")
    parser.add_argument("--out", default="discord-export", help="output folder (default: discord-export)")
    parser.add_argument("--full", action="store_true",
                        help="pull everything again instead of only messages newer than the last run")
    args = parser.parse_args()

    sys.stdout.reconfigure(encoding="utf-8")
    token = os.environ.get("DISCORD_BOT_TOKEN")
    if not token:
        sys.exit("Set the DISCORD_BOT_TOKEN environment variable first.")

    guild = pick_guild(token, args.guild)
    print(f"Server: {guild['name']} ({guild['id']})")

    channels = api(token, f"/guilds/{guild['id']}/channels")
    names = {c["id"]: c["name"] for c in channels}
    categories = {c["id"]: c["name"] for c in channels if c["type"] == CATEGORY}
    threads, skipped = list_threads(token, guild["id"], channels)

    targets = []
    for c in sorted(channels, key=lambda c: (c.get("position", 0), c["name"])):
        if c["type"] in MESSAGE_CHANNELS:
            category = categories.get(c.get("parent_id"), "")
            label = f"#{c['name']}" + (f" ({category})" if category else "")
            targets.append({"id": c["id"], "name": c["name"], "kind": MESSAGE_CHANNELS[c["type"]],
                            "label": label, "category": category, "topic": c.get("topic")})
    for t in threads:
        parent = names.get(t.get("parent_id"), "?")
        parent_type = next((c["type"] for c in channels if c["id"] == t.get("parent_id")), None)
        kind = "forum post" if parent_type in FORUM_TYPES else THREAD_TYPES.get(t["type"], "thread")
        targets.append({"id": t["id"], "name": f"{parent}--{t['name']}", "kind": kind,
                        "label": f"{t['name']} ({kind} in #{parent})", "parent": parent})

    out = Path(args.out)
    (out / "json").mkdir(parents=True, exist_ok=True)
    (out / "md").mkdir(parents=True, exist_ok=True)

    index = {"server": guild["name"], "server_id": guild["id"],
             "exported_at": datetime.now().astimezone().isoformat(timespec="seconds"),
             "channels": [], "skipped": skipped}
    total = new_total = empty = 0
    for entry in targets:
        previous_path, previous = (None, []) if args.full else load_previous(out / "json", entry["id"])
        last_id = previous[-1]["id"] if previous else None
        try:
            new = [simplify(m) for m in fetch_messages(token, entry["id"], after=last_id)]
        except ApiError as error:
            index["skipped"].append(f"{entry['label']}: messages ({error.status})")
            print(f"  skipped  {entry['label']} ({error.status})")
            continue
        known = {m["id"] for m in previous}
        messages = previous + [m for m in new if m["id"] not in known]
        new_total += len(messages) - len(previous)
        file_stem = f"{slug(entry['name'])}-{entry['id']}"
        if previous_path and previous_path.stem != file_stem:  # channel or thread was renamed
            previous_path.unlink()
            (out / "md" / f"{previous_path.stem}.md").unlink(missing_ok=True)
        (out / "json" / f"{file_stem}.json").write_text(
            json.dumps(entry | {"messages": messages}, ensure_ascii=False, indent=2), encoding="utf-8")
        (out / "md" / f"{file_stem}.md").write_text(to_markdown(entry, messages), encoding="utf-8")
        index["channels"].append({k: entry[k] for k in ("id", "label", "kind")}
                                 | {"messages": len(messages), "file": file_stem})
        total += len(messages)
        empty += sum(1 for m in messages if not m["bot"] and m["type"] in CHAT_MESSAGE_TYPES
                     and not m["content"] and not m["attachments"])
        print(f"  {len(messages):6} (+{len(messages) - len(previous)})  {entry['label']}")

    (out / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n{total} messages ({new_total} new) from {len(index['channels'])} channels and threads "
          f"written to {out}/")
    if index["skipped"]:
        print(f"{len(index['skipped'])} skipped (no permission); see index.json")
    if total and empty > total / 2:
        print("WARNING: most messages have no text. Enable the Message Content intent for the bot in the "
              "Discord Developer Portal (Bot > Privileged Gateway Intents) and run again.")


if __name__ == "__main__":
    main()
