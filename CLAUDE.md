# CLAUDE.md

## Project

Player-facing gameplay wiki for the Valheim mod **Norse Demigods**.

- Built with MkDocs Material; deployed to GitHub Pages by GitHub Actions (`.github/workflows/deploy.yml`) on every
  push to `main`.
- Live site: <https://brewland.github.io/NorseDemigodsWiki/>
- Repository: <https://github.com/Brewland/NorseDemigodsWiki>

## Rules

- **Always read and follow [WIKI_GUIDE.md](WIKI_GUIDE.md) before writing or editing pages.** It is the complete
  rulebook: sources, conventions, styling, CSS classes, templates.
- **Mod source:** `../NorseDemigods/NorseDemigods` is the only source of truth for numbers. It is **read-only**:
  never modify anything outside this repository.
- **Reference example:** Thor is the approved reference batch. Match it:
  - `docs/demigods/thor.md`
  - `docs/abilities/` `lightning-strike.md`, `dash.md`, `lightning-aura.md`, `lightning-storm.md`,
    `restoration.md`, `teleport.md`
  - `docs/attributes/` `static-body.md`, `bear-strength.md`, `titan-legs.md`
- **Decisions go into the guide.** Any style or convention decision the user makes in chat must be written into
  WIKI_GUIDE.md in the same batch, so the guide alone is enough to produce identical-looking pages.

## Workflow per batch

1. **Generate** the pages for the batch (following WIKI_GUIDE.md and the Thor reference), including `nav` in
   `mkdocs.yml` and the section index pages.
2. **Build:** `.\.venv\Scripts\mkdocs.exe build --strict` (prefix `NO_MKDOCS_2_WARNING=1` in Git Bash to hide the
   MkDocs 2 notice). It must exit with no warnings. Strict mode does not fail on broken `#anchor` links: treat
   any `INFO` line about a missing anchor as a failure too.
3. **Report:**
   - a **verification table**: every number used → source file and line or config name;
   - a **TODO list**: everything marked `TODO: verify` in the pages, plus anything derived or uncertain.
4. **Wait for the user's review.** Apply feedback; update WIKI_GUIDE.md for any new decision.
5. **Commit and push only when the user approves.** Never commit or push automatically.
6. **Update the progress tracker below** as part of the approved batch.

## Local setup

- Python venv in `.venv` (`pip install -r requirements.txt`). `site/` and `.venv/` are git-ignored.
- Preview: `.\.venv\Scripts\mkdocs.exe serve`, then check light and dark mode.

## Progress tracker

Status: ✅ done · 🟡 partly done · ⬜ to do

### Demigods

Each demigod batch = the demigod page, its ability pages (or variant sections) and its attribute pages, including
shared attributes not written yet.

| Demigod | Status | Notes |
| --- | --- | --- |
| Brokkr | ✅ | |
| Eir | ✅ | |
| Fenrir | ✅ | |
| Freyja | ✅ | |
| Hel | ✅ | |
| Hraesvelgr | ⬜ | Already exist: Eagle Strength, Hare Legs |
| Kvasir | ⬜ | Already exist: Heal Over Time Blood section, Deer Endurance, Hare Legs |
| Njord | ✅ | |
| Surtr | ✅ | |
| Thor | ✅ | Reference batch |
| Ullr | ⬜ | Already exist: Summon Wolf Wolf and Heal Over Time Frost sections, Deer Endurance, Hare Legs, Wolf Speed |

### Shared attributes

| Page | Status | Notes |
| --- | --- | --- |
| `bear-strength.md` | ✅ | Thor batch |
| `deer-endurance.md` | ✅ | Eir/Fenrir batch |
| `eagle-strength.md` | ✅ | Eir batch |
| `hare-legs.md` | ✅ | Eir/Fenrir batch |
| `titan-legs.md` | ✅ | Thor batch |
| `valkyrie.md` | ✅ | Eir batch |
| `wolf-speed.md` | ✅ | Fenrir batch |

### Other sections

