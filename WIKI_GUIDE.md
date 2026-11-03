# Wiki Writing Guide

The rulebook for anyone, human or AI, who writes or edits pages in this wiki. Read it fully before writing a page.

**Reference batch:** Thor is the approved example of every rule in this guide: `docs/demigods/thor.md`, its
ability pages (`lightning-strike`, `dash`, `lightning-aura`, `lightning-storm`, `restoration`, `teleport`), its
attribute pages (`attributes/static-body.md`, the Bear Strength and Titan Legs sections) and the glossary. When
this guide leaves a detail open, copy what the matching Thor page does.

## 1. Audience

- Write for **players** (and server admins tuning their server), not developers. The wiki is built to be
  searched and to be quoted by AI assistants, so every page must stand on its own.
- No implementation details: no class names, code, Harmony patches, prefab internals, file paths or internal
  formulas. The only technical identifiers allowed on pages are the **Config ID** and the **config section/key**
  (admins need them to find settings).
- Plain language, short sentences, scannable tables. Use American spelling, matching the mod ("armor", "favorite").
- Do not try to avoid overlap with the in-game compendium or the NorseDemigodsUI addon's built-in wiki.
  The wiki serves a different audience.

## 2. Source of truth

The mod source at `../NorseDemigods` is the **only** source of truth. It is **read-only**: never modify it.

- **Every number must come from the code defaults.** Never guess, estimate, round loosely or reuse values
  from memory, forums, screenshots or a local BepInEx `.cfg` file (those may be changed by the user, and
  mod updates reset them unless auto-update is turned off).
- If something is unclear, contradictory or not found, write `TODO: verify` (optionally with a short reason,
  e.g. `TODO: verify (duration depends on charge time)`) instead of inventing an answer.
- Order of authority, highest first:
  1. Default values in `SetupConfigs` (`config.Bind(...)` calls) and the code that uses them.
  2. Shipped data files: `NorseDemigods/_Publish/Demigods.yaml` (class kits, inputs, weapon skills, themes)
     and `NorseDemigods/_Publish/Consumables.json` (recipes, stations, food stats).
  3. English localization `NorseDemigods/_Publish/Translations/English/EN-NorseDemigods.json`: display names
     and tooltip wording. Tooltip numbers are placeholders (`{0}`); fill them from the code.
  4. `NorseDemigods/_Publish/README.md`: secondary. If it disagrees with the code, follow the code.
- **Default values only.** Assume every setting is at its default: `Difficulty` = `Vanilla`,
  `(Special Modifiers)` at 100%, no Infused Liquid Frost or Infused Morgenheart consumed, and the shipped
  `Demigods.yaml`. Some tooltips are scaled by these (e.g. Elemental Shield by Difficulty), so the in-game
  tooltip may differ on a changed server.
- Record the mod version you verified against in the HTML comment at the end of each page
  (the current version is `PluginVersion` in `NorseDemigods/NorseDemigods.cs`).
- **Vanilla Valheim facts** (e.g. tool tiers, how status-effect speed bonuses apply) may be used when the mod
  relies on vanilla behavior. Verify them against the game itself: the decompiled `assembly_valheim.dll`
  (`ilspycmd`) or the game's data files. Community sources (wikis, data dumps) are only a cross-check, and
  the game wins when they disagree. Label such values as vanilla on the page (e.g. "These are vanilla Valheim
  values, not mod settings.").

### Settled decisions

- **Hraesvelgr is fully released.** The player README still marks him as experimental (asterisk and footnote);
  that is outdated. The code does not lock him. Do not label him "If enabled".
- **Holy Sun burning tar** works only with `[(General)] Enable Experimental Features` = `true`, and does not work
  in multiplayer yet. Mention it on the Holy Sun page with an "If enabled" label.
- **No controller support.** Gamepad bindings are commented out in the code. Do not document controller controls.
- **Changelog** links to the mod's release notes. Do not copy them into the wiki.
- **Images:** add an image placeholder on every page now (see templates); screenshots come later.
  Icons and models live in the Unity bundle and cannot be extracted from the source scan.
- **Server-defaults disclaimer:** the sentence "Values shown are server defaults; your server may differ." appears
  **once**, as a normal paragraph in the body of the home page (`docs/index.md`). No site-wide banner, and do not
  repeat it on other pages.
- **No unarmed note for attack-speed bonuses.** Do not state whether weapon attack-speed bonuses apply to
  unarmed attacks unless the mod code handles unarmed explicitly.
- **Movement speed bonuses** that go through the mod's status effect apply to all movement (walking, jogging,
  sprinting, crouching, swimming), whatever the config text says. Write "Movement speed (all movement,
  including swimming)".

## 3. Conventions

### Names and IDs

- Always use the **English display name** from the localization file, never the internal ID, in titles and text.
  Known differences:

  | Config ID | Display name |
  | --- | --- |
  | `ElementalGolem` | Stone Golem |
  | `Enraged` | Enrage |
  | `RegenerativeFlesh` | Regenerative Body |
  | `Wolf` | Summon Wolf |
  | `Surtling` | Summon Surtling |
  | `InfusedBeltStrength` (based on `BeltStrength`) | Infused Megingjord |

- Every demigod, ability, attribute and item page or section has a small **Config ID** field for admins:
  - Demigods, abilities, attributes: the `id` used in `Demigods.yaml` (e.g. `Slash`).
  - Items: the `Prefab` name in `Consumables.json`, or the custom item name in the code (e.g. `DemigodRunestone`).
- Config sections are generated by splitting the class name into words: `AbilitySlash` → `Ability Slash`,
  `AttributeHareLegs` → `Attribute Hare Legs`, `DemigodThor` → `Demigod Thor`. Keys follow the same rule,
  with the unit in brackets when present, e.g. `[Ability Slash] Ability Cooldown (seconds)`.
  Write settings as `` `[Section] Key` ``.

### Inputs

Inputs are written as **keyboard keys** with `pymdownx.keys` (`++key++`), followed by the input's name in
brackets. Show the **default** binding; players can rebind every key.

