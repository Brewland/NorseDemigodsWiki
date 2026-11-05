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
- **Tooltips may leave details out** (e.g. Corruption does not list every item it copies; stamina regeneration
  tooltips do not mention "encumbered"). The wiki still documents the full behavior from the code. Ask for a
  tooltip fix only when the tooltip is wrong, not when it is merely shorter.
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

- **Hraesvelgr is fully released** (since 1.9.0). He does not need `Enable Experimental Features`. Do not label him
  "If enabled" or experimental.
- **Holy Sun burning tar** works only with `[(General)] Enable Experimental Features` = `true`, and does not work
  in multiplayer yet. Mention it on the Holy Sun page with an "If enabled" label.
- **Controllers are never mentioned.** Gamepad bindings are commented out in the code. Do not write about
  controllers at all, not even to say they are unsupported.
- **Changelog** (`reference/changelog.md`) links to the mod's release notes in the Changelog tab of the mod page
  (the mod's `CHANGELOG.md`; Thunderstore · Hexium) and names the mod version the wiki describes. Do not copy or
  summarize the release notes: no per-version lines.
- **Images:** add an image placeholder on every page now (see templates); screenshots come later.
  Icons and models live in the Unity bundle and cannot be extracted from the source scan.
- **Server-defaults disclaimer:** the sentence "Values shown are server defaults; your server may differ." appears
  **once**, as a normal paragraph in the body of the home page (`docs/index.md`). No site-wide banner, and do not
  repeat it on other pages.
- **No unarmed note for attack-speed bonuses.** Do not state whether weapon attack-speed bonuses apply to
  unarmed attacks unless the mod code handles unarmed explicitly.
- **Demigod Role** is the README's "Brief Description", kept in full, even when part of it is flavor text (e.g. Eir's
  "bringing light to even the depths of the underworld"). Do not trim it to match the mechanics.
