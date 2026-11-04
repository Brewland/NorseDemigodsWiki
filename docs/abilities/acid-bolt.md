# Acid Bolt

Acid Bolt is Hel's unarmed special attack: an acid bolt that explodes on impact, dealing true damage plus extra Poison
damage to enemies around it. It costs eitr instead of energy and can give energy back on a hit.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Hel](../demigods/hel.md) |
| **Input** | ++mouse-middle++<br>(Special attack, unarmed) |
| **Eitr cost** | 15 |
| **Energy cost** | None |
| **Cooldown** | None |
| **Explosion radius** | 2 m |
| **Config ID** | `AcidBolt` |
| **Config section** | `[Ability Acid Bolt]` |

</div>

<!-- IMAGE: in-game screenshot of an Acid Bolt exploding on an enemy -->

## Effect

1. Hel casts an acid bolt toward your aim point.
2. It explodes where it hits, damaging all enemies within 2 m.
3. If it hits an enemy: 30% chance to regenerate 1 energy.

- The bolt can be blocked and dodged.
- It drops slightly in flight and disappears after 20 s if it hits nothing.

## Damage

[True damage](../reference/glossary.md#true-damage): 5 base + 0.7
[per level](../reference/glossary.md#per-level). Extra *Poison*{.dmg .poison} damage: 20% of the true damage.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| True damage | **5** | **40** | **75** |
| Extra damage *Poison*{.dmg .poison} | **1** | **8** | **15** |

- The in-game status shows the two values separately.
- The explosion also damages trees, rocks and ores within 2 m. [Tool tier](../reference/glossary.md#tool-tier) 1.

## Infused

- Eitr cost: 15 → 10.

## Notes

- No energy regeneration while an energy-draining ability is active, such as [Decay Aura](decay-aura.md).

## Related pages

- [Hel](../demigods/hel.md)
- [Glossary](../reference/glossary.md)

<!-- Verified against NorseDemigods 1.9.1 -->
