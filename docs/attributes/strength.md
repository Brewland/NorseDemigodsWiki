# Strength Attributes

Passive attributes that let demigods wear heavy equipment with less slowdown, carry more weight and hit harder.

<!-- IMAGE: Bear Strength attribute icon -->

| Attribute | Demigods | Summary |
| --- | --- | --- |
| [Bear Strength](#bear-strength) | Njord, Surtr, [Thor](../demigods/thor.md) | Less armor slowdown, more carry weight, extra melee, tree and ore damage. |

<!-- Eagle Strength (Eir, Freyja, Hraesvelgr) will be added in a later batch. -->

## Bear Strength

Bear Strength lets you move freely in heavy equipment, carry much more and hit harder with melee weapons the more
energy you have left.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Demigods** | Njord, Surtr, [Thor](../demigods/thor.md) |
| **Condition** | Always active |
| **Config ID** | `BearStrength` |
| **Config section** | `[Attribute Bear Strength]` |

</div>

| Effect | Value |
| --- | --- |
| Movement penalty from equipment ignored | Up to 25% |
| Extra damage with axes, clubs, polearms, spears and swords *Blunt*{.dmg .blunt} | Up to +5%, based on unspent energy |
| Extra damage to trees with an axe | +50% |
| Extra damage to ores with a pickaxe | +25% |

Extra carry weight: 2 [per level](../getting-started/glossary.md#per-level).

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Extra carry weight | 0 | 100 | 200 |

**Notes:**

- The movement penalty counts all equipment together.
- Example: 30% total penalty from [heavy armor](../getting-started/glossary.md#heavy-armor), weapon and shield
  slows you by only 5%.
- The extra *Blunt*{.dmg .blunt} damage scales with current energy compared to maximum energy.
- Example: +5% at full energy, +2% with 2 of 5 energy.
- Knives and unarmed attacks get no extra damage.

<!-- Verified against NorseDemigods 1.9.0 -->
