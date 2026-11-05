# Troubleshooting

What to try when something does not work, where to find your log files, and how to report a bug on the Norse
Demigods Discord.

<!-- IMAGE: the #bugs forum on the Norse Demigods Discord -->

## Common problems

| Problem | What to do |
| --- | --- |
| Text is missing or shows as placeholders | The mod's files were moved or are missing. Reinstall the mod and keep its folder structure. See [Manual install](../getting-started/installing-the-mod.md#manual-install). |
| You cannot join a server: your `Demigods.yaml` differs from the server's | Install the same mod files as the server, for example its modpack. See [Multiplayer](../getting-started/installing-the-mod.md#multiplayer). |
| The runestone says *"Disabled by divine intervention!"* | The server has disabled that demigod. See the [FAQ](faq.md#the-runestone-says-disabled-by-divine-intervention). |
| The energy meter clashes with another interface mod | Turn off the mod's meters: `[User Interface] Enable Meters`. See [Interface settings](../getting-started/controls-and-hotkeys.md#interface-settings). |
| Your settings go back to the server's when you join | The server controls most settings. See the [FAQ](faq.md#which-settings-does-the-server-control). |

## Is it this mod?

Before reporting a bug, check whether Norse Demigods causes it:

1. Back up your characters and worlds. Items from mods that are not loaded can disappear.
2. Make a new mod manager profile with only Norse Demigods and its required mods (see
   [Requirements](../getting-started/installing-the-mod.md#requirements)).
3. Try to make the problem happen again.

- If it does not happen, another mod is involved. Add your other mods back a few at a time to find which one.
- Check [Compatibility](../getting-started/compatibility.md) for known problems.

## Log files

The game writes a log file every session. It holds the error messages that help find a bug.

| File | Where |
| --- | --- |
| `Player.log` (latest session) | `%USERPROFILE%\AppData\LocalLow\IronGate\Valheim` (Windows) |
| `Player-prev.log` (the session before) | The same folder |

- Error messages usually contain the word "Exception", for example *"NullReferenceException: Object reference not
  set to an instance of an object"*.
- Lines that mention `NorseDemigods` under an error point to this mod.
- Each new session replaces the old log, so copy it right after the problem happens.

## Reporting a bug

Post in the **#bugs** forum on the [Norse Demigods Discord](https://discord.gg/gSQHmE3yap).

- Title: the mod's name in brackets, then the problem, for example *"(Norse Demigods) Wolf disappears after
  teleporting"*.
- Describe what you did, what you expected and what happened.
- Say which mod version you use, and whether you play alone or on a server.
- Attach your `Player.log`, or at least the error messages.
- List your other mods, or say if the problem also happens with Norse Demigods alone.

Ideas and suggestions go in the **#ideas** forum.

## Related pages

- [FAQ](faq.md)
- [Compatibility](../getting-started/compatibility.md)
- [Installing the Mod](../getting-started/installing-the-mod.md)

<!-- Verified against NorseDemigods 1.9.1 -->
