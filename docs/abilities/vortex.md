# Vortex

Vortex is a channeled wind ability for Hraesvelgr: a vortex around him pulls in loose objects, picks nearby plants and
fish, and ends in an explosion that damages every enemy around him. It costs no energy.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Hraesvelgr](../demigods/hraesvelgr.md) |
| **Input** | ++mouse-side-down++<br>(Ability B), hold |
| **Energy cost** | None |
| **Cooldown** | 15 s, starts when activated |
| **Duration** | Up to 8 s of channeling |
| **Range** | Pulls objects within 20 m |
| **Explosion radius** | 10 m |
| **Config ID** | `Vortex` |
| **Config section** | `[Ability Vortex]` |

</div>

<!-- IMAGE: in-game screenshot of Hraesvelgr channeling the vortex with items flying towards him -->

## Effect

1. Hold the key. A vortex forms around you.
2. While you hold it, loose objects within 20 m are pulled towards you, more strongly the longer you channel.
3. When you release the key, or after 8 s, the vortex explodes if you channeled for at least 0.5 s.
4. The explosion damages every enemy within 10 m and throws the pulled objects away from you.

- Pulled objects: dropped items, fish, logs, carts and other loose physics objects. Creatures and players are not
  pulled.
- **Plants:** pickable plants within 20 m (such as berries, mushrooms and ripe crops) are picked after 4.5–6 s of
  channeling, and their drops are pulled in.
- **Fish:** fish within 20 m are pulled too. A fish that ends up out of the water within 2 m of you is picked up after
  1 s.
- A cart another player is pulling or has open is not pulled.
- The explosion also hits birds. It is very loud and alerts enemies nearby.

## Damage

The explosion deals *Blunt*{.dmg .blunt} damage for each second you channeled, up to 3 s:
5 base + 0.45 [per level](../reference/glossary.md#per-level) per second.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Damage per second channeled *Blunt*{.dmg .blunt} | **5** | **27.5** | **50** |
| Peak damage, 3 s or more *Blunt*{.dmg .blunt} | **15** | **82.5** | **150** |

- Every enemy within 10 m takes the same damage.
- Channeling longer than 3 s pulls harder but adds no damage.

## Cooldown reset

- If you release the key before 0.5 s, there is no explosion and the cooldown resets.
- If the explosion hits no enemy, the cooldown resets. Setting: `[Ability Vortex] Reset Cooldown On No Damage`
  (on by default).

## Infused

The explosion also deals *Chop*{.dmg .chop} damage to trees and other destructible objects within 10 m, with
[tool tier](../reference/glossary.md#tool-tier) 1. Per second channeled, up to 3 s: 10 base + 0.2 per level.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Damage to trees per second channeled *Chop*{.dmg .chop} | **10** | **20** | **30** |
| Peak damage to trees, 3 s or more *Chop*{.dmg .chop} | **30** | **60** | **90** |

- The felled logs are pulled in by your next vortex like any loose object.

## Limits

- Usable while airborne. Not usable while swimming.

## Notes

- **Collateral protection:** trees and ores are not damaged when an enemy is within 10 m of the explosion, or when an
  enemy within 6 m of you is targeting you. Setting: `[(General)] Protect Resources From Collateral Damage` (on by
  default; outdoors only).
- The push on objects gets weaker with distance from you. Enemies are not pushed.

## Related pages

- [Hraesvelgr](../demigods/hraesvelgr.md)
- [Telekinesis](telekinesis.md)

<!-- Verified against NorseDemigods 1.9.1 -->
