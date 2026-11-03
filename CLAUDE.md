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
| Freyja | ⬜ | Already exist: Dash Nature and Heal Over Time Nature sections, Stagger, Deer Endurance, Eagle Strength, Hare Legs, Valkyrie, Wolf Speed |
| Hel | ⬜ | |
| Hraesvelgr | ⬜ | Already exist: Eagle Strength, Hare Legs |
| Kvasir | ⬜ | Already exist: Heal Over Time Blood section, Deer Endurance, Hare Legs |
| Njord | ⬜ | Already exist: Restoration Water section, Bear Strength, Titan Legs |
| Surtr | ⬜ | Already exist: Elemental Shield Fire and Slash Fire sections, Bear Strength, Titan Legs |
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
| Abilities | 🟡 | Teleport + Brokkr's, Eir's, Fenrir's and Thor's abilities done |
| Items | ⬜ | Demigod Runestone, Infusion Items, Permanent Consumables, Infused Megingjord, Sweet Fish Foods, Abyssal Harpoon |
| Companions | ⬜ | |
| Reference | ⬜ | Difficulty and Server Settings, Optional Features, Compatibility, FAQ, Changelog |
