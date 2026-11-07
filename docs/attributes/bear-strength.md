# Bear Strength

Bear Strength lets you move freely in heavy equipment, carry much more and hit harder with melee weapons the more
energy you have left.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Demigods** | [Njord](../demigods/njord.md), [Surtr](../demigods/surtr.md), [Thor](../demigods/thor.md) |
| **Condition** | Always active |
| **Config ID** | `BearStrength` |
| **Config section** | `[Attribute Bear Strength]` |

</div>

<!-- IMAGE: Bear Strength attribute icon -->

## Effects

| Effect | Value |
| --- | --- |
| Movement penalty from equipment ignored | Up to 25% |
| Extra damage with axes, clubs, polearms, spears and swords *Blunt*{.dmg .blunt} | Up to +5%, based on unspent energy |
| Extra damage to trees with an axe | +50% |
| Extra damage to ores with a pickaxe | +25% |

## Scaling

Extra carry weight: 2 [per level](../reference/glossary.md#per-level).

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Extra carry weight | 0 | 100 | 200 |

## Notes

- The movement penalty counts all equipment together.
- Example: 30% total penalty from [heavy armor](../reference/glossary.md#heavy-armor), weapon and shield
  slows you by only 5%.
- The extra *Blunt*{.dmg .blunt} damage scales with current energy compared to maximum energy.
- Example: +5% at full energy, +2% with 2 of 5 energy.
- Knives and unarmed attacks get no extra damage.

## Related pages

- [Njord](../demigods/njord.md)
- [Surtr](../demigods/surtr.md)
- [Thor](../demigods/thor.md)
- [Eagle Strength](eagle-strength.md)

<!-- Verified against NorseDemigods 1.9.3 -->
