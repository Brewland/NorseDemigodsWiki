# Static Body

Static Body is Thor's own attribute: the electricity in his body adds Lightning damage to his weapons, shocks
enemies that hit him and strengthens his heavy armor.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Demigod** | [Thor](../demigods/thor.md) |
| **Condition** | Always active; the armor bonus needs 2+ [heavy armor](../getting-started/glossary.md#heavy-armor) pieces |
| **Config ID** | `StaticBody` |
| **Config section** | `[Attribute Static Body]` |

</div>

<!-- IMAGE: Static Body attribute icon -->

## Weapon damage

Extra damage added to your weapon hits:

| Weapon | Extra damage *Lightning*{.dmg .lightning} |
| --- | ---: |
| Bows and crossbows | +10% |
| Axes | +10% |
| One-handed clubs | +15% |
| Two-handed clubs | +20% |
| Himminafl | +20% |
| Other polearms, spears and swords | +5% |

- Knives and unarmed attacks get no extra damage.
- **Lightning splash:** hits with axes or clubs also deal **35%** of the hit's damage as
  *Lightning*{.dmg .lightning} to other enemies within 2 m.

## Defense

| Effect | Value |
| --- | --- |
| Armor with 2+ heavy armor pieces (helmet, chest, legs) | +10% |
| Chance to stagger an enemy that hits you | 20% |
| *Lightning*{.dmg .lightning} resistance | Very resistant |

When an enemy hits you, it takes *Lightning*{.dmg .lightning} damage back.
0.25 [per level](../getting-started/glossary.md#per-level):

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Reflected damage *Lightning*{.dmg .lightning} | **0** | **12.5** | **25** |

- Damage from other players is not reflected.
- Bosses are not staggered.

## Resources and skills

| Effect | Value |
| --- | --- |
| Base eitr | +50 |
| Chance every second to regenerate 1 energy | 10% |
| Polearms skill experience with Himminafl (until Polearms level 50) | ×3 (300%) |

## Related pages

- [Thor](../demigods/thor.md)
- [Glossary](../getting-started/glossary.md)

<!-- Verified against NorseDemigods 1.9.1 -->
