# Burning Ground

Burning Ground sets the ground where Surtr stands on fire for 6 seconds, burning every enemy in it. Infused, it also
charges a large explosion and cleanses Poison and Frost from him.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Surtr](../demigods/surtr.md) |
| **Input** | ++mouse-side-up++<br>(Ability A) |
| **Energy cost** | 2 |
| **Cooldown** | 30 s |
| **Duration** | 6 s |
| **Fire radius** | 3 m |
| **Config ID** | `BurningGround` |
| **Config section** | `[Ability Burning Ground]` |

</div>

<!-- IMAGE: in-game screenshot of Surtr standing in a circle of fire -->

## Effect

1. A circle of fire appears where you stand. It does not move with you.
2. For 6 s, it deals *Fire*{.dmg .fire} damage to everything within 3 m, right away and then every second.
3. With [Cold Blood](../attributes/cold-blood.md) (Surtr's default), standing in your own fire heals you every second.

- It never hits you, tamed creatures or summoned companions, yours or anyone else's.
- It hits other players only if they have PvP on (a vanilla rule).
- Neutral creatures that can be angered, such as the Dvergr, are hit too.
- Only one fire burns at a time: casting again puts out the previous one. This only matters on servers that set
  the cooldown shorter than the duration.

## Damage

2 base + 0.48 [per level](../reference/glossary.md#per-level), per second.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Damage per second *Fire*{.dmg .fire} | **2** | **26** | **50** |
| Total over 6 s *Fire*{.dmg .fire} | **12** | **156** | **300** |

## Infused

- **Explosion:** 4.8 s after casting, the spot where you cast explodes, hitting every enemy within 9 m. It also hits
  birds, and is loud enough to alert enemies far away.
- **Cleanse:** while you stand in the fire, Poison and Frost are removed from you every second.

Explosion damage: 1.25 [per level](../reference/glossary.md#per-level), with no base damage, split 80%
*Blunt*{.dmg .blunt} and 20% *Fire*{.dmg .fire}.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Explosion damage | **0** | **62.5**<br><span class="nd-split">50 *Blunt*{.dmg .blunt} + 12.5 *Fire*{.dmg .fire}</span> | **125**<br><span class="nd-split">100 *Blunt*{.dmg .blunt} + 25 *Fire*{.dmg .fire}</span> |

## Limits

- Not usable while airborne or swimming.

## Related pages

- [Surtr](../demigods/surtr.md)
- [Cold Blood](../attributes/cold-blood.md)

<!-- Verified against NorseDemigods 1.9.3 -->