| Section | Status | Notes |
| --- | --- | --- |
| Home (`index.md`) | 🟡 | Summary and server-defaults disclaimer only |
| Getting Started | 🟡 | Glossary done; Becoming a Demigod, Controls and Hotkeys, Energy, Demigod Skill and Progression, Ability Infusion to do |
| Abilities | 🟡 | Teleport + Brokkr's, Eir's, Fenrir's, Freyja's, Hel's, Njord's, Surtr's and Thor's abilities done |
| Items | ⬜ | Demigod Runestone, Infusion Items, Permanent Consumables, Infused Megingjord, Sweet Fish Foods, Abyssal Harpoon |
| Companions | ⬜ | |
| Reference | ⬜ | Difficulty and Server Settings, Optional Features, Compatibility, FAQ, Changelog |

## Open items

Remove an item once it is resolved.

### Before sharing the wiki

- **Mod 1.9.1 must be released first.** The wiki already describes it, including the sneak-attack changes and the
  fixes made during the Freyja/Hel/Njord/Surtr batch (Burning Ground, Crush, Sacrifice, Raider, Water Sphere; mod
  commits up to `6d943d6`).
- **Check the damage display** (total on top, smaller `nd-split` breakdown line) in light and dark mode with
  `mkdocs serve`. It was only checked in the generated HTML.

### Questions for the mod (not answered yet)

- **Wolf data on logout (possible bug, untested):** `SE_Wolf.OnDestroy` calls `AbilityWolf.Stop()`. If the game
  removes the wolf without it dying (e.g. 5 s after the owner logs out, or when its area unloads), its ZDO may
  already be gone, so `Stop()` takes the "dead" branch and deletes its name, hits and stars
  (`AbilityWolf.cs:254-266`). Test: summon a wolf with stars, log out and back in, summon again.
- **Sneak and swim speed ignore `Special Movement Speed Modifier (%)`** (`SE_Demigod.GetSneakSpeedModifier`,
  `GetSwimSpeedModifier`), although the setting's description says it scales speed from "special sources from this
  mod (such as attributes)". Scale them, or change the description. The guide currently says they are not scaled.
- **Elemental Shield, infused:** eitr and stamina regeneration pause while burning, poisoned, frozen, shocked or
  freezing (`SE_ElementalShield.cs:45`). The user's notes said eitr has no conditions. The wiki documents the code.
- **Wind Aura tooltip** says stamina regenerates "when not sprinting"; the code also requires not being
  encumbered while on the ground (`AttributeWindAura.cs:63`). Relevant for the Hraesvelgr batch.

### `TODO: verify` in the pages

- `docs/abilities/holy-conjuration.md`: fish names (vanilla names of the fish spawned per biome).
- `docs/abilities/ice-shards.md`: shards per cast (Staff of Embers cast with Staff of Frost shards).
- `docs/abilities/slash.md`, `docs/attributes/titan-arms.md`: rounding of the Lv 50, Unarmed skill 100 value.
- `docs/attributes/purity.md`: Spirit damage scope (the tooltip says "all spirit damage").
- `docs/demigods/eir.md`: Spirit piercing on the first hit, and in multiplayer when another player's game controls
  the enemy.
- `docs/demigods/fenrir.md`: Fenris full-set skill bonus (assumed to be the vanilla Unarmed bonus); display name
  of the Berserkir set.
- `docs/demigods/freyja.md`: Poison piercing on the first hit and in multiplayer (same question as Eir).
- `docs/abilities/meteor.md`: explosion radius and tool tier (vanilla `projectile_meteor`).
- `docs/abilities/fireball.md`: explosion radius (vanilla Staff of Embers projectile).
- `docs/abilities/crush.md`: the strike's damage (the equipped weapon's secondary attack, with the knife animation).
- `docs/abilities/tornado.md`: damage to trees, rocks and buildings (it also hits destructible objects).

### For later batches

- **Changelog page:** use the player README's release notes (1.9.1 has a "Sneak attacks" entry); link to them,
  do not copy them.
- **Holy Sun tar burning:** still needs `Enable Experimental Features` and does not work in multiplayer; document
  it on the Optional Features page too.
- **Hunter (Ullr batch):** its extra skins only come from creatures that are enemies of the nearby Hunter player,
  never from tamed creatures or companions (`NorseDemigods.cs:2534`). The same 50 m / closest-player rule as Raider.
