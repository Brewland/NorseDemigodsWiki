# Progression

The Demigod skill (level 0 to 100) measures your demigod's power. It rises as you fight, raises your energy and
the strength of your abilities and attributes, and is capped until you obtain each boss's trophy.

<!-- IMAGE: the Demigod skill in the skills menu -->

## How it works

- **Demigod** appears in Valheim's skills menu like any other skill. It gains experience and levels up the
  same way.
- Each demigod gains experience differently, mostly from combat: dealing damage, blocking or taking hits. Each
  demigod page lists its sources under "Demigod skill experience": [Brokkr](../demigods/brokkr.md#demigod-skill-experience),
  [Eir](../demigods/eir.md#demigod-skill-experience), [Fenrir](../demigods/fenrir.md#demigod-skill-experience),
  [Freyja](../demigods/freyja.md#demigod-skill-experience), [Hel](../demigods/hel.md#demigod-skill-experience),
  [Hraesvelgr](../demigods/hraesvelgr.md#demigod-skill-experience), [Kvasir](../demigods/kvasir.md#demigod-skill-experience),
  [Njord](../demigods/njord.md#demigod-skill-experience), [Surtr](../demigods/surtr.md#demigod-skill-experience),
  [Thor](../demigods/thor.md#demigod-skill-experience), [Ullr](../demigods/ullr.md#demigod-skill-experience).
- The energy meter shows your level. Turn on `[User Interface] Show Current Experience` to also see your progress
  toward the next level, as a percentage.

## What the level does

- **Energy:** 1 more maximum energy every 10 levels. See [Energy](energy.md#maximum-energy).
- **Abilities and attributes:** most damage, healing and other values grow
  [per level](../reference/glossary.md#per-level). Their pages show the values at levels 0, 50 and 100.

## Experience needed

Each level needs more experience than the last (vanilla Valheim rules). The experience values on the demigod pages
use these same points.

| Level | Experience for this level | Total from level 0 |
| ---: | ---: | ---: |
| 1 | 1 | 1 |
| 10 | 16 | 76 |
| 25 | 63 | 669 |
| 40 | 127 | 2,107 |
| 55 | 204 | 4,617 |
| 70 | 293 | 8,381 |
| 85 | 392 | 13,561 |
| 100 | 501 | 20,301 |

- Valheim's skill gain world modifier also changes how fast the Demigod skill rises.

## Skill cap

Your demigod skill stops rising at a cap, set by the strongest boss whose trophy you have obtained.

| Highest boss trophy you have | Skill cap |
| --- | ---: |
| None | 10 |
| Eikthyr | 25 |
| The Elder | 40 |
| Bonemass | 55 |
| Moder | 70 |
| Yagluth | 85 |
| The Queen | None (100) |

- **Killing the boss is not enough:** its trophy (head) must be in your trophy list. You get it by picking the
  trophy up; it stays in the list even if you drop or use the trophy afterwards.
- Only the strongest trophy counts: if you have Moder's trophy, the cap is 70 even without Bonemass's.
- While capped, you gain no experience at all. In-game message when you reach the cap: *"Your demigod's skill is
  now capped until you have obtained the head of the next boss!"*
- **Tip:** in multiplayer, each player needs the trophy in their own list. Pass the head around so everyone picks
  it up.

## Losing levels

| When | What you lose |
| --- | --- |
| You die | Nothing: the Demigod skill is protected from Valheim's skill loss on death |
| You die, with skill loss on death turned on | 5 levels, and your progress toward the next level |
| You switch demigods with the [Demigod Runestone](../items/demigod-runestone.md#switching-demigods) | 5 levels, and your progress toward the next level |
| You use the `RevokeDemigod` command (see [First Steps](first-steps.md#changing-your-mind)) | Everything: back to level 0 |

You never drop below level 0.

## Default values

| Setting | Default | Config |
| --- | --- | --- |
| Experience gained | 100% | `[Skills] Skill Demigod Experience Modifier (%)` |
| Skill cap on | Yes | `[Skills] Enable Skill Demigod Cap` |
| Cap per boss | See [Skill cap](#skill-cap) (`0` removes that cap) | `[Skills] Skill Demigod Cap None`, `… Eikthyr`, `… The Elder`, `… Bonemass`, `… Moder`, `… Yagluth`, `… The Queen` |
| Skill loss on death | Off | `[Skills] Enable Skill Loss On Death` |
| Levels lost on death (if on) | 5 | `[Skills] Levels Lost On Death` |
| Levels lost when switching demigods | 5 | `[Skills] Levels Lost When Switching Demigod` |

## Related pages

- [Energy](energy.md)
- [Demigods](../demigods/index.md)
- [Compatibility](compatibility.md#built-in-support) (PathOfValheiman's skill freeze)

<!-- Verified against NorseDemigods 1.9.3 -->
