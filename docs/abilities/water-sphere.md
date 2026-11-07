# Water Sphere

Water Sphere summons four water spheres above Njord's head. They launch one after another at the closest enemy and
explode on impact with Blunt damage.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Njord](../demigods/njord.md) |
| **Input** | ++mouse-side-up++<br>(Ability A) |
| **Energy cost** | 1 |
| **Cooldown** | 10 s |
| **Range** | Targets enemies within 15 m |
| **Explosion radius** | 3 m |
| **Config ID** | `WaterSphere` |
| **Config section** | `[Ability Water Sphere]` |

</div>

<!-- IMAGE: in-game screenshot of water spheres hovering above Njord -->

## Effect

1. 4 spheres appear 3 m above the spot where you cast. They stay there until launched.
2. After 1.5 s, the first sphere launches; the others follow every 0.5 s.
3. Each sphere flies at the closest enemy within 15 m, and explodes on arrival. It only targets enemies in line
   of sight, never behind walls or terrain.
4. The explosion damages all enemies within 3 m, and also birds.

- A sphere that finds no enemy bursts without damage.
- You cannot cast again while spheres are still waiting.
- Usable while airborne or swimming.

## Damage

5 base + 0.7 [per level](../reference/glossary.md#per-level), per sphere.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Damage per sphere *Blunt*{.dmg .blunt} | **5** | **40** | **75** |
| All 4 spheres on one enemy *Blunt*{.dmg .blunt} | **20** | **160** | **300** |

## Infused

- Spheres per cast: 4 → 6.

## Related pages

- [Njord](../demigods/njord.md)

<!-- Verified against NorseDemigods 1.9.3 -->