- One input per line. Never split an input across lines: in tables, one input per cell (use `<br>` between
  inputs); in cards, the input is its own paragraph. Key groups never wrap (CSS keeps them on one line).
- Combine keys with ` + ` between key groups: `++mouse-side-up++ + ++block++`.

| YAML input | Write on pages as | Renders as |
| --- | --- | --- |
| `SLOT_1` | `++mouse-side-up++ (Ability A)` | Upper Side Mouse (Ability A) |
| `SLOT_2` | `++mouse-side-down++ (Ability B)` | Lower Side Mouse (Ability B) |
| `SLOT_3` | `++mouse-side-up++ + ++block++ (Ability C)` | Upper Side Mouse + Block (Ability C) |
| `SLOT_4` | `++mouse-side-down++ + ++block++ (Ability D)` | Lower Side Mouse + Block (Ability D) |
| `SPECIAL_ATTACK` | `++mouse-middle++ (Special attack, clubs or axes)` | Middle Mouse (…), list the weapon types from `skills:` |
| `SPECIAL_ATTACK_BLOCKING` | `++block++ + ++mouse-middle++ (Special attack while blocking, …)` | Block + Middle Mouse (…) |
| `SPECIAL_ATTACK_AIR` | `++mouse-middle++ (Special attack while airborne)` | Middle Mouse (…) |
| Teleport | `++p++ (Teleport)` | P (Teleport) |
| Ignore special attack | `++left-alt++ + ++mouse-middle++` | Left Alt + Middle Mouse |

Where the defaults come from:

- **Ability A / B / Teleport / Ignore special attack:** `[(Hotkeys)]` in `Configs.cs` (`Mouse4`, `Mouse3`, `P`,
  `LeftAlt`). Unity numbers mouse buttons from 0 (`Mouse0` = left), so the config's `Mouse4` is the 5th button
  and `Mouse3` the 4th. Never write "Mouse 4" or "Mouse 5" on pages; players know them as the side buttons:
  - `++mouse-side-up++` (**Upper Side Mouse**, config `Mouse4`): the side button furthest from the fingers
    (the upper one when looking down at the mouse).
  - `++mouse-side-down++` (**Lower Side Mouse**, config `Mouse3`): the other side button.
  Keep key labels short; explanations go in text outside the key, never inside it.
- **Ability C / D:** no hotkey by default; the mod uses Ability A / B while blocking.
- **Special attack** is Valheim's *secondary attack* (default: middle mouse); **block** is Valheim's block
  (default: right mouse). `++block++` means "hold your block key".

