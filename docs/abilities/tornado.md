# Tornado

Tornado calls a slow tornado that travels forward from Njord for 8 seconds, shocking every enemy in its path with
Lightning damage.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Njord](../demigods/njord.md) |
| **Input** | ++mouse-side-down++<br>(Ability B) |
| **Energy cost** | 2 |
| **Cooldown** | 25 s |
| **Duration** | 8 s |
| **Damage radius** | 4 m |
| **Config ID** | `Tornado` |
| **Config section** | `[Ability Tornado]` |

</div>

<!-- IMAGE: in-game screenshot of Njord's tornado moving through enemies -->

## Effect

1. Njord cheers and a tornado forms 1.5 m in front of you.
2. It moves slowly (0.7–1 m/s) in the direction you were facing, following the ground or water surface.
3. From 1 s to 8 s after casting, it hits every enemy within 4 m every 0.5 s (15 hits). It also hits birds.

- Casting is loud and alerts enemies nearby.
- Usable while airborne or swimming.
- It also hits destructible objects in its path.

## Damage

Each hit: 1 base + 0.39 [per level](../reference/glossary.md#per-level).

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Damage per hit *Lightning*{.dmg .lightning} | **1** | **20.5** | **40** |
| Damage per second *Lightning*{.dmg .lightning} | **2** | **41** | **80** |
| All 15 hits on one enemy *Lightning*{.dmg .lightning} | **15** | **307.5** | **600** |

## Infused

- Each hit: 10% chance to stagger every enemy it hits. Bosses are not staggered.

## Limits

- Not usable indoors, such as in dungeons and caves.

## Notes

- Its Lightning damage gives Njord extra demigod skill experience (see
  [Njord](../demigods/njord.md#demigod-skill-experience)).

## Related pages

- [Njord](../demigods/njord.md)

<!-- Verified against NorseDemigods 1.9.2 -->
