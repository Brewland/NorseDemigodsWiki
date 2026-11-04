# Warp

Warp instantly teleports Kvasir forward, in the direction he is looking. It costs no energy, and its range grows with
his level.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Kvasir](../demigods/kvasir.md) |
| **Input** | ++mouse-side-up++<br>(Ability A) |
| **Energy cost** | None |
| **Cooldown** | 10 s |
| **Range** | 12–18 m, by level |
| **Config ID** | `Warp` |
| **Config section** | `[Ability Warp]` |

</div>

<!-- IMAGE: in-game screenshot of Kvasir warping forward -->

## Effect

1. You turn in the direction you are looking.
2. You teleport forward to the furthest free spot within range.

- The spot can be up to 10 m higher or lower than you.
- Walls, buildings and other obstacles (but not the terrain) between you and the spot block it.
- If no spot is found, nothing happens: no cooldown starts.
- It deals no damage.

## Range

Range grows evenly from 12 m to 18 m.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Range | 12 m | 15 m | 18 m |

## Infused

- Cooldown: 10 s → 5 s.

## Limits

- Usable while airborne. Not usable while swimming, sitting or encumbered.

## Related pages

- [Kvasir](../demigods/kvasir.md)
- [Dash](dash.md)

<!-- Verified against NorseDemigods 1.9.1 -->
