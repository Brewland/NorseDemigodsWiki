# Poison Javelin

Poison Javelin is Freyja's unarmed special attack: she throws an elemental javelin that deals Pierce and Poison damage.
It costs eitr instead of energy, can give energy back on a hit and also damages rocks and ores.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Freyja](../demigods/freyja.md) |
| **Input** | ++mouse-middle++<br>(Special attack, unarmed) |
| **Eitr cost** | 15 |
| **Energy cost** | None |
| **Cooldown** | None |
| **Config ID** | `PoisonJavelin` |
| **Config section** | `[Ability Poison Javelin]` |

</div>

<!-- IMAGE: in-game screenshot of Freyja throwing a Poison Javelin -->

## Effect

1. Freyja throws a javelin toward your aim point, like a thrown spear.
2. The javelin damages the first enemy it hits.
3. If it hits an enemy: 30% chance to regenerate 1 energy.

- The throw costs no stamina.
- The javelin falls in an arc and can be blocked and dodged.
- It disappears after 10 s if it hits nothing.

## Damage

10 base + 1.9 [per level](../reference/glossary.md#per-level), split evenly between the two types.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Damage | **10**<br><span class="nd-split">5 *Pierce*{.dmg .pierce} + 5 *Poison*{.dmg .poison}</span> | **105**<br><span class="nd-split">52.5 *Pierce*{.dmg .pierce} + 52.5 *Poison*{.dmg .poison}</span> | **200**<br><span class="nd-split">100 *Pierce*{.dmg .pierce} + 100 *Poison*{.dmg .poison}</span> |
| Damage to rocks and ores *Pickaxe*{.dmg .pickaxe} | 10 | 105 | 200 |

- [Tool tier](../reference/glossary.md#tool-tier) 1.

## Infused

- Eitr cost: 15 → 10.

## Notes

- No energy regeneration while an energy-draining ability is active.
- Sneak attacks deal ×4 damage.
- Freyja's hits also weaken enemies that resist Poison (see [Freyja](../demigods/freyja.md#class-quirks)).

## Related pages

- [Freyja](../demigods/freyja.md)
- [Glossary](../reference/glossary.md)

<!-- Verified against NorseDemigods 1.9.1 -->
