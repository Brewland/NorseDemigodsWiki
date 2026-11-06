# Ice Shards

Ice Shards lets Fenrir hurl ice shards from his bare hands, dealing Pierce and Frost damage.
It costs eitr instead of energy, can give energy back on a hit and also damages ores.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Fenrir](../demigods/fenrir.md) |
| **Input** | ++block++ + ++mouse-middle++<br>(Special attack while blocking, unarmed) |
| **Eitr cost** | 7 |
| **Energy cost** | None |
| **Cooldown** | None |
| **Config ID** | `Iceshards` |
| **Config section** | `[Ability Iceshards]` |

</div>

<!-- IMAGE: in-game screenshot of Fenrir firing ice shards -->

## Effect

1. Hold block with bare hands and use the special attack.
2. Fenrir casts an ice shard toward your aim point, with a slight spread.
3. Each shard that hits an enemy: 10% chance to regenerate 1 energy.

## Damage

Each shard: 5 base + 0.75 [per level](../reference/glossary.md#per-level), split evenly between the two types.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Damage per shard | **5**<br><span class="nd-split">2.5 *Pierce*{.dmg .pierce} + 2.5 *Frost*{.dmg .frost}</span> | **42.5**<br><span class="nd-split">21.25 *Pierce*{.dmg .pierce} + 21.25 *Frost*{.dmg .frost}</span> | **80**<br><span class="nd-split">40 *Pierce*{.dmg .pierce} + 40 *Frost*{.dmg .frost}</span> |
| Damage to ores per shard *Pickaxe*{.dmg .pickaxe} | 5 | 42.5 | 80 |

- [Tool tier](../reference/glossary.md#tool-tier) 1.
- One shard per cast.

## Infused

- Eitr cost: 7 → 5.

## Limits

- Bare hands only: not with fist weapons.

## Notes

- No energy regeneration while an energy-draining ability is active.
- [Frost Body](../attributes/frost-body.md)'s bonus for frost staffs does not apply to Ice Shards.

## Related pages

- [Fenrir](../demigods/fenrir.md)
- [Frost Body](../attributes/frost-body.md)

<!-- Verified against NorseDemigods 1.9.2 -->
