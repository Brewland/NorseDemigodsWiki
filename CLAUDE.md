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
| Hraesvelgr | ✅ | |
| Kvasir | ✅ | |
| Njord | ✅ | |
| Surtr | ✅ | |
| Thor | ✅ | Reference batch |
| Ullr | ✅ | |

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
| Getting Started | ✅ | Setup (Installing the Mod, Recommended Mods, Compatibility, Difficulty, Optional Features) and Playing (How the Mod Works, Controls and Hotkeys, Progression, Energy, First Steps). No Ability Infusion page: infusion is on each ability page |
| Abilities | ✅ | All 54 ability pages and Teleport |
| Items | ✅ | Demigod Runestone, Abyssal Harpoon, Infused Megingjord, Infusion Items, Permanent Consumables, Sweet Fish Foods |
| Companions | ✅ | One overview page comparing every companion |
| Help | ✅ | FAQ (from the Discord export), Troubleshooting, Console Commands |
| Reference | ✅ | Glossary (moved from Getting Started), Changelog (links the release notes) |

## Open items

Remove an item once it is resolved.

### Before sharing the wiki

- **Mod 1.9.1 must be released first.** The wiki already describes it, including the sneak-attack changes and the
  fixes made during the Freyja/Hel/Njord/Surtr batch (Burning Ground, Crush, Sacrifice, Raider, Water Sphere), the
  Hraesvelgr/Kvasir/Ullr batch (Holy Strike swing, Infused Arrow crossbows in `Demigods.yaml`, Vortex tooltip in all
  languages), the Getting Started batch (Find Closest Bosses pins the Queen and Fader, Difficulty scales only creature
  damage, `Ignore Non Teleportable Items` description) and the 2026-11-04 review (sneak and swim speed scaled by
  `Special Movement Speed Modifier (%)`, Hraesvelgr's airborne experience uses the experience modifiers, switching
  demigods resets progress, Purity boosts all Spirit damage, elemental piercing per hit and in multiplayer for the
  demigod's own hits, Bloody Archer's eitr burst only on the arrow's target, a wolf left behind or unloaded keeps its
  data, "obtain the head of the next boss" tooltip, Corruption tooltip without timings). All are committed in the
  mod (up to `fc62316`) but not released yet.
- **Infused Morgenheart +25% damage** (was 20%): changed in the mod by `norsedemigods-7e`
  (`AttributeInfusedMorgenHeart.cs:14`, README table and 1.9.1 release notes) but **not committed** there yet. The
  wiki already shows 25%.

### Parked indefinitely

Not planned. Do not bring these up as open work.

- **Saving energy:** the user decided not to do it. `norsedemigods-7e` had proposed a separate custom-data key,
  restored on login (clamped to max), reset to 0 on death and when switching demigods. If it is ever revived,
  update `energy.md`.

### `TODO: verify` in the pages

- `docs/abilities/crush.md`: the strike in game. With a spear, Crush throws and drops the spear (user-tested); the
  fix was requested from `norsedemigods-7e` on 2026-11-05. Update the page from its reply.
- `docs/abilities/meteor.md`: explosion radius and tool tier (vanilla `projectile_meteor`). The user will confirm.
- `docs/abilities/fireball.md`: explosion radius (vanilla Staff of Embers projectile). The user will confirm.
