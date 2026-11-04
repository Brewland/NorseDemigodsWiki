# Thorn Body

Thorn Body is Freyja's own attribute: the thorns on her skin add Poison damage to her weapons and spread it to nearby
enemies, give her extra health and eitr, and let her draw energy from trees.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Demigod** | [Freyja](../demigods/freyja.md) |
| **Condition** | Always active; energy from trees only near a tree |
| **Config ID** | `ThornBody` |
| **Config section** | `[Attribute Thorn Body]` |

</div>

<!-- IMAGE: Thorn Body attribute icon -->

## Weapon damage

Extra damage added to your weapon hits:

| Weapon | Extra damage *Poison*{.dmg .poison} |
| --- | ---: |
| Bows and crossbows | +20% |
| Spears and swords | +20% |
| Axes, clubs and polearms | +10% |

- Knives and unarmed attacks get no extra damage.
- **Poison splash:** hits with spears or swords also deal **50%** of the hit's damage as *Poison*{.dmg .poison} to
  other enemies within 2 m.

## Energy from trees

- Every 5 s, if a tree is within 8 m of you, you absorb 1 energy from it.
- Only while your energy is not full.

## Resources and defense

| Effect | Value |
| --- | --- |
| Maximum health | +15 |
| Base eitr | +25 |
| *Poison*{.dmg .poison} resistance | Very resistant |

## Notes

- Freyja's damage also weakens enemies that resist Poison (see [Freyja](../demigods/freyja.md#class-quirks)).

## Related pages

- [Freyja](../demigods/freyja.md)
- [Glossary](../reference/glossary.md)

<!-- Verified against NorseDemigods 1.9.1 -->