- **Movement speed bonuses** ("+X% movement speed") apply to walking, jogging, sprinting, sneaking and swimming,
  never while encumbered, and do not change jump height. They add up with each other and are scaled by
  `[(Special Modifiers)] Special Movement Speed Modifier (%)`. Write the row as `| Movement speed | +10% |` and add
  the movement speed standard note (see [Standard notes](#standard-notes)). Exception: Wind Aura is removed while
  swimming, so its bonus never applies in water; say so on its page.
- **Sneak and swim speed** (since 1.9.1) are separate percentage bonuses, not part of movement speed:
  - Sneak speed (`Bonus Sneak Speed (%)`): only while sneaking, never while encumbered; sneaking is never faster
    than jogging (armor penalties included).
  - Swim speed (`Bonus Swim Speed (%)`): only while swimming, also while encumbered.
  - Bonuses of the same kind do not stack (the highest applies). Both multiply with movement speed bonuses.
  - Both are scaled by `[(Special Modifiers)] Special Movement Speed Modifier (%)` (since 1.9.1). Add the bullet
    "Scaled by `[(Special Modifiers)] Special Movement Speed Modifier (%)`." after the "Does not stack" bullet.
- **Sneak stamina** (`Stamina Drain Modifier From Sneaking (%)`): reductions from different attributes add up,
  like the sprinting ones.
- **Sprinting:** call the sprint key's effects "sprinting" everywhere, never "running" or "jogging" (e.g. "No
  stamina regeneration while sprinting, swimming or encumbered"). The vanilla skill keeps its name, Run.
- **Minor conditions may be left out** (e.g. regeneration pausing while burning or poisoned), unless leaving them
  out would mislead players. They must be stated when a nearby line implies the opposite, such as "also while
  sprinting or swimming".
- **Sneak attacks** (vanilla backstab: target not alerted, at most once per target every 300 s), since 1.9.1:
  - Only Lightning Torpedo and Poison Javelin have their own ×4 bonus; they get the ×4 standard note.
  - Acid Bolt, Fireball, Ice Shards and Lightning Bolt reuse a cloned vanilla weapon attack, and Infused Arrow's
    arrow uses the bow's attack. They get that attack's vanilla sneak bonus. Many fire without a weapon equipped,
    so never call it "your weapon's" bonus. Do not mention sneak attacks on them at all.
  - Every other ability, including its weapon swing, and all attribute splash damage get no sneak bonus. Add no
    sneak note to them, and make no sneak claims about summons.
- **Bosses are never staggered** by the mod's staggers (abilities and attributes). Add the boss standard note to
  every stagger effect.
- **Player buildings:** Titan Legs' landing blast is the only effect that skips pieces built by players; its page says
  so. Do not mention buildings for any other ability or attribute, even when its area damage hits destructible objects.
- **Weapon swings of special attacks:** state the swing's damage only when the ability sets it (Slash, Blood Slash,
  Cleave: 50%; Stagger: 70%, configurable; Whirlwind and Holy Strike: none, and no stamina). Crush, Soar and
  Combustion leave the weapon's own special-attack damage unchanged; say nothing about their swing damage.

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

- Keys first, then the input's name in brackets **on the next line**, with `<br>` between them:
  `++mouse-side-up++<br>(Ability A)`. This applies everywhere inputs appear: infoboxes, index tables and cards.
  The keys of one input never split across lines (CSS keeps key groups on one line).
- One input per cell (in tables) or per paragraph (in cards).
- Combine keys with ` + ` between key groups: `++mouse-side-up++ + ++block++`.

| YAML input | Write on pages as | Renders as |
| --- | --- | --- |
| `SLOT_1` | `++mouse-side-up++<br>(Ability A)` | Upper Side Mouse (Ability A) |
| `SLOT_2` | `++mouse-side-down++<br>(Ability B)` | Lower Side Mouse (Ability B) |
| `SLOT_3` | `++mouse-side-up++ + ++block++<br>(Ability C)` | Upper Side Mouse + Block (Ability C) |
| `SLOT_4` | `++mouse-side-down++ + ++block++<br>(Ability D)` | Lower Side Mouse + Block (Ability D) |
| `SPECIAL_ATTACK` | `++mouse-middle++<br>(Special attack, clubs or axes)` | Middle Mouse (…), list the weapon types from `skills:` |
| `SPECIAL_ATTACK_BLOCKING` | `++block++ + ++mouse-middle++<br>(Special attack while blocking, …)` | Block + Middle Mouse (…) |
| `SPECIAL_ATTACK_AIR` | `++mouse-middle++<br>(Special attack while airborne)` | Middle Mouse (…) |
| Teleport | `++p++<br>(Teleport)` | P (Teleport) |
| Ignore special attack | `++left-alt++ + ++mouse-middle++` | Left Alt + Middle Mouse |

When a shared special attack uses different weapons per demigod, the ability page (infobox and index row) lists
each: `++mouse-middle++<br>(Special attack, unarmed for Fenrir; axes or swords for Surtr)`. A demigod's own card shows only
that demigod's weapons: `++mouse-middle++<br>(Special attack, unarmed)`.

Where the defaults come from:

- **Ability A / B / Teleport / Ignore special attack:** `[(Hotkeys)]` in `Configs.cs` (`Mouse4`, `Mouse3`, `P`,
  `LeftAlt`). Unity numbers mouse buttons from 0 (`Mouse0` = left), so the config's `Mouse4` is the 5th button
  and `Mouse3` the 4th. Never write "Mouse 4" or "Mouse 5" on pages; players know them as the side buttons:
  - Picture the mouse from above, as a flat 2D image with its front (the main buttons) at the top.
  - `++mouse-side-up++` (**Upper Side Mouse**, config `Mouse4`, Ability A): the side button higher up in that view,
    nearer the front of the mouse (the README's "front side mouse button").
  - `++mouse-side-down++` (**Lower Side Mouse**, config `Mouse3`, Ability B): the side button lower down in that
    view, nearer the back.
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
  | Several types, table cell | `**5**<br><span class="nd-split">2.5 *Blunt*{.dmg .blunt} + 2.5 *Fire*{.dmg .fire}</span>` | **5**, then a smaller grey line: 2.5 [Blunt] + 2.5 [Fire] |
  | Several types, prose | `**5** (2.5 *Blunt*{.dmg .blunt} + 2.5 *Fire*{.dmg .fire})` | **5** (2.5 [Blunt] + 2.5 [Fire]) |
  | Weapon-relative | `**100%** of weapon damage (75% *Slash*{.dmg .slash} + 25% *Fire*{.dmg .fire})` | |

  The **in-game total** (what the tooltip shows) is the main value: bold, on its own line in tables (the CSS makes
  it larger). The split comes second: not bold, on a second line in the `nd-split` span (smaller, grey), so the
  badges never outweigh the total. Example: Fireball's config is 2.5 per type, but the tooltip shows 5.
- Damage is a base amount plus an amount [per level](reference/glossary.md#per-level). Put scaling
  values in a **level table** with the columns `Lv 0 / Lv 50 / Lv 100` (demigod skill level), one row per value.
  Right-align the level columns. When a row has a single damage type, put the badge in the **row label** and
  only bold numbers in the cells:

  ```markdown
  | | Lv 0 | Lv 50 | Lv 100 |
  | --- | ---: | ---: | ---: |
  | Damage *Lightning*{.dmg .lightning} | **10** | **80** | **150** |
  | Range | 12 m | 15 m | 18 m |
  ```

  Mixed-type rows keep the badges in each cell's `nd-split` line. Non-damage values (range, carry weight) are not bold.
  Variant rows name the demigod before the badge: `| Path damage, Thor *Lightning*{.dmg .lightning} | **10** | … |`.
- Values that also scale with another skill (e.g. Titan Arms: demigod skill **and** Unarmed skill) keep the
  `Lv 0 / Lv 50 / Lv 100` columns (demigod level) and get one row per level of the other skill:
  `| Damage per hit, Unarmed skill 0 | … |`, `| Damage per hit, Unarmed skill 100 | … |`.
- Values that depend **only** on another skill get their own columns, named after that skill:
  `| | Unarmed 0 | Unarmed 50 | Unarmed 100 |` (e.g. Titan Arms tree damage).
- A column that holds one damage type may carry the badge in its **header**:
  `| Weapon | Extra damage *Lightning*{.dmg .lightning} |` (see Static Body).
- Tables that compare several sources with different damage types (the Companions page) put the types in their own
  `Damage types` column, as shares with badges, one share per line (`75% *Blunt*{.dmg .blunt}<br>25% *Pierce*{.dmg .pierce}`, or just
  the badge for one type), and keep only the bold totals in the level columns.
- **Bold** marks damage and healing amounts only, including a damage share in prose ("deal **35%** of the hit's
  damage as *Lightning*{.dmg .lightning}"). Percentage bonuses in effect tables (`+10%`) are not bold.
- State the formula in one short line above the table: "10 base + 1.4 per level".
- Mark time-based values clearly: "per second", "every X seconds".
- Values are before enemy armor, resistances and weaknesses. Round the way the in-game tooltip does
  (most tooltips show whole numbers); if unsure, give one decimal and add `TODO: verify`.
- Healing follows the same rules (bold numbers, level table, caps stated explicitly), without a badge.
- Resistances and weaknesses: badge, then the level in plain text: `*Lightning*{.dmg .lightning} Very resistant`.
- **True damage** (untyped damage, e.g. Acid Bolt, Decay Aura) has no badge. Write "true damage" in plain text and link
  the first use to the glossary. In level tables, use the row label `True damage` with bold numbers. When an ability
  adds typed damage on top (Acid Bolt's extra Poison), give it its own row, as the in-game status shows the two values
  separately: `| Extra damage *Poison*{.dmg .poison} | **1** | **8** | **15** |`.

### Numbers and units

- Units after a space, abbreviated in infoboxes and tables: `3 s`, `12 m`, `+20%`. In prose, "seconds" is fine.
- Ranges with an en dash and no spaces: `12–18 m`, `7.5–12.5`. Negative changes with a real minus sign:
  `−40%`. Multipliers with `×`: `×3 (300%)`.
- Changes as before → after: `Eitr cost: 40 → 30`.
- "None" for a cost or cooldown that is zero (`**Cooldown** | None`).
- Minimum resource needs as `Needs 1+ energy; drains 1 every 4 s`.
- In-game messages in italics with quotes: `In-game message when it gets hungry again: *"Your wolf is no longer
  happy"*`. Quote one only when it tells the player something the page does not already say (e.g. a
  notification). Never quote the message that only repeats a stated limit ("Not usable indoors" needs no
  *"The sun will not shine underground..."*).

### Writing style

- **Short bullet lists over long sentences.** One fact per bullet.
- **No paragraph longer than 3 lines** (about 3 × 100 characters as rendered). Split or convert to bullets.
- Numbered lists only for sequences (what happens, in order).
- Tables for anything with two or more comparable values.

### Table orientation

A table that lists a series of more than 6 values (e.g. maximum energy every 10 levels, experience per level) is
**vertical**: one row per step, the step in the first column (`| Demigod skill level | Maximum energy |`). Short
series of up to 6 values may stay horizontal (e.g. Infused Leather Scraps per item consumed). Level tables
(`Lv 0 / Lv 50 / Lv 100`) keep their horizontal form.

### Line breaks

Rendered width must never decide where a line breaks. Where a cell or line holds several items, break it
explicitly with `<br>`:

| Case | Write | Not |
| --- | --- | --- |
| Input (table cell or card) | `++p++<br>(Teleport)` | `++p++ (Teleport)` |
| Cell that lists badges (Element, demigod infobox and index) | `*Spirit*{.dmg .spirit}<br>*Fire*{.dmg .fire}` | `*Spirit*{.dmg .spirit} *Fire*{.dmg .fire}` |
| Favorite weapons and preferred armor (demigod infobox and index) | `Axes<br>Clubs<br>Crossbows`, `Heavy<br>Light` (one per line, each capitalized) | `Axes, clubs, crossbows`, `Heavy and light` |
| Cell that lists damage shares (Companions `Damage types`) | `75% *Pierce*{.dmg .pierce}<br>25% *Poison*{.dmg .poison}` | `75% … + 25% …` |
| Text that introduces a link | `Mod page:<br>` then the link on the next source line | Text and link on one line, or a blank line between |

Badges inside a row label or a sentence (`| *Blunt*{.dmg .blunt} *Slash*{.dmg .slash} resistance |`) stay inline.
A damage breakdown in an `nd-split` line stays on one line (`2.5 *Blunt*{.dmg .blunt} + 2.5 *Fire*{.dmg .fire}`).

### Standard notes

Reuse these exact wordings in `## Notes` (or the `**Notes:**` label) wherever they apply:

| When | Note (copy the wording) |
| --- | --- |
| The ability damages trees, rocks or ores in an area | **Collateral protection:** trees and ores are not damaged when an enemy is within 10 m of the explosion (or beam), or when an enemy within 6 m of you is targeting you. Setting: `[(General)] Protect Resources From Collateral Damage` (on by default; outdoors only). |
| The ability's hit has its own ×4 sneak bonus (since 1.9.1 only Lightning Torpedo and Poison Javelin) | Sneak attacks deal ×4 damage. |
| The ability summons a companion | Bosses deal only 50% damage to summoned companions. Setting: `[Combat] Follower Damage From Boss Modifier (%)`. |
| An energy-on-hit or energy-on-block chance that is blocked by draining abilities | No energy regeneration while an energy-draining ability is active. |
| A "+X% movement speed" bonus | **Movement speed:** applies to walking, jogging, sprinting, sneaking and swimming, but not while encumbered, and does not change jump height. Adds up with other movement speed bonuses. Setting: `[(Special Modifiers)] Special Movement Speed Modifier (%)`. |
| A stagger effect | Bosses are not staggered. |
| Area damage that also hits destructible objects (not limited to trees and ores) | It also hits destructible objects in the area. Add the collateral limit when the code checks it: "Objects are not hit while an enemy is within 10 m, or an enemy within 6 m of you is targeting you. Setting: `[(General)] Protect Resources From Collateral Damage` (on by default; outdoors only)." |
| A special attack whose weapon swing still deals damage (the ability sets a damage multiplier on the swing) | Your weapon also swings, hitting with **50%** of its normal damage. The swing costs no stamina. (Use the code's percentage.) |

### Standard limits

State whether an ability works while airborne or swimming (`Helper.IsPlayerBusy`'s `ignoreFlying` and
`ignoreSwimming`) with these exact wordings:

| When | Wording (copy it) |
| --- | --- |
| Works in both cases | Usable while airborne or swimming. |
| Works in neither case | Not usable while airborne or swimming. |
| Only one case is worth stating | Usable while airborne. / Not usable while swimming. |
| Needs to be airborne (e.g. Crush) | Only while airborne. Extra conditions go in the same bullet. |

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

Kvasir's infusion is a kill, not a recipe. Use the title "Infusion condition (spoiler)" and put the condition in
bullets inside the box:

```markdown
??? spoiler "Infusion condition (spoiler)"

    Kill **Brenna**, the fire skeleton that guards one of Hildir's chests (vanilla).

    - Kvasir must land the killing blow, or be within 50 m of Brenna when it dies.
```

Recipes **and crafting stations** of infusion items, permanent consumables and Infused Megingjord are spoilers:
they appear only inside the spoiler box, never in an overview table or an infobox. The box starts with
"Craft it at a Forge (level 7+)." (on demigod pages: "Craft an **Infused Hammer** at a Forge (level 7+) and consume
it."), then any extra bullets, then the recipe table. Title: "Infusion recipe (spoiler)" for infusion items,
"Recipe (spoiler)" for the others. A `TODO: verify` about recipe materials goes inside the box too.

Food and Runestone recipes are not spoilers.

### Off-by-default features

Anything disabled by default is labelled **"If enabled"** and names the setting. Off-by-default features
(extra merchant items, the Queen Bee spawn chance, boss/merchant map pins, ward protection, and so on)
are documented on the **Optional Features** page (`getting-started/optional-features.md`).

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

The page lives in Getting Started (`getting-started/compatibility.md`), with three tables: `## Known problems`
(Mod, Severity, Problem, Source; severity copied from the README), `## Built-in support` (Mod, What Norse
Demigods does, Source; no links) and `## Bridge mods` (Mod, Author, For players of, What it does, Links; no
Source label), then `## If something breaks`. All five known problems are User-reported (the author confirmed
this). Old compatibility claims from past release notes that the current code no longer shows (Auga, Harpoon
Melee Attack And Upgrading, the Therzie damage-modifier workaround) are left out. EpicLootRaritySets is not listed anywhere in the wiki (it turns off
the demigod system).

### Getting Started pages

Getting Started is a linear reading path for new players, split into two `nav` groups. Setup (outside the game) is
always kept separate from Playing (in the game). `nav` and the index follow this order:

- **Setup:** Installing the Mod, Recommended Mods, Compatibility, Difficulty, Optional Features.
- **Playing:** How the Mod Works, Controls and Hotkeys, Progression, Energy, First Steps.

There is no Ability Infusion page: Infusion Items and each demigod's `## Infusion` section cover it, and How the Mod
Works links to Infusion Items.

All use the System template.

- **Each fact lives on one page.** There is no General Tips page: a tip goes on the page that owns its topic (e.g.
  the trophy needed to raise the skill cap in How the Mod Works, a new character in First Steps), as a bullet or
  paragraph starting with **Tip:** or **Good to know:**. Other pages link to it instead of repeating it.
- **Difficulty** (`difficulty.md`): the summary's second sentence (final damage keeps shields and armor useful) is
  bold. Presets table columns: Difficulty, Base damage, `Final damage<br>(enemies)`, `Final damage<br>(bosses)`.
  Then why final damage keeps shields and armor useful (vanilla block and armor formulas, with a worked example), and the other
  `[(Difficulty)]` settings. Expert is the recommended difficulty (README).
- **Optional Features** (`optional-features.md`): every server feature that is optional, on or off by default, in
  two tables (Feature, Default, What it does, Setting): "Easier materials" (Harpoon fishing first, then pins,
  Haldor's items, queen bees, beehives, feathers) and "Other features" (Experimental features first; Skill loss on
  death before Disabled demigods). Each setting is documented once: feather drops live here, the
  other `[(Difficulty)]` settings on Difficulty.
- **Energy** (`energy.md`): maximum energy per 10 levels and its bonuses, regeneration (spending restarts the
  countdown), the draining abilities table, and a "Getting energy back" table (Source, Demigods, When, Blocked
  while draining). The exact chances and amounts stay on each ability or attribute page; the Energy page only names
  the trigger. Add a row when an ability or attribute gains an energy source.
- **Progression** (`progression.md`, about the demigod skill): links to each demigod's
  `#demigod-skill-experience` section instead of repeating the sources; experience per level (vanilla formula
  `(level)^1.5 × 0.5 + 0.5`, totals rounded); the skill cap per boss trophy; losing levels; settings.
- **How the Mod Works** keeps only a short paragraph on energy and the demigod skill, then links to these pages.
- **Video guide:** the setup video (<https://www.youtube.com/watch?v=uaGUaIzbVR8>) is on Installing the Mod: one
  sentence ending in `:<br>`, the link on the next line (see [Line breaks](#line-breaks)), then a warning
  admonition that it is from early access and outdated.

- **No "Becoming a Demigod" page.** The Demigod Runestone item page covers choosing and switching; First Steps covers
  the first session, the compendium and revoking (`RevokeDemigod`), and links to the Runestone page.
- **How the Mod Works** is an overview: one short `##` section per system, few numbers, a link to the full page.
  Do not repeat tables that belong to another page (e.g. the skill cap per boss).
- **File paths are allowed** on install and settings pages when players need them: `BepInEx/plugins`,
  `BepInEx/config/NorseDemigods.cfg`, `NorseDemigods.dll`, `Demigods.yaml`, `Consumables.json`.
- **Links to mods**, this one included, give the Thunderstore page and, when one exists, the Hexium page, written
  `[Thunderstore](…) · [Hexium](…)`. In tables they go in a `Links` column. Exception: the Built-in support table on
  Compatibility has no links.
  - Thunderstore: `https://thunderstore.io/c/valheim/p/<Namespace>/<Name>/`, checked against the Thunderstore API.
  - Hexium: `https://valheim.hexium.gg/mods/<Namespace>/<Name>`, checked to load (a missing mod returns 404).
  - Mods without a verified page are named in plain text.
- **Recommended Mods** lists only NorseDemigodsUI and shudnal's ConfigurationManager: a plain table (Mod, Author,
  What it adds, Links), then one `##` section per mod. Weapon mods and other suggestions are not listed.
- **Bridge mods** (third-party mods that connect Norse Demigods to another mod, such as NorseDemigodsPovBridge for
  PathOfValheiman) go on Compatibility, not Recommended Mods: they are only useful together with that other mod.
  Describe them from their own page and say they are not made or tested by the Norse Demigods author.
- **Compendium page names** are written in bold as they appear in-game: **ND: Introduction**, **ND: Abilities**.
- **Console commands** (`RevokeDemigod`): say that the console opens with ++f5++ only when the game is started with
  `-console` (vanilla). Cheat commands are not documented in Getting Started: they live on Help › Console Commands.

### Help pages

The Help section (`docs/help/`) holds the pages players open when they are stuck. `nav` order: FAQ, Troubleshooting,
Console Commands. All use the System template.

- **FAQ** (`faq.md`): questions players really ask (from the Discord), grouped under topic `##` headings (Getting
  started, Controls, Progression and infusion, Abilities and combat, Companions, Servers and settings,
  Troubleshooting). Each question is its own `###` heading, so it shows in the page's table of contents, the search
  finds it and it can be linked directly.
  - Each question and its answer sit in one box: `<div class="nd-faq" markdown>`, blank line, the `###` question,
    the answer, blank line, `</div>`. The question shows as a tinted header bar with an accent "Q"; the boxes
    separate one question from the next. Not a table: answers often hold bullets or a small table.
  - Answers are short (1–3 sentences or a few bullets) and link to the page that owns the topic.
  - **No duplicated details:** do not repeat numbers (damage, levels lost, chances, ranges) that live on another page;
    say what happens and link there. Setting names are fine. This keeps the FAQ stable when values change.
  - **Spoilers:** never name an infusion recipe, material, crafting station or Kvasir's enemy. Say what kind of thing
    it is ("Kvasir has no infusion item: he must defeat a specific enemy"), point to the compendium hint and link the
    spoiler box.
  - Leave out opinion questions (which demigod is strongest), questions about other mods by the same author, and
    questions about past bugs.
- **Troubleshooting** (`troubleshooting.md`): a Common problems table (Problem, What to do), how to
  test the mod alone, the log files (`Player.log` and `Player-prev.log` in
  `%USERPROFILE%\AppData\LocalLow\IronGate\Valheim`), and how to report a bug in the Discord **#bugs** forum
  (`https://discord.gg/gSQHmE3yap`; title format "(Norse Demigods) Problem").
- **Console Commands** (`console-commands.md`): how to open the console and turn on cheats (vanilla), a Commands table
  (Command, What it does, Cheat) from `Console/*.cs`, then vanilla commands that act on the mod. `MakeMeSaiyan` is
  excluded (see [Exclusions](#exclusions)). Do not say whether the world's skill modifiers scale
  `GiveDemigodExperience`: it is untested.

### Exclusions

- **Saiyan is excluded.** It is a hidden test class reachable only with an admin command. Do not document it,
  its exclusive abilities (Arcane Bolt, Blink, Sharp Mist), its `ARCANE` themes (Elemental Shield, Restoration,
  Titan Arms), its attributes (Saiyan Body, Saiyan Strength) or the `MakeMeSaiyan` console command.

### Linking

- Use relative links to `.md` files so `mkdocs build --strict` can check them:
  `[Surtr](../demigods/surtr.md)`.
- Link the **first** use of a glossary term on each page. On grouped item pages, link it in **each item section**
  that uses it, since each section is read on its own (e.g. "tool tier" in both Earthbreaker cards):

  | Term | Link target | Meaning (verify against the code) |
  | --- | --- | --- |
  | heavy armor | `reference/glossary.md#heavy-armor` | Any armor piece with a movement penalty of 5% or more |
  | per level | `reference/glossary.md#per-level` | Per demigod skill level (0–100) |
  | specialized weapons | `reference/glossary.md#specialized-weapons` | The weapon types an attribute's bonus applies to |
  | tool tier | `reference/glossary.md#tool-tier` | Which trees and ores an ability or attribute can damage |
  | true damage | `reference/glossary.md#true-damage` | Damage without a type: armor, resistances and weaknesses do not change it (vanilla) |

  The glossary lives in Reference (`docs/reference/glossary.md`), not Getting Started.

- Every new page must be added to `nav` in `mkdocs.yml`, under its section, after that section's `index.md`.
  Order within a section:
  - **Getting Started:** reading order (see [Getting Started pages](#getting-started-pages)), not alphabetical.
  - **Demigods:** alphabetical.
  - **Abilities:** Teleport first, then alphabetical.
  - **Attributes:** alphabetical.
  - **Items:** Demigod Runestone first, then alphabetical.
  - **Help:** FAQ, Troubleshooting, Console Commands.
  - **Reference:** Glossary, Changelog.
- Every new page also gets a row in its section's `index.md` table (see [Section index pages](#section-index-pages)).

### File naming

- `lowercase-kebab-case.md`, from the English display name: `docs/abilities/stone-golem.md`.
- Abilities shared by several demigods or with theme variants (Slash, Crush, Dash, Elemental Shield,
  Heal Over Time, Restoration, Stagger, Summon Wolf) get **one page with a section per variant**:
  `docs/abilities/slash.md` with `### Fire (Surtr)` and `### Frost (Fenrir)` under `## Variants`.
  Variants share one config section, so a server change affects all of them; say so on the page.
- If **all** owners use the same theme (e.g. Stagger: Eir and Freyja, both `BROWN`), skip `## Variants`: say in the
  summary that they share the same version, and cards link to the page itself, not a section.
- If variants share a theme but differ in another property, name the section after that difference. Example: Summon
  Wolf (both `FROST`) uses the creature: `### Ulv (Fenrir)`, `### Wolf (Ullr)`.
- **One page per attribute**, whether one demigod or several have it: `docs/attributes/static-body.md`,
  `docs/attributes/hare-legs.md`. Never group attributes on a shared page (no "Movement and Stamina" or "Strength"
  pages), even when their content is similar. The same goes for abilities: one page per ability (theme variants of
  the same ability stay as sections on that page, see above).
- **Items are the exception:** related items stay grouped on one page, one `##` section each. Keep the groups
  separate by who can use them:
  - **Infusion Items** (`infusion-items.md`): the items that infuse a demigod's abilities, one per demigod.
  - **Permanent Consumables** (`permanent-consumables.md`): items any demigod can consume for a permanent effect.
  - **Sweet Fish Foods** (`sweet-fish-foods.md`).
  - Standalone items (Demigod Runestone, Infused Megingjord, Abyssal Harpoon) get their own page.

### Images

The home page has no images. On every other page, until screenshots exist, add an image placeholder as an HTML comment right after the infobox:

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
| **Input** | ++mouse-side-up++<br>(Ability A) |
| **Energy cost** | 1 |
| **Cooldown** | 3 s |
| **Config ID** | `Dash` |
| **Config section** | `[Ability Dash]` |

</div>
```

Field order (omit rows that do not apply, except where marked "always"):

| Page type | Fields, in order |
| --- | --- |
| Demigod | Role, Element (badges), Favorite weapons, Preferred armor, Config ID, Config section |
| Ability | Used by, Input, Eitr cost (only if any), Energy cost (always), Cooldown (always), Duration or Cast time, Range, other areas (e.g. Explosion radius), Config ID, Config section |
| Attribute | Demigod (one owner) or Demigods (several owners), Condition, Config ID, Config section |
| Item | Type, Effect (or food stats: Health, Stamina, Eitr, Healing, Duration), Crafting station, Recipe, Restricted to, Stack size, Consume limit, Config ID, Config section |

- Values that scale with level appear as a range: `12–18 m, by level`; the level table has the details.
- Item infoboxes show **Crafting station** and **Recipe** only when the recipe is not a spoiler (foods, Runestone).
  The Recipe row lists one material per line, amount first: `2 Raw fish<br>2 Honey`. **Effect** is a short
  summary; several effects go on separate lines with `<br>`.
- Channeled abilities add ", hold" after the input: `++mouse-side-down++ + ++block++<br>(Ability D), hold`.
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

    ++mouse-side-up++<br>(Ability A)

    Teleport forward, damaging enemies in your path.

</div>
```

Card order:

- **Abilities:** by input: special attacks (normal, while blocking, airborne), Ability A, B, C, D, then Teleport.
- **Attributes:** the demigod's own attributes (no other owner) first, then shared attributes; alphabetical within
  each.

Card text rules:

- Toggles start with "Toggle: ", e.g. "Toggle: faster attacks, faster movement and stamina regeneration."
- Teleport's card always reads "Teleport to your bed and back. Shared by all demigods."
- Variant abilities link to the variant section: `../abilities/dash.md#lightning-thor` (unless the page has no
  `## Variants`, see [File naming](#file-naming)).
- Attributes always link to their page: `../attributes/bear-strength.md`.

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
| Lightning Torpedo | `:material-rocket-launch:` |
| Combustion | `:material-rocket:` |
| Bomb | `:material-bomb:` |
| Stone Shield | `:material-wall:` |
| Stone Golem | `:material-robot-angry:` |
| Nano Cube | `:material-cube-outline:` |
| Blacksmith | `:material-hammer:` |
| Gourmand | `:material-food-drumstick:` |
| Sturdy Legs | `:material-foot-print:` |
| Thunder Forger | `:material-anvil:` |
| Titan Strength | `:material-weight-lifter:` |
| Holy Strike | `:material-star-four-points:` |
| Stagger | `:material-rotate-3d-variant:` |
| Holy Sun | `:material-weather-sunny:` |
| Elemental Shield | `:material-shield-sun:` |
| Holy Heal | `:material-hand-heart:` |
| Holy Conjuration | `:material-fish:` |
| Holy Body | `:material-white-balance-sunny:` |
| Purity | `:material-flare:` |
| Deer Endurance | `:material-heart-pulse:` |
| Eagle Strength | `:material-bird:` |
| Hare Legs | `:material-rabbit:` |
| Valkyrie | `:material-shield-sword:` |
| Slash | `:material-slash-forward:` |
| Ice Shards | `:material-snowflake:` |
| Enrage | `:material-emoticon-angry:` |
| Frost Nova | `:material-snowflake-variant:` |
| Summon Wolf | `:material-paw:` |
| Heal Over Time | `:material-heart-plus:` |
| Boiling Blood | `:material-thermometer-high:` |
| Frost Body | `:material-snowman:` |
| Titan Arms | `:material-boxing-glove:` |
| Wolf Speed | `:material-speedometer:` |
| Poison Javelin | `:material-spear:` |
| Poison Cloud | `:material-biohazard:` |
| Nature Wisp | `:material-sprout:` |
| Thorn Body | `:material-cactus:` |
| Acid Bolt | `:material-bottle-tonic-skull:` |
| Meteor | `:material-meteor:` |
| Decay Aura | `:material-skull-crossbones:` |
| Minions | `:material-skull:` |
| Sacrifice | `:material-blood-bag:` |
| Celestial Body | `:material-orbit:` |
| Child of Darkness | `:material-weather-night:` |
| Cursed Hands | `:material-hand-back-right:` |
| Fox Legs | `:material-run:` |
| Phantom Shroud | `:material-ghost:` |
| Soul Reaper | `:material-sickle:` |
| Lightning Bolt | `:material-lightning-bolt-outline:` |
| Crush | `:material-arrow-collapse-down:` |
| Water Sphere | `:material-water:` |
| Tornado | `:material-weather-tornado:` |
| Neck | `:material-snake:` |
| Aquatic Body | `:material-waves:` |
| Raider | `:material-sail-boat:` |
| Water Shield | `:material-shield-half-full:` |
| Fireball | `:material-fire:` |
| Burning Ground | `:material-campfire:` |
| Summon Surtling | `:material-emoticon-devil:` |
| Drain Blood | `:material-heart-minus:` |
| Cold Blood | `:material-thermometer-low:` |
| Flame Body | `:material-fire-circle:` |
| Cleave | `:material-weather-windy:` |
| Whirlwind | `:material-weather-hurricane:` |
| Soar | `:material-airplane-takeoff:` |
| Telekinesis | `:material-magnet:` |
| Vortex | `:material-rotate-orbit:` |
| Energy Wisp | `:material-star-shooting:` |
| Wind Shield | `:material-shield-airplane:` |
| Eagle Agility | `:material-sword:` |
| Eagle Endurance | `:material-lungs:` |
| Eagle Precision | `:material-bullseye-arrow:` |
| Eagle Sense | `:material-compass:` |
| Glide | `:material-feather:` |
| Wind Aura | `:material-weather-windy-variant:` |
| Blood Slash | `:material-knife:` |
| Warp | `:material-transfer-right:` |
| Dark Aura | `:material-shield-moon:` |
| Charm | `:material-account-heart:` |
| Bloody Archer | `:material-bow-arrow:` |
| Corruption | `:material-treasure-chest:` |
| Piercing Instincts | `:material-knife-military:` |
| Regenerative Body | `:material-bandage:` |
| Thirsty | `:material-glass-wine:` |
| Infused Arrow | `:material-arrow-projectile:` |
| Blast | `:material-weather-dust:` |
| Sense Creatures | `:material-radar:` |
| Hunter | `:material-target-account:` |
| Lumberjack | `:material-axe:` |
| Sneaky | `:material-incognito:` |
| Wolf Fur | `:material-dog-side:` |

#### Overview table

Tables that list the entries of a section or page are styled as overview tables: full content width, a bronze
accent line on top, a fjord-blue header row (`--nd-overview-head-bg`), the panel border with rounded corners,
striped rows (`--nd-overview-stripe`), an accent tint on hover and a bold first column. Use it for:

- every section index table (`demigods/`, `abilities/`, `attributes/`, `items/index.md`);
- the `## Overview` table of grouped item pages (Infusion Items, Permanent Consumables, Sweet Fish Foods);
- the `## Overview` table of the Companions page.

Wrap the table in a `div` (blank lines inside it are required). Notes after the table go outside the `div`.

```markdown
<div class="nd-overview" markdown>

| Item | Effect | Consume limit |
| --- | --- | --- |
| [Infused Bloodbag](#infused-bloodbag) | +20 maximum health | Once |

</div>
```

Do not use it for other tables (level tables, effect tables, recipes): those get the plain table style.

#### Plain table

Every other table (level tables, effect tables, recipes, settings tables) gets a light style automatically, with
no wrapper and no class: a thin panel-colored border with rounded corners and a header row tinted with the panel
background. No accent line, stripes or colored header, so it stays lighter than the infobox and the overview table.
The infobox and overview rules are more specific and override it.

#### Section index pages

Each section's `index.md` is a one-line summary plus one entry per page, sorted alphabetically by name, in an
[overview table](#overview-table):

| Index | Columns | Notes |
| --- | --- | --- |
| `demigods/index.md` | Demigod, Summary, Element, Favorite weapons, Preferred armor | Element as badges |
| `abilities/index.md` | Ability, Used by, Input, Summary | Input as keys; ends with "Inputs show the default keys." |
| `attributes/index.md` | Attribute, Demigods, Summary | Every attribute links to its own page |
| `items/index.md` | Page, Summary | One row per page (grouped pages are one row), in `nav` order: Demigod Runestone first, then alphabetical |
| `getting-started/index.md` | No table: `## Setup` and `## Playing` bullet lists, in reading order (Python-Markdown ignores list start numbers, so no numbered lists) | `- [Installing the Mod](installing-the-mod.md): requirements, …` |
| `help/index.md` | No table: a `## Pages` bullet list, in `nav` order | `- [FAQ](faq.md): short answers to …` |
| `reference/index.md` | No table: a `## Pages` bullet list | `- [Glossary](glossary.md): heavy armor, per level, …` |

Demigods without a page yet are plain text (no link) in the Used by / Demigods columns.

#### Home page

`docs/index.md` is short and written to be found by search engines and AI tools. No images, no icons, no infobox.
In this order:

1. `# Norse Demigods Wiki`, then one intro paragraph (max 3 sentences): the mod in the README's own words ("a
   daughter or son of Odin blessed with the powers of the gods"), the number of demigods, each "an RPG-like class
   of its own", and that many echo classic RPG roles (cleric, necromancer, ranger) while each is a figure from Norse
   myth that belongs in Valheim. Never call it "just another RPG mod" or reduce a demigod to a class.
2. One paragraph: the mod version the wiki describes, then the server-defaults disclaimer.
3. `## New to the mod?`: four grid cards, Installing the Mod → How the Mod Works → Controls and Hotkeys → First
   Steps. The hotkeys card says to set up the ability keys first.
4. `## Choose your demigod`: one grid card per demigod, alphabetical. Line 1: the linked name in bold, then its
   element badges. After `---`, one line: a classic-role label in Title Case with `&` for "and" (e.g. "Engineer &
   Smith"; the same labels as the README's "Plays like" column), a colon, then two or three signature abilities or
   traits (max ~10 words), e.g. "Cleric: holy strikes, healing and elemental shields." Each claim must match the
   demigod's ability and attribute pages. Never call a melee demigod a mage (Hraesvelgr is an "Aerial Warrior").
5. `## Explore the wiki`: one grid card per remaining section (Abilities, Attributes, Items, Companions, Help,
   Reference), one line each.
6. `## Download and community`: the Thunderstore · Hexium links and the Discord.

Home cards have no icon; otherwise they follow the [card grid](#card-grid) format. When a demigod is added or its
kit changes, update its home card and the demigod count in the intro.

Search metadata: `site_description` in `mkdocs.yml` is the meta description for every page (keep it under ~160
characters, with "Valheim mod", "demigods" and "classes"). `overrides/main.html` gives only the home page the
`<title>` "Norse Demigods Wiki: Valheim Class Mod Guide"; other pages keep Material's "Page - Norse Demigods Wiki".

#### CSS class reference

| Class | Use on | Markdown example |
| --- | --- | --- |
| `nd-infobox` | `<div>` around the page's top fact table | `<div class="nd-infobox" markdown>` |
| `dmg` + type | Emphasis with `attr_list`, for damage types, elements, resistances | `*Fire*{.dmg .fire}` |
| `grid cards` | `<div>` around a card list (Material built-in). CSS makes the whole card click through to the first link on its first line (the title), so every card must start with its title link | `<div class="grid cards" markdown>` |
| `lg middle` | Card icon size and alignment (Material built-in) | `:material-flash:{ .lg .middle }` |
| `keys` | Generated by `pymdownx.keys`; CSS stops key combinations from wrapping | `++mouse-side-up++ + ++block++` |
| `admonition quote` | Lore box, recolored to the accent color | `!!! quote "Lore"` |
| `nd-overview` | `<div>` around a section index table or a grouped page's `## Overview` table | `<div class="nd-overview" markdown>` |
| (none) | Any other table: plain table style, applied automatically | A normal Markdown table |
| `nd-row-exception` | A link in a table's first cell; tints that whole row with the panel background (CSS `:has()`) | `[Kvasir](../demigods/kvasir.md){ .nd-row-exception }` |
| `nd-faq` | `<div>` around one FAQ question (`###`) and its answer; the question becomes a tinted header bar | `<div class="nd-faq" markdown>` |
| `nd-updated` | The "Updated" date after the site name in the header; set by the template, never written in pages | (none) |

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
| Overview table header / stripe | `#24394d` / `#faf8f4` | `#2c4155` / `rgba(255, 255, 255, 0.025)` |
| Plain table border / header | Panel border / panel background | Panel border / panel background |

The accent color is used for the infobox's left border, the Lore box, the top border and icon of each card, and
card titles on hover. `h2` headings get a thin bottom border.

#### Discord tab

The last `nav` entry is `Discord: https://discord.gg/gSQHmE3yap`, an external link. CSS (selected by
`href*="discord.gg"`) turns its tab into a Discord-blurple (`#5865f2`) rounded button with the Discord logo, and shows
it in blurple with the logo in the mobile menu. Keep it last.

#### Header date, logo and download links

The header shows **Updated** and a date after the site name (for example *Updated 5 Nov 2026*). It is the build date
(`build_date_utc`), and the site is rebuilt on every push to `main`, so it is the date of the last update. It comes
from `overrides/partials/header.html`, a copy of Material's header partial with only that addition; re-copy it
and add the `<time class="nd-updated">` element again if Material is upgraded and changes the partial. Pages never
write the date themselves.

The header icon is `docs/assets/images/logo.png`: a 128 × 128 copy of the mod's white logo ("Norse Demigods White
Only.png"), trimmed to its content and centered on a transparent square. White reads on the header in both light
and dark mode.

The browser tab icon (favicon) is `docs/assets/images/favicon.png`: a 64 × 64 copy of the mod's colored icon
("icon.png"), trimmed and centered on a transparent square. It is colored with dark outlines so it shows on light
and dark tabs. To replace either image, make a new resized copy; never edit the original artwork.

The header also shows the download links **Thunderstore | Hexium**, between the title and the light/dark toggle:
small text in the header color, a faint `|` between them, accent color on hover, hidden below 60em like the repo
link. Keep it to these two short names; no other text in the header. The URLs live in `mkdocs.yml` under
`extra.download` (a list of `name` and `link`), and `overrides/partials/header.html` loops over that list.

#### Required `mkdocs.yml` setup

These settings make the components work; do not remove them:

```yaml
theme:
  name: material
  custom_dir: overrides          # main.html: home page <title> (no banner); partials/header.html: the date
  logo: assets/images/logo.png   # header icon (see Header date, logo and download links)
  favicon: assets/images/favicon.png  # browser tab icon
  palette: # light + dark, both with primary: custom, accent: custom
extra:
  download:                      # header links: Thunderstore, Hexium (name + link)
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

    ++mouse-middle++<br>(Special attack, unarmed)

    One short sentence.

-   … one card per ability, in input order: special attacks, A, B, C, D, Teleport

</div>

## Attributes

<div class="grid cards" markdown>

-   :material-flash:{ .lg .middle } [**Static Body**](../attributes/static-body.md)

    ---

    One short sentence.

-   :material-arm-flex:{ .lg .middle } [**Bear Strength**](../attributes/bear-strength.md)

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
| **Input** | ++mouse-middle++<br>(Special attack, …) |
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

10 base + 1.4 [per level](../reference/glossary.md#per-level).

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

### Attribute

```markdown
# Static Body

One-sentence summary of this attribute.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Demigod** | [Thor](../demigods/thor.md) (several owners: **Demigods**, comma-separated) |
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

### Item

```markdown
# Infused Megingjord

Infused Megingjord is an equippable belt that increases your maximum energy and carry weight.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Type** | Equipment (belt) / Consumable (permanent effect) / Consumable (ability infusion) / Food / Misc (reusable) / Weapon (vanilla item) |
| **Effect** | Short summary (grouped pages; standalone pages use `## Effect`) |
| **Crafting station** | None (craft from your inventory) / Cauldron (level X+) / Unchanged (vanilla recipe); omit if it is a spoiler |
| **Recipe** | `1 Stone<br>1 Resin`; omit if it is a spoiler |
| **Restricted to** | Anyone / Any demigod / [Demigod](../demigods/….md) (omit for foods) |
| **Stack size** | X |
| **Consume limit** | Once / 5 times / Once, after Infused Earthbreaker (consumables only) |
| **Config ID** | `InfusedBeltStrength` |
| **Config section** | `[Enhanced Megingjord]` (omit if the item has none) |

</div>

<!-- IMAGE: Infused Megingjord in the inventory -->

## Effect

- Effect at default settings.

## Recipe

??? spoiler "Recipe (spoiler)"

    Craft it at a Forge (level 7+).

    | Material | Amount |
    | --- | --- |
    | … | … |

## Related pages

- …

<!-- Verified against NorseDemigods x.y.z -->
```

A visible recipe (Runestone) has no `## Recipe` section: it is the infobox's Recipe row, and any recipe setting
goes under `## Getting one`.

Grouped item pages (Infusion Items, Permanent Consumables, Sweet Fish Foods) start with a `## How … work` bullet
list (the shared rules), then a `## Overview` table (an [overview table](#overview-table)), then one `##` section per item. Each section is
**one card**:

1. The infobox, holding everything that fits in a row: Effect (or the food stats), and a visible recipe.
2. The image placeholder.
3. Only if needed, details without a heading: a table when an effect has several values (Infused Chitin per
   weapon, Infused Hard Antlers per item consumed), then bullets.
4. The recipe spoiler box, if the recipe is a spoiler.

Never use `###` subsections or a one-row table inside an item section. The Sweet Fish Foods page notes that only
one sweet fish food can be active at a time.

- **Infusion Items:** item names are public; recipes and crafting stations are spoilers. Overview columns: Demigod,
  Item, sorted by demigod, with Kvasir last as the exception: his row reads
  `| [Kvasir](../demigods/kvasir.md){ .nd-row-exception } | None: [a kill](#kvasir) |`, which gives it a faint
  panel background. The sections follow the table order (Kvasir's `## Kvasir` section last). Each section is the
  infobox, a "What it upgrades: [Thor › Infusion](../demigods/thor.md#infusion)." line and the spoiler (the demigod
  page's recipe table and any extra bullet, e.g. Brokkr's Blacksmith line; Kvasir: the same condition spoiler as
  his page).
- **Permanent Consumables:** overview columns: Item, Effect, Consume limit. Sections are
  alphabetical, except Infused Grand Earthbreaker, which follows Infused Earthbreaker (it is its upgrade). Their
  config section is the attribute's: `[Attribute Infused Bloodbag]` (`MorgenHeart` → `[Attribute Infused Morgen Heart]`).
- **Sweet Fish Foods:** overview columns: Food, Health, Stamina, Eitr, Healing, Duration (no Crafting station: the
  table must fit without a horizontal scroll bar; the station is in each card). Each card
  lists Type, Health, Stamina, Eitr, Healing (`5 per tick`), Duration, Crafting station, Recipe, Stack size,
  Config ID. Food stats are plain numbers (not bold); a note under the overview says a tick is every 10 seconds
  (vanilla). Durations in minutes (`m_foodBurnTime` / 60).
- **Recipe materials** use the vanilla English display names in sentence case, as the demigod pages do: "Hard
  antler", "Raw fish", "Refined eitr" (prefab `Eitr`), "Bronze pickaxe".
- **Vanilla armor sets** are named "<Name> set". When the in-game set has no single name, use the material and the
  set effect: "Bear (Berserker) set" (Headdress, Patterns and Loincloth of the Bear; set effect Berserk). Never
  "Berserkir".
- **Vanilla items the mod changes** (Abyssal Harpoon) use the vanilla prefab as Config ID (`SpearChitin`) and the
  mod's config section for that feature.

### System

Used for Getting Started topics (Progression, Energy, …), Companions, Help and
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

### Companions

`companions/index.md` is a single System page (no infobox) that compares every companion. The ability pages keep the
details; the Companions page only compares and links. Sections, in order:

1. `## Overview`: an [overview table](#overview-table) with the columns Companion, Ability, Demigod, Job, How many,
   Lasts. The companion name is plain text (bold through the overview style, no link); the Ability column links to
   the ability page or its variant section (`[Summon Wolf](../abilities/summon-wolf.md#ulv-fenrir)`,
   `[Minions](../abilities/minions.md#infused), infused`), and the Demigod column to the demigod page. Rows alphabetical by companion.
2. `## How companions work`: the shared rules as bullets, then `### Summon Wolf is different`.
3. `## Damage` and `## Health`: level tables with one row per companion (alphabetical), damage types in a
   `Damage types` column (see [Damage and healing](#damage-and-healing)).
4. `## Energy and regeneration`, `## Distance from you`: plain comparison tables. Write "No" when a rule does not
   apply, "None" for a zero chance.
5. `## Permanent bonuses`, `## Interactions` (links to the abilities and attributes that treat companions
   differently), `## Wisps`, `## Related pages`.

- **Companion names** are the vanilla creature names in sentence case: Stone golem, Surtling, Skeleton, Ghost,
  Deathsquito, Neck, Ulv, Wolf, plus "Charmed creature". Rows that share every value are merged ("Skeleton or ghost").
- **What counts as a companion:** a creature summoned or charmed by an ability. Nature Wisp and Energy Wisp are not
  creatures (enemies cannot attack them); they get a short `## Wisps` section, not rows.
- Every companion ability page lists `[Companions](../companions/index.md)` last in its Related pages.
- Each value on the Companions page must match its ability page. When one changes, update both.
- **Logout:** write "when you teleport, die or log out". Do not mention the 5 s delay after a disconnect
  (logging out through the menu removes companions at once; the difference does not matter to players).
- **Distances** are written "X m or more", even where the code checks "more than X m" (e.g. Charm's 55 m).

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
| Consume checks (demigods only, restriction, limits, sweet fish one at a time) | `NorseDemigods.cs` (`Humanoid_UseItem_Patch`) |
| Where each permanent effect applies | `NorseDemigods.cs` (max health, armor, block armor, eitr, attack speed), `SE_Demigod.cs` (energy, eitr regeneration), `Helper.cs` (damage, healing, summons), `StatusEffects/SE_Minion.cs`, `SE_Wolf.cs` |
| Runestone menu, switching demigods | `CustomUI.cs` (`RunestoneMenu*`), `Demigod.cs` (`RevokeDemigod`) |
| Abyssal Harpoon, raw fish recipe | `NorseDemigods.cs` (`ObjectDB_Awake_Patch`, `ApplyItemCustomChanges`, `Projectile_OnHit_Patch`) |

### System pages

| Topic | Source |
| --- | --- |
| Energy, skill caps, level loss, difficulty presets, teleport | `Configs.cs`, `Helper.cs` |
| Maximum energy, regeneration, drains | `SE_Demigod.cs` (`GetMaxEnergy`, `GetEnergyPassiveRegenerationTimePeriod`, `RemoveEnergy`), `DemigodAbility.cs` (`EnergyDrainPeriod`, `Stop`), callers of `Helper.IsAnyDrainingAbilityActive` |
| Skill experience, cap, death and switching | `SE_Demigod.cs` (`RaiseSkill`, `RaiseSkillPct`), `Helper.IsDemigodSkillCapped`, `NorseDemigods.cs` (`Skills_LowerAllSkills_Patch`), `Demigod.RevokeDemigod`; vanilla `Skills.Skill.Raise` and `GetNextLevelRequirement` |
| Teleport ability | `Abilities/AbilityTeleport.cs`, `StatusEffects/SE_TeleportLocationExpiration.cs` |
| Harpoon fishing, honey, merchant, armor sets | `Configs.cs`, `NorseDemigods.cs` |
| Console commands (for First Steps and the FAQ) | `Console/*.cs` (`IsCheat`), `Demigod.cs` (`RevokeDemigod`) |
| Installing: dependencies, version check, data-file check | `_Publish/manifest.json`, `NorseDemigods.cs` (`NetworkCompatibility`), `DataFileValidation.cs` |
| Settings file, update reset, server-synced vs own settings | `Configs.cs` (`AutomaticallyUpdateConfigs`, `ResetMainSettings`, `IsAdminOnly`) |
| Compendium pages, spawn message, free runestone | `CustomUI.cs` (`UpdateLore`), `NorseDemigods.cs` (`Player_OnSpawned_Patch`), translation keys `lore_*`, `tutorial_*` |
| Interface settings | `CustomUI.cs` (`SetupConfigs`) |
| Difficulty: final damage, base damage | `Helper.cs` (`GetDifficultyDamageModifier`, `GetCreatureDifficultyDamageModifier`), `NorseDemigods.cs` (`Character_ApplyDamage_Patch`, the `SE_Burning` / `SE_Poison` prefixes, `Humanoid_GiveDefaultItems_Patch`); vanilla order in `Character.RPC_Damage`, `Humanoid.BlockAttack`, `HitData.ApplyArmor` |
| Optional features (pins, merchant, honey, feathers, spawns, ammo, ward) | `Configs.cs`, `NorseDemigods.cs` (`Player_OnSpawned_Patch`, the Haldor trader patch, `Beehive_*` patches, `DropOnDestroyed_OnDestroyed_Patch`, `SpawnSystem_Awake_Patch`, `WearNTear_Damage_Patch`) |
| Recommended mods, tips, incompatible mods | `_Publish/README.md` (Enhanced User Interface, General Tips, Setup) |
| Companions: shared rules (distance, boss damage, regeneration, energy on hit, summon bonuses) | `StatusEffects/SE_Minion.cs`, `StatusEffects/SE_Wolf.cs`, `Helper.cs` (`GetSummonDamageModifier`, `GetSummonHealthModifier`), each summon ability's `Execute` |
| Companions: what happens on teleport, death and logout | `DemigodAbility.cs` (`OnPlayerTeleporting`, `OnPlayerDeath`, `OnPlayerDisconnecting`), each ability's `Stop` |
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
│   ├── index.md                            ## Setup and ## Playing lists, reading order
│   │   Setup:
│   ├── installing-the-mod.md               Requirements, mod managers, video, multiplayer, settings file
│   ├── recommended-mods.md                 NorseDemigodsUI, ConfigurationManager (shudnal)
│   ├── compatibility.md                    Known problems, built-in support, bridge mods
│   ├── difficulty.md                       Final vs base damage, presets, other difficulty settings
│   ├── optional-features.md                Easier materials, other features (on or off by default)
│   │   Playing:
│   ├── how-the-mod-works.md                Overview of every system, with tips
│   ├── controls-and-hotkeys.md             Default keys, special attacks, changing keys, interface
│   ├── progression.md                      Demigod skill: experience, skill cap per boss, losing levels
│   ├── energy.md                           Maximum, regeneration, draining abilities, energy sources
│   └── first-steps.md                      Compendium, runestone, first session, revoking
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
│   └── one page per attribute              (table below), e.g. static-body.md, hare-legs.md
├── items/
│   ├── index.md
│   ├── demigod-runestone.md
│   ├── abyssal-harpoon.md                  Abyssal Harpoon & Harpoon Fishing
│   ├── infused-megingjord.md
│   ├── infusion-items.md                   10 item sections + Kvasir, recipes in spoilers
│   ├── permanent-consumables.md            Bloodbag, Chitin, Earthbreaker (+ Grand), Eitr, Hard Antlers,
│   │                                       Leather Scraps, Liquid Frost, Morgenheart, Serpent Scale
│   └── sweet-fish-foods.md                 Overview table + one section per food
├── companions/
│   └── index.md                            One page comparing every companion (see Companions template)
├── help/
│   ├── index.md                            ## Pages list
│   ├── faq.md                              Question headings, short answers, links (see Help pages)
│   ├── troubleshooting.md                  Common problems, testing alone, log files, bug reports
│   └── console-commands.md                 Mod commands, cheats, vanilla commands
└── reference/
    ├── index.md
    ├── glossary.md                         heavy armor, per level, specialized weapons, tool tier, true damage
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

Every attribute gets its own page, named from the display name (`static-body.md`, `hare-legs.md`), listed
alphabetically in `nav`.

Shared attributes (several owners):

| Attribute | Demigods |
| --- | --- |
| Bear Strength | Njord, Surtr, Thor |
| Deer Endurance | Eir, Fenrir, Freyja, Kvasir, Ullr |
| Eagle Strength | Eir, Freyja, Hraesvelgr |
| Hare Legs | Eir, Fenrir, Freyja, Hraesvelgr, Kvasir, Ullr |
| Titan Legs | Njord, Surtr, Thor |
| Valkyrie | Eir, Freyja |
| Wolf Speed | Fenrir, Freyja, Ullr |

Attributes with one owner (38):

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
not as attribute pages. Attribute themes (Titan Arms `FROST`; Titan Legs `BLUE`/`BROWN`) are documented on the
attribute's page.
