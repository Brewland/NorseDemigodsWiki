# Regenerative Body

Regenerative Body is Kvasir's own attribute: without heavy armor, his body gains armor and absorbs part of all damage,
and Slash wounds heal back over time. He is weak to Spirit damage.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Demigod** | [Kvasir](../demigods/kvasir.md) |
| **Condition** | Always active; armor and damage reduction only without [heavy armor](../reference/glossary.md#heavy-armor) |
| **Config ID** | `RegenerativeFlesh` |
| **Config section** | `[Attribute Regenerative Flesh]` |

</div>

<!-- IMAGE: Regenerative Body attribute icon -->

## Scaling

Without any heavy armor piece: 0.2 extra armor and 0.2% less damage taken
[per level](../reference/glossary.md#per-level).

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Extra armor | 0 | 10 | 20 |
| Damage taken reduction | 0% | 10% | 20% |

- The damage reduction applies to all damage types.
- The armor is rounded down to a whole number.

## Slash healing

- The *Slash*{.dmg .slash} damage you take is healed back over time, starting 1 s after the hit.
- Each second: up to 2% of your maximum health (at least 1 health).
- Healing stops when your health is full; any Slash damage still left is not healed later.
- Works with or without heavy armor.

## Resistances

- *Spirit*{.dmg .spirit} Weak

## Related pages

- [Kvasir](../demigods/kvasir.md)
- [Wolf Fur](wolf-fur.md)

<!-- Verified against NorseDemigods 1.9.1 -->