Custom key names are defined under `pymdownx.keys` → `key_map` in `mkdocs.yml`: `mouse-side-up`,
`mouse-side-down`, `mouse-middle`, `block`. Add new ones there; never invent a key name that is not in the key map or the
[built-in list](https://facelessuser.github.io/pymdown-extensions/extensions/keys/#key-map-index).

### Damage and healing

- **Numbers in bold**, **damage type as a colored badge** after the number. Never write the type in brackets.

  | Case | Markdown | Renders as |
  | --- | --- | --- |
  | One type | `**80** *Lightning*{.dmg .lightning}` | **80** [Lightning] |
  | Several types | `**5** = **2.5** *Blunt*{.dmg .blunt} + **2.5** *Fire*{.dmg .fire}` | **5** = **2.5** [Blunt] + **2.5** [Fire] |
  | Weapon-relative | `**100%** of weapon damage = **75%** *Slash*{.dmg .slash} + **25%** *Fire*{.dmg .fire}` | |

  Lead with the **in-game total** (what the tooltip shows), then the split. Example: Fireball's config is 2.5 per
  type, but the tooltip shows 5.
- Damage is a base amount plus an amount [per level](getting-started/glossary.md#per-level). Put scaling
  values in a **level table** with the columns `Lv 0 / Lv 50 / Lv 100` (demigod skill level), one row per value.
  Right-align the level columns. When a row has a single damage type, put the badge in the **row label** and
  only bold numbers in the cells:

  ```markdown
  | | Lv 0 | Lv 50 | Lv 100 |
  | --- | ---: | ---: | ---: |
  | Damage *Lightning*{.dmg .lightning} | **10** | **80** | **150** |
  | Range | 12 m | 15 m | 18 m |
  ```

  Mixed-type rows keep the badges in each cell. Non-damage values (range, carry weight) are not bold.
  Variant rows name the demigod before the badge: `| Path damage, Thor *Lightning*{.dmg .lightning} | **10** | … |`.
- A column that holds one damage type may carry the badge in its **header**:
  `| Weapon | Extra damage *Lightning*{.dmg .lightning} |` (see Static Body).
- **Bold** marks damage and healing amounts only, including a damage share in prose ("deal **35%** of the hit's
  damage as *Lightning*{.dmg .lightning}"). Percentage bonuses in effect tables (`+10%`) are not bold.
- State the formula in one short line above the table: "10 base + 1.4 per level".
- Mark time-based values clearly: "per second", "every X seconds".
- Values are before enemy armor, resistances and weaknesses. Round the way the in-game tooltip does
  (most tooltips show whole numbers); if unsure, give one decimal and add `TODO: verify`.
- Healing follows the same rules (bold numbers, level table, caps stated explicitly), without a badge.
- Resistances and weaknesses: badge, then the level in plain text: `*Lightning*{.dmg .lightning} Very resistant`.

### Numbers and units

- Units after a space, abbreviated in infoboxes and tables: `3 s`, `12 m`, `+20%`. In prose, "seconds" is fine.
- Ranges with an en dash and no spaces: `12–18 m`, `7.5–12.5`. Negative changes with a real minus sign:
  `−40%`. Multipliers with `×`: `×3 (300%)`.
- Changes as before → after: `Eitr cost: 40 → 30`.
- "None" for a cost or cooldown that is zero (`**Cooldown** | None`).
- Minimum resource needs as `Needs 1+ energy; drains 1 every 4 s`.
- In-game messages in italics with quotes: `In-game message: *"You have not claimed a bed yet"*`.

### Writing style

- **Short bullet lists over long sentences.** One fact per bullet.
- **No paragraph longer than 3 lines** (about 3 × 100 characters as rendered). Split or convert to bullets.
- Numbered lists only for sequences (what happens, in order).
- Tables for anything with two or more comparable values.

### Spoilers

Infusion recipes are deliberately hidden in the game. Put them **inside a collapsible spoiler box**, on the demigod
page and on the Infusion Items page. This also applies to Kvasir's infusion condition, which is not a recipe.
Use exactly this form:

```markdown
??? spoiler "Infusion recipe (spoiler)"

    | Material | Amount |
    | --- | --- |
    | Thunderstone | 1 |
```

Food, Runestone, Megingjord and permanent consumable recipes do not need a spoiler.

### Off-by-default features

Anything disabled by default is labelled **"If enabled"** and names the setting. Off-by-default features
(extra merchant items, the Queen Bee spawn chance, boss/merchant map pins, ward protection, and so on)
are documented on the **Optional Features** page.

- Whole page or section: put this admonition directly under the summary:

  ```markdown
  !!! info "If enabled"
      Off by default. Requires `[Merchant] Enable Custom Merchant Items` = `true`.
  ```

- Single table row or sentence: prefix with **If enabled:**.

Check each default in `Configs.cs` before labelling it. Default `false` at the time of writing:
`[(General)] Enable Experimental Features`, `[(General)] Find Closest Bosses`, `[(General)] Find Closest Merchants`,
`[(General)] Protect Pieces Covered By Ward`, `[Merchant] Enable Custom Merchant Items`,
`[Skills] Enable Skill Loss On Death`, `[Runestone] Runestone Consumable`,
`[Teleportation] Ignore Non Teleportable Items`, `[Honey] Ignore Beehive Proximity Check`.
Teleport and Harpoon Fishing are **on** by default.

### Configurable class kits

Servers can change which abilities and attributes each demigod has (`Demigods.yaml`). Every demigod page
carries this note after the infobox and image placeholder, directly before the Lore box:

```markdown
!!! note
    This is the default loadout. Servers can change which abilities and attributes each demigod has.
```

### Compatibility

Every entry on the compatibility page is labelled:

- **Confirmed**: the mod code handles or patches it (e.g. a compatibility setting or patch exists), or the
  mod author has stated it.
- **User-reported**: reported by players (e.g. on Discord) and not verified in code. Include these as-is.

### Exclusions

- **Saiyan is excluded.** It is a hidden test class reachable only with an admin command. Do not document it,
  its exclusive abilities (Arcane Bolt, Blink, Sharp Mist), its `ARCANE` themes (Elemental Shield, Restoration,
  Titan Arms), its attributes (Saiyan Body, Saiyan Strength) or the `MakeMeSaiyan` console command.

### Linking

- Use relative links to `.md` files so `mkdocs build --strict` can check them:
  `[Surtr](../demigods/surtr.md)`.
- Link the **first** use of a glossary term on each page:

  | Term | Link target | Meaning (verify against the code) |
  | --- | --- | --- |
  | heavy armor | `getting-started/glossary.md#heavy-armor` | Any armor piece with a movement penalty of 5% or more |
  | per level | `getting-started/glossary.md#per-level` | Per demigod skill level (0–100) |
  | specialized weapons | `getting-started/glossary.md#specialized-weapons` | The weapon types an attribute's bonus applies to |
  | tool tier | `getting-started/glossary.md#tool-tier` | Which trees and ores an ability or attribute can damage |

- Every new page must be added to `nav` in `mkdocs.yml`, under its section, after that section's `index.md`.
  Order within a section:
  - **Demigods:** alphabetical.
  - **Abilities:** Teleport first, then alphabetical.
  - **Attributes:** grouped pages first (Movement and Stamina, Strength, Valkyrie), then single-class pages
    alphabetical.
- Every new page also gets a row in its section's `index.md` table (see [Section index pages](#section-index-pages)).

### File naming

- `lowercase-kebab-case.md`, from the English display name: `docs/abilities/stone-golem.md`.
- Abilities shared by several demigods or with theme variants (Slash, Crush, Dash, Elemental Shield,
  Heal Over Time, Restoration, Stagger, Summon Wolf) get **one page with a section per variant**:
  `docs/abilities/slash.md` with `### Fire (Surtr)` and `### Frost (Fenrir)` under `## Variants`.
  Variants share one config section, so a server change affects all of them; say so on the page.
- **Single-class attributes** get their own page: `docs/attributes/static-body.md`.
- **Shared attributes** (owned by several demigods) stay on their grouped page, one `##` section each:
  `docs/attributes/strength.md#bear-strength`.

### Images

Until screenshots exist, add an image placeholder as an HTML comment right after the infobox:

```markdown
<!-- IMAGE: in-game screenshot of Slash (Fire) hitting an enemy -->
```

Replace it later with `![Description](../assets/images/<section>/<page>.png)`, storing files in
`docs/assets/images/<section>/`.

### Visual components

All custom styling lives in `docs/stylesheets/extra.css` (registered as `extra_css` in `mkdocs.yml`). It must look
right in both light and dark mode; check both with the palette toggle after changing it. Use only the classes
listed here; do not add inline `style=` attributes.

#### Infobox

Every demigod, ability, attribute and item page starts with an infobox right after the summary: a two-column
table (empty header row) wrapped in `<div class="nd-infobox" markdown>`. Player-facing fields first;
**Config ID** and **Config section** always last. Blank lines inside the `div` are required.

```markdown
<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Thor](../demigods/thor.md) |
| **Input** | ++mouse-side-up++ (Ability A) |
| **Energy cost** | 1 |
| **Cooldown** | 3 s |
| **Config ID** | `Dash` |
| **Config section** | `[Ability Dash]` |

</div>
```

Grouped attribute pages put one infobox at the top of each attribute's `##` section.

Field order (omit rows that do not apply, except where marked "always"):

| Page type | Fields, in order |
| --- | --- |
| Demigod | Role, Element (badges), Favorite weapons, Preferred armor, Config ID, Config section |
| Ability | Used by, Input, Eitr cost (only if any), Energy cost (always), Cooldown (always), Duration or Cast time, Range, other areas (e.g. Explosion radius), Config ID, Config section |
| Attribute | Demigod (single-class) or Demigods (grouped), Condition, Config ID, Config section |
| Item | Type, Crafting station, Restricted to, Stack size, Consume limit, Config ID |

- Values that scale with level appear as a range: `12–18 m, by level`; the level table has the details.
- Channeled abilities add ", hold" after the input: `++mouse-side-down++ + ++block++ (Ability D), hold`.
- Shared config sections add `(shared by all variants)` after the section.
- Element and resistance rows use damage badges: `*Lightning*{.dmg .lightning}`.

#### Lore

The demigod description goes in a quote admonition titled "Lore", directly after the class-kit note:

```markdown
!!! quote "Lore"
    Thor is the god of thunder, lightning, storms, wrestling and strength…
```

#### Card grid

Demigod pages list abilities and attributes **only** as Material grid cards that link to their pages; no details
inline. One card per ability or attribute:

- Line 1: a Material icon, then the linked name in bold.
- A `---` separator.
- The input (abilities only), as its own paragraph.
- One short sentence (max ~15 words).
- Shared attributes: a last line "Shared with Njord, Surtr."

```markdown
<div class="grid cards" markdown>

-   :material-run-fast:{ .lg .middle } [**Dash**](../abilities/dash.md#lightning-thor)

    ---

    ++mouse-side-up++ (Ability A)

    Teleport forward, damaging enemies in your path.

</div>
```

Card order:

- **Abilities:** by input: special attacks (normal, while blocking, airborne), Ability A, B, C, D, then Teleport.
- **Attributes:** the demigod's single-class attributes first, then shared attributes; alphabetical within each.

Card text rules:

- Toggles start with "Toggle: ", e.g. "Toggle: faster attacks, faster movement and stamina regeneration."
- Teleport's card always reads "Teleport to your bed and back. Shared by all demigods."
- Variant abilities link to the variant section: `../abilities/dash.md#lightning-thor`.
- Shared attributes link to their grouped section: `../attributes/strength.md#bear-strength`.

Icons come from `pymdownx.emoji` with Material's icon set (`:material-<name>:`). Browse names at
<https://pictogrammers.com/library/mdi/>; check the icon exists in
`.venv/Lib/site-packages/material/templates/.icons/material/` before using it. Reuse the same icon for the same
ability or attribute everywhere, and never give two different abilities or attributes the same icon. Icons in
use (add new ones here):

| Ability or attribute | Icon |
| --- | --- |
| Lightning Strike | `:material-lightning-bolt:` |
| Dash | `:material-run-fast:` |
| Lightning Aura | `:material-lightning-bolt-circle:` |
| Lightning Storm | `:material-weather-lightning:` |
| Restoration | `:material-meditation:` |
| Teleport | `:material-bed:` |
| Static Body | `:material-flash:` |
| Bear Strength | `:material-arm-flex:` |
| Titan Legs | `:material-shoe-print:` |

#### Section index pages

Each section's `index.md` is a one-line summary plus one entry per page, sorted alphabetically by name:

| Index | Columns | Notes |
| --- | --- | --- |
| `demigods/index.md` | Demigod, Summary, Element, Favorite weapons, Preferred armor | Element as badges |
| `abilities/index.md` | Ability, Used by, Input, Summary | Input as keys; ends with "Inputs show the default keys." |
| `attributes/index.md` | Attribute, Demigods, Summary | Shared attributes link to their grouped section |
| `getting-started/index.md` | No table: a `## Pages` bullet list | `- [Glossary](glossary.md): heavy armor, per level, …` |

Demigods without a page yet are plain text (no link) in the Used by / Demigods columns.

#### CSS class reference

| Class | Use on | Markdown example |
| --- | --- | --- |
| `nd-infobox` | `<div>` around the page's top fact table | `<div class="nd-infobox" markdown>` |
| `dmg` + type | Emphasis with `attr_list`, for damage types, elements, resistances | `*Fire*{.dmg .fire}` |
| `grid cards` | `<div>` around a card list (Material built-in) | `<div class="grid cards" markdown>` |
| `lg middle` | Card icon size and alignment (Material built-in) | `:material-flash:{ .lg .middle }` |
| `keys` | Generated by `pymdownx.keys`; CSS stops key combinations from wrapping | `++mouse-side-up++ + ++block++` |
| `admonition quote` | Lore box, recolored to the accent color | `!!! quote "Lore"` |

Damage-type classes (always together with `dmg`): `blunt`, `slash`, `pierce`, `chop`, `pickaxe`, `fire`,
`frost`, `lightning`, `poison`, `spirit`. Use the badge for **damage types and elements only**, not for
themes or status effects. Write the visible text with a capital letter: `*Poison*{.dmg .poison}`.

Badge colors (from `extra.css`; solid background, so they read the same in light and dark mode):

| Class | Background | Text |
| --- | --- | --- |
| `blunt` | `#795548` brown | white |
| `slash` | `#b03a3a` red | white |
| `pierce` | `#3f51b5` indigo | white |
| `chop` | `#5d4037` dark brown | white |
| `pickaxe` | `#546e7a` blue-gray | white |
| `fire` | `#d84315` orange | white |
| `frost` | `#4fc3f7` light blue | dark |
| `lightning` | `#fdd835` yellow | dark |
| `poison` | `#7cb342` green | dark |
| `spirit` | `#8e24aa` purple | white |

The theme colors are CSS variables at the top of `extra.css`; `mkdocs.yml` uses `primary: custom` and
`accent: custom` for both palettes:

| Variable | Light | Dark (`slate`) |
| --- | --- | --- |
| Primary (header) | `#24394d` fjord blue | `#1a2836` |
| Accent | `#b07a22` bronze | `#e2b354` gold |
| Links | `#2a5d88` | `#8cbbe3` |
| Panel background / border (infobox) | `#f4f1ea` / `#d9cfbd` | `#1f2a36` / `#34465a` |

The accent color is used for the infobox's left border, the Lore box, the top border and icon of each card, and
card titles on hover. `h2` headings get a thin bottom border.

#### Required `mkdocs.yml` setup

These settings make the components work; do not remove them:

```yaml
theme:
  name: material
  custom_dir: overrides          # main.html only extends base.html (no banner)
  palette: # light + dark, both with primary: custom, accent: custom
extra_css:
  - stylesheets/extra.css
markdown_extensions:
  - admonition
  - pymdownx.details             # ??? spoiler boxes
  - pymdownx.superfences
  - tables
  - attr_list                    # damage badges, card icon classes
  - md_in_html                   # infobox and card grid divs
  - pymdownx.emoji:              # :material-...: icons
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
  - pymdownx.keys:               # ++key++ inputs
      key_map:
        mouse-side-up: Upper Side Mouse
        mouse-side-down: Lower Side Mouse
        mouse-middle: Middle Mouse
        block: Block
  - toc:
      permalink: true
```

## 4. Page templates

Every page starts with a **1–2 sentence plain-language summary** right after the title. It must make sense on
its own (search snippets and AI answers quote it). Then the infobox, then the image placeholder. Remove optional
sections that would be empty; never leave empty headings.

### Demigod

Abilities and attributes appear **only as cards** (see [Card grid](#card-grid)). All details live on their own
pages.

```markdown
# Thor

Thor is a lightning demigod who dashes at the speed of light and strikes enemies with lightning. He favors
clubs and axes and fights best in heavy armor.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Role** | … |
| **Element** | *Lightning*{.dmg .lightning} |
| **Favorite weapons** | … |
| **Preferred armor** | Heavy |
| **Config ID** | `Thor` |
| **Config section** | `[Demigod Thor]` |

</div>

<!-- IMAGE: Thor in full armor with his passive lightning effect -->

!!! note
    This is the default loadout. Servers can change which abilities and attributes each demigod has.

!!! quote "Lore"
    From the demigod description.

## Abilities

<div class="grid cards" markdown>

-   :material-lightning-bolt:{ .lg .middle } [**Lightning Strike**](../abilities/lightning-strike.md)

    ---

    ++mouse-middle++ (Special attack, unarmed)

    One short sentence.

-   … one card per ability, in input order: special attacks, A, B, C, D, Teleport

</div>

## Attributes

<div class="grid cards" markdown>

-   :material-flash:{ .lg .middle } [**Static Body**](../attributes/static-body.md)

    ---

    One short sentence.

-   :material-arm-flex:{ .lg .middle } [**Bear Strength**](../attributes/strength.md#bear-strength)

    ---

    One short sentence.

    Shared with Njord, Surtr.

</div>

## Demigod skill experience

Thor gains demigod skill experience from dealing and taking damage.

| Source | Experience gained |
| --- | --- |
| Damage dealt with abilities | X per 100 damage |

## Infusion

- One bullet per ability: [Ability](../abilities/….md#infused): what infusion adds, in a few words.

!!! tip "In-game hint"
    *"First § paragraph of `demigod_<id>_overview_ext`, in full (it says where to craft, e.g. 'a highly
    equipped forge'), without color tags or the §."*

Other § paragraphs of `_overview_ext` (e.g. Fenrir's Fenris Set) belong in Class quirks.

??? spoiler "Infusion recipe (spoiler)"

    Craft an **Infused Hammer** at a Forge (level 7+) and consume it.

    - Only Thor can consume it.
    - It can be consumed only once.

    | Material | Amount |
    | --- | --- |
    | … | … |

## Class quirks

Class-specific rules (e.g. armor sets, unarmed skill), as bullets, if any.

## Related pages

- …

<!-- Verified against NorseDemigods x.y.z -->
```

### Ability

```markdown
# Slash

Slash is a special attack that damages enemies in front of you with a claw slash and also chops trees.
Surtr's version deals fire damage and Fenrir's deals frost damage.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Surtr](../demigods/surtr.md), [Fenrir](../demigods/fenrir.md) |
| **Input** | ++mouse-middle++ (Special attack, …) |
| **Eitr cost** | X (omit if none) |
| **Energy cost** | X or None |
| **Cooldown** | X s or None |
| **Duration** | X s (omit if instant) |
| **Range** | X m (omit if not relevant) |
| **Config ID** | `Slash` |
| **Config section** | `[Ability Slash]` (shared by all variants) |

</div>

<!-- IMAGE: in-game screenshot of Slash hitting an enemy -->

Both variants share one config section: a server change affects Surtr and Fenrir alike.

## Effect

1. What happens, in order, one step per item.

## Damage

10 base + 1.4 [per level](../getting-started/glossary.md#per-level).

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Damage *Fire*{.dmg .fire} | **…** | **…** | **…** |

- Damage to trees and ores, tool tier, chance to regain energy on hit (if any).

## Variants

### Fire (Surtr)

- Differences only (damage type, effects).

### Frost (Fenrir)

- …

## Infused

- What infusion adds (values at default settings).

## Limits

- When the ability cannot be used (e.g. underground, target too strong).

## Notes

- Interactions and tips derivable from the code.

## Related pages

- …

<!-- Verified against NorseDemigods x.y.z -->
```

### Attribute (single-class)

```markdown
# Static Body

One-sentence summary of this attribute.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Demigod** | [Thor](../demigods/thor.md) |
| **Condition** | Always active / e.g. only when not wearing heavy armor, out of combat, sneaking |
| **Config ID** | `StaticBody` |
| **Config section** | `[Attribute Static Body]` |

</div>

<!-- IMAGE: Static Body attribute icon -->

## Effects

| Effect | Value |
| --- | --- |
| … | … |

## Scaling

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| … | … | … | … |

## Resistances

- *Lightning*{.dmg .lightning} Very resistant

## Notes

- …

## Related pages

- …

<!-- Verified against NorseDemigods x.y.z -->
```

Split long effect lists into themed `##` sections (e.g. "Weapon damage", "Defense") when that reads better.

### Attribute (grouped)

Only for attributes shared by several demigods; one `##` section per attribute, each with its own infobox.

```markdown
# Movement and Stamina Attributes

Passive attributes that make demigods run faster, jump higher or use less stamina.

<!-- IMAGE: attribute icons -->

| Attribute | Demigods | Summary |
| --- | --- | --- |
| [Hare Legs](#hare-legs) | Eir, Fenrir, … | … |

## Hare Legs

One-sentence summary of this attribute.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Demigods** | [Eir](../demigods/eir.md), … |
| **Condition** | Always active / … |
| **Config ID** | `HareLegs` |
| **Config section** | `[Attribute Hare Legs]` |

</div>

| Effect | Value |
| --- | --- |
| Run speed | +X% |

Add a `Lv 0 / Lv 50 / Lv 100` table if the attribute scales. List resistances and weaknesses if it grants any.

### A sub-topic (e.g. Landing blast)

- Longer topics get `###` subsections inside the attribute's `##` section.

**Notes:**

- Short notes use a bold "Notes:" label instead of a heading.

<!-- Verified against NorseDemigods x.y.z -->
```

Placeholders for attributes added in later batches stay as HTML comments under the overview table, e.g.
`<!-- Eagle Strength (Eir, Freyja, Hraesvelgr) will be added in a later batch. -->`.

### Item

```markdown
# Infused Megingjord

Infused Megingjord is an equippable belt that increases your maximum energy and carry weight.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Type** | Equipment / Consumable (permanent effect) / Food |
| **Crafting station** | Forge (level X+) |
| **Restricted to** | Any demigod / [Demigod](../demigods/….md) |
| **Stack size** | X |
| **Consume limit** | How many times it can be consumed, if limited |
| **Config ID** | `InfusedBeltStrength` |

</div>

<!-- IMAGE: Infused Megingjord in the inventory -->

## Effect

- Effect at default settings.

## Recipe

| Material | Amount |
| --- | --- |
| … | … |

## Related pages

- …

<!-- Verified against NorseDemigods x.y.z -->
```

Grouped item pages (Infusion Items, Permanent Consumables, Sweet Fish Foods) start with an overview table and
then repeat the infobox under one `##` section per item. Infusion recipes go in spoiler boxes. Food sections add a
stats table (health, stamina, eitr, regeneration, duration) and note that only one sweet fish type can be active
at a time.

### System

Used for Getting Started topics (Energy, Demigod Skill & Progression, Ability Infusion, …), Companions and
Reference pages. No infobox.

```markdown
# Energy

Energy is the resource demigods spend to cast abilities. It regenerates over time, and your maximum energy grows
with your demigod skill level.

<!-- IMAGE: energy display in the HUD -->

## How it works

- Plain-language explanation, as bullets.

## Default values

| Setting | Default | Config |
| --- | --- | --- |
| Maximum energy at level 0 | X | `[Energy] Energy At Base Level` |

## Tips and interactions

- …

## Related pages

- …

<!-- Verified against NorseDemigods x.y.z -->
```

## 5. Source-file map

Paths are relative to `../NorseDemigods/NorseDemigods/`. Translation keys are in
`_Publish/Translations/English/EN-NorseDemigods.json`.

### Ability page

| Field | Source |
| --- | --- |
| Name, description, infused effect, status line | Translation keys `ability_<id>_name`, `_tooltip`, `_infused_tooltip`, `_status_tooltip` |
| Used by, input, weapon-skill restriction, theme | `_Publish/Demigods.yaml` |
| Energy, eitr, cooldown, duration, damage base/per level, damage types, tree/ore damage, tool tier, energy-on-hit %, infused values | `Abilities/Ability<Id>.cs`: `SetupConfigs` defaults, `ModifyWeaponSharedData` |
| Damage at levels 0 / 50 / 100 (calculated) | The same configs |
| Usage limits ("not underground", "too strong") | Translation keys `ability_<id>_interior`, `_too_strong`, etc. |
| Default hotkeys | `Configs.cs` (`(Hotkeys)`) |
| Shared rules (cooldown, energy, inputs, infusion) | `DemigodAbility.cs` |
| Linked status effects and summons | `StatusEffects/SE_*.cs`, `Controllers/*.cs`, `WorkerAI.cs` |

### Attribute page

| Field | Source |
| --- | --- |
| Name, description | Translation keys `attribute_<id>_name`, `_tooltip` |
| Conditions and numbers | `Attributes/Attribute<Id>.cs` (`SetupConfigs` defaults and logic) |
| Owning demigods, theme | `_Publish/Demigods.yaml` |
| Resistances and weaknesses | Tooltip text and the attribute code |
| Heavy armor check | `Helper.cs` (`PlayerWearingHeavyArmorCount`) |
| Specialized-weapon bonus damage | `SE_Demigod.cs` |

### Demigod page

| Field | Source |
| --- | --- |
| Lore, infusion hint | Translation keys `demigod_<id>_description`, `_overview_ext` |
| Role, elements, weapons, armor | `_Publish/README.md` Demigods table (ignore the outdated Hraesvelgr footnote) |
| Ability loadout and inputs, attributes | `_Publish/Demigods.yaml` |
| How it gains experience | `Demigods/Demigod<Id>.cs` (`SkillDemigodXp*`) |
| Infusion recipe or condition | `_Publish/Consumables.json` (`RestrictedToDemigod`); Kvasir: `Demigods/DemigodKvasir.cs` |
| Class quirks (e.g. Fenrir armor sets, unarmed skill) | `Demigods/*.cs`, `NorseDemigods.cs`, `Configs.cs` |
| Passive effects | `StatusEffects/SE_Demigod<Id>.cs`, `SE_Demigod.cs` |

### Item page

| Field | Source |
| --- | --- |
| Recipe, station and level, stack size, food stats | `_Publish/Consumables.json` |
| Runestone and Megingjord recipes | `Configs.cs` (`Runestone`, `Enhanced Megingjord`), `NorseDemigods.cs` |
| Effects and consume limit (`MaxLevel`) | `Attributes/AttributeInfused*.cs` |
| Names and descriptions | Translation keys `item_*`, `attribute_infused*` |
| Consumable behavior | `CustomConsumable.cs`, `StatusEffects/SE_CustomConsumable.cs`, `StatusEffects/SE_Infused_Belt_Strength.cs` |

### System pages

| Topic | Source |
| --- | --- |
| Energy, skill caps, level loss, difficulty presets, teleport | `Configs.cs`, `Helper.cs` |
| Teleport ability | `Abilities/AbilityTeleport.cs`, `StatusEffects/SE_TeleportLocationExpiration.cs` |
| Harpoon fishing, honey, merchant, armor sets | `Configs.cs`, `NorseDemigods.cs` |
| Console commands (for Becoming a Demigod and the FAQ) | `Console/*.cs` |
| Compatibility | `Configs.cs` (`Enhance Compatibility With …`), `Patches/*.cs`, `_Publish/README.md` |

Global config sections in `Configs.cs`: `(Configs)`, `(Difficulty)`, `(General)`, `(Hotkeys)`,
`(Special Modifiers)`, `Combat`, `Energy`, `Enhanced Armor Set Berserker`, `Enhanced Armor Set Fenris`,
`Enhanced Megingjord`, `Harpoon Fishing`, `Honey`, `Merchant`, `Runestone`, `Skills`, `Teleportation`,
plus `User Interface` in `CustomUI.cs`. Ignore `(Gamepad)`: it is commented out.

## 6. Planned structure

Derived from the shipped `Demigods.yaml`, `Consumables.json` and `Configs.cs` (mod 1.9.0). Create missing
pages from this list and add each one to `nav`.

```text
docs/
├── index.md                                Home
├── stylesheets/extra.css                   Theme colors, badges, infobox (see Visual components)
├── getting-started/
│   ├── index.md
│   ├── becoming-a-demigod.md               Runestone, choosing, switching, revoking
│   ├── controls-and-hotkeys.md             Slots, special-attack combos, ignore key
│   ├── energy.md
│   ├── demigod-skill-and-progression.md    Experience, boss caps, death
│   ├── ability-infusion.md
│   └── glossary.md                         heavy armor, per level, specialized weapons, tool tier
├── demigods/
│   ├── index.md                            Overview / comparison table
│   └── brokkr.md  eir.md  fenrir.md  freyja.md  hel.md  hraesvelgr.md
│       kvasir.md  njord.md  surtr.md  thor.md  ullr.md
├── abilities/
│   ├── index.md                            All abilities (table)
│   ├── teleport.md                         Shared by all demigods
│   └── one page per ability                (table below)
├── attributes/
│   ├── index.md                            All attributes (table)
│   ├── movement-and-stamina.md             Hare Legs, Deer Endurance, Titan Legs, Wolf Speed
│   ├── strength.md                         Bear Strength, Eagle Strength
│   ├── valkyrie.md                         Eir and Freyja
│   └── one page per single-class attribute (table below), e.g. static-body.md
├── items/
│   ├── index.md
│   ├── demigod-runestone.md
│   ├── infusion-items.md                   10 sections, recipes in spoilers
│   ├── permanent-consumables.md            Bloodbag, Chitin, Earthbreaker (+ Grand), Eitr, Hard Antlers,
│   │                                       Leather Scraps, Liquid Frost, Morgenheart, Serpent Scale
│   ├── infused-megingjord.md
│   ├── sweet-fish-foods.md                 One page, table
│   └── abyssal-harpoon.md                  Abyssal Harpoon & Harpoon Fishing
├── companions/
│   └── index.md                            Overview of every summon
└── reference/
    ├── index.md
    ├── difficulty-and-server-settings.md   What players feel
    ├── optional-features.md                Off by default, "If enabled"
    ├── compatibility.md                    Confirmed / User-reported
    ├── faq.md
    └── changelog.md                        Links to the mod's release notes
```

### Abilities

54 ability pages plus Teleport (Saiyan-only abilities excluded).

| Page | Display name | Config ID | Used by (input; theme) |
| --- | --- | --- | --- |
| `acid-bolt.md` | Acid Bolt | `AcidBolt` | Hel (Special attack) |
| `blast.md` | Blast | `Blast` | Ullr (A) |
| `blood-slash.md` | Blood Slash | `BloodSlash` | Kvasir (Special attack) |
| `bomb.md` | Bomb | `Bomb` | Brokkr (A) |
| `burning-ground.md` | Burning Ground | `BurningGround` | Surtr (A) |
| `charm.md` | Charm | `Charm` | Kvasir (C) |
| `cleave.md` | Cleave | `Cleave` | Hraesvelgr (Special attack) |
| `combustion.md` | Combustion | `Combustion` | Brokkr (Airborne) |
| `crush.md` | Crush | `Crush` | Njord (Airborne; `LIGHTNING`), Surtr (Airborne; `FIRE`) |
| `dark-aura.md` | Dark Aura | `DarkAura` | Kvasir (B) |
| `dash.md` | Dash | `Dash` | Freyja (A; `NATURE`), Thor (A; `LIGHTNING`) |
| `decay-aura.md` | Decay Aura | `DecayAura` | Hel (B) |
| `drain-blood.md` | Drain Blood | `DrainBlood` | Surtr (D) |
| `elemental-shield.md` | Elemental Shield | `ElementalShield` | Eir (B; `HOLY`), Surtr (B; `FIRE`) |
| `energy-wisp.md` | Energy Wisp | `EnergyWisp` | Hraesvelgr (C) |
| `enrage.md` | Enrage | `Enraged` | Fenrir (A) |
| `fireball.md` | Fireball | `Fireball` | Surtr (Special attack) |
| `frost-nova.md` | Frost Nova | `FrostNova` | Fenrir (B) |
| `heal-over-time.md` | Heal Over Time | `HealOverTime` | Fenrir (D; `FROST`), Freyja (D; `NATURE`), Kvasir (D; `BLOOD`), Ullr (D; `FROST`) |
| `holy-conjuration.md` | Holy Conjuration | `HolyConjuration` | Eir (D) |
| `holy-heal.md` | Holy Heal | `HolyHeal` | Eir (C) |
| `holy-strike.md` | Holy Strike | `HolyStrike` | Eir (Special attack) |
| `holy-sun.md` | Holy Sun | `HolySun` | Eir (A); tar burning: If enabled, not in multiplayer |
| `ice-shards.md` | Ice Shards | `Iceshards` | Fenrir (Special attack while blocking) |
| `infused-arrow.md` | Infused Arrow | `InfusedArrow` | Ullr (Special attack) |
| `lightning-aura.md` | Lightning Aura | `LightningAura` | Thor (B) |
| `lightning-bolt.md` | Lightning Bolt | `LightningBolt` | Njord (Special attack) |
| `lightning-storm.md` | Lightning Storm | `LightningStorm` | Thor (C) |
| `lightning-strike.md` | Lightning Strike | `LightningStrike` | Thor (Special attack) |
| `lightning-torpedo.md` | Lightning Torpedo | `LightningTorpedo` | Brokkr (Special attack) |
| `meteor.md` | Meteor | `Meteor` | Hel (A) |
| `minions.md` | Minions | `Minions` | Hel (C) |
| `nano-cube.md` | Nano Cube | `NanoCube` | Brokkr (D) |
| `nature-wisp.md` | Nature Wisp | `NatureWisp` | Freyja (C) |
| `neck.md` | Neck | `Neck` | Njord (C) |
| `poison-cloud.md` | Poison Cloud | `PoisonCloud` | Freyja (B) |
| `poison-javelin.md` | Poison Javelin | `PoisonJavelin` | Freyja (Special attack) |
| `restoration.md` | Restoration | `Restoration` | Njord (D; `WATER`), Thor (D; `LIGHTNING`) |
| `sacrifice.md` | Sacrifice | `Sacrifice` | Hel (D) |
| `sense-creatures.md` | Sense Creatures | `SenseCreatures` | Ullr (B) |
| `slash.md` | Slash | `Slash` | Fenrir (Special attack; `FROST`), Surtr (Special attack; `FIRE`) |
| `soar.md` | Soar | `Soar` | Hraesvelgr (Airborne) |
| `stagger.md` | Stagger | `Stagger` | Eir, Freyja (Special attack while blocking; `BROWN`) |
| `stone-golem.md` | Stone Golem | `ElementalGolem` | Brokkr (C) |
| `stone-shield.md` | Stone Shield | `StoneShield` | Brokkr (B) |
| `summon-surtling.md` | Summon Surtling | `Surtling` | Surtr (C) |
| `summon-wolf.md` | Summon Wolf | `Wolf` | Fenrir (C; `FROST`, creature `Ulv_Friendly`), Ullr (C; `FROST`, creature `Wolf_Friendly`) |
| `telekinesis.md` | Telekinesis | `Telekinesis` | Hraesvelgr (A) |
| `teleport.md` | Teleport | `Teleport` | All demigods (Teleport hotkey) |
| `tornado.md` | Tornado | `Tornado` | Njord (B) |
| `vortex.md` | Vortex | `Vortex` | Hraesvelgr (B) |
| `warp.md` | Warp | `Warp` | Kvasir (A) |
| `water-sphere.md` | Water Sphere | `WaterSphere` | Njord (A) |
| `whirlwind.md` | Whirlwind | `Whirlwind` | Hraesvelgr (Special attack while blocking) |
| `wind-shield.md` | Wind Shield | `WindShield` | Hraesvelgr (D) |

Surtr has two `SPECIAL_ATTACK` abilities (Fireball and Slash); the weapon type decides which one triggers.
Read the `skills:` list in `Demigods.yaml` for each.

### Attributes

Shared attributes (grouped pages):

| Page | Attributes (demigods) |
| --- | --- |
| `movement-and-stamina.md` | Hare Legs (Eir, Fenrir, Freyja, Hraesvelgr, Kvasir, Ullr), Deer Endurance (Eir, Fenrir, Freyja, Kvasir, Ullr), Titan Legs (Njord, Surtr, Thor), Wolf Speed (Fenrir, Freyja, Ullr) |
| `strength.md` | Bear Strength (Njord, Surtr, Thor), Eagle Strength (Eir, Freyja, Hraesvelgr) |
| `valkyrie.md` | Valkyrie (Eir, Freyja) |

Single-class attributes (38) each get their own page, named from the display name (`static-body.md`). In `nav`,
list the grouped pages first, then the single-class pages alphabetically.

| Demigod | Attributes |
| --- | --- |
| Brokkr | Blacksmith, Gourmand, Sturdy Legs, Thunder Forger, Titan Strength |
| Eir | Holy Body, Purity |
| Fenrir | Boiling Blood, Frost Body, Titan Arms |
| Freyja | Thorn Body |
| Hel | Celestial Body, Child of Darkness, Cursed Hands, Fox Legs, Phantom Shroud, Soul Reaper |
| Hraesvelgr | Eagle Agility, Eagle Endurance, Eagle Precision, Eagle Sense, Glide, Wind Aura |
| Kvasir | Bloody Archer, Corruption, Piercing Instincts, Regenerative Body, Thirsty |
| Njord | Aquatic Body, Raider, Water Shield |
| Surtr | Cold Blood, Flame Body |
| Thor | Static Body |
| Ullr | Hunter, Lumberjack, Sneaky, Wolf Fur |

The 10 `Infused…` attributes are covered on the Items pages (Infusion Items, Permanent Consumables),
not as attribute pages. Attribute themes (Titan Arms `FROST`; Titan Legs `BLUE`/`BROWN`) are documented within the
attribute's section.
