# CLAUDE.md

## Project

Player-facing gameplay wiki for the Valheim mod **Norse Demigods**.

- Built with MkDocs Material; deployed to GitHub Pages by GitHub Actions (`.github/workflows/deploy.yml`) on every
  push to `main`.
- Live site: <https://brewland.github.io/NorseDemigodsWiki/>
- Repository: <https://github.com/Brewland/NorseDemigodsWiki>

## Rules

- **Always read and follow [WIKI_GUIDE.md](WIKI_GUIDE.md) before writing or editing pages.** It is the complete
  rulebook: sources, conventions, styling, CSS classes, templates, search metadata.
- **Mod source:** `../NorseDemigods/NorseDemigods` is the only source of truth for numbers. It is **read-only**:
  never modify anything outside this repository.
- **Reference example:** for a new page, match the existing page of the same type (Thor for demigods,
  `lightning-strike.md` for abilities, `static-body.md` for attributes).
- **Decisions go into the guide.** Any style or convention decision the user makes in chat must be written into
  WIKI_GUIDE.md in the same change, so the guide alone is enough to produce identical-looking pages.

## Workflow

1. **Edit** the pages, including `nav` in `mkdocs.yml` and the section index pages when pages are added or moved.
2. **Build:** `.\.venv\Scripts\mkdocs.exe build --strict` (in Git Bash, prefix
   `NO_MKDOCS_2_WARNING=1 DISABLE_MKDOCS_2_WARNING=true` to hide the MkDocs 2 notices). It must exit with no
   warnings. Strict mode does not fail on broken `#anchor` links: treat any `INFO` line about a missing anchor as a
   failure too.
3. **Report:** a **verification table** for every number used (→ source file and line or config name), and
   anything derived or uncertain.
4. **Wait for the user's review.** Apply feedback; update WIKI_GUIDE.md for any new decision.
5. **Commit and push only when the user approves.** Never commit or push automatically.

## Local setup

- Python venv in `.venv` (`pip install -r requirements.txt`). `site/` and `.venv/` are git-ignored.
- Preview: `.\.venv\Scripts\mkdocs.exe serve`, then check light and dark mode.
