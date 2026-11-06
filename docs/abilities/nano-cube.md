# Nano Cube

Nano Cube forges a large cube of lightning around Brokkr for 5 seconds. Enemies inside take Lightning damage twice
per second, while players inside are healed.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Brokkr](../demigods/brokkr.md) |
| **Input** | ++mouse-side-down++ + ++block++<br>(Ability D) |
| **Energy cost** | 2 |
| **Cooldown** | 30 s |
| **Duration** | 5 s |
| **Range** | Cube 8 m wide |
| **Config ID** | `NanoCube` |
| **Config section** | `[Ability Nano Cube]` |

</div>

<!-- IMAGE: in-game screenshot of the Nano Cube around a group of enemies -->

## Effect

1. A cube 8 m wide appears where you stand. It does not move with you.
2. Every 0.5 s for 5 s, it pulses:
    - Every enemy inside takes *Lightning*{.dmg .lightning} damage and has a 10% chance to be staggered.
    - Every injured player inside, including you, is healed.

## Damage and healing

Damage per pulse: 1 base + 0.14 [per level](../reference/glossary.md#per-level).
Healing per pulse grows evenly from 3 at level 0 to 8 at level 100.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Damage per pulse *Lightning*{.dmg .lightning} | **1** | **8** | **15** |
| Damage per second *Lightning*{.dmg .lightning} | **2** | **16** | **30** |
| Healing per pulse | **3** | **5.5** | **8** |
| Healing per second | **6** | **11** | **16** |

## Infused

- The cube is 50% larger: 12 m wide.

## Notes

- Bosses are not staggered.

## Related pages

- [Brokkr](../demigods/brokkr.md)

<!-- Verified against NorseDemigods 1.9.2 -->
