# Bomb

Bomb lets Brokkr throw an explosive that damages and pushes back enemies and breaks trees, rocks and whole ore veins
around the impact point.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Brokkr](../demigods/brokkr.md) |
| **Input** | ++mouse-side-up++<br>(Ability A) |
| **Energy cost** | 1 |
| **Cooldown** | 5 s |
| **Explosion radius** | 5 m |
| **Config ID** | `Bomb` |
| **Config section** | `[Ability Bomb]` |

</div>

<!-- IMAGE: in-game screenshot of a Bomb exploding on an ore vein -->

## Effect

1. Brokkr puts his weapons away and throws a bomb in the direction you are facing.
2. The bomb flies in an arc and explodes on impact.
3. All enemies within 5 m take damage and are pushed away.
4. Trees, rocks and ores within 5 m take resource damage.
5. Fallen logs in the area take two more hits over the next second.

## Damage

Enemies: 5 base + 0.95 [per level](../reference/glossary.md#per-level), 80% *Blunt*{.dmg .blunt} and 20%
*Fire*{.dmg .fire}.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Explosion damage | **5**<br><span class="nd-split">4 *Blunt*{.dmg .blunt} + 1 *Fire*{.dmg .fire}</span> | **52.5**<br><span class="nd-split">42 *Blunt*{.dmg .blunt} + 10.5 *Fire*{.dmg .fire}</span> | **100**<br><span class="nd-split">80 *Blunt*{.dmg .blunt} + 20 *Fire*{.dmg .fire}</span> |
| Damage to trees and ores *Chop*{.dmg .chop} *Pickaxe*{.dmg .pickaxe} | 100 | 200 | 300 |

- Resource damage: 100 base + 2 per level.
- [Tool tier](../reference/glossary.md#tool-tier) 2.

## Infused

- Cooldown: 5 s → 3 s.
- Tool tier 2 → 3: also breaks giant remains (black marble) and flametal.

## Notes

- **Collateral protection:** trees and ores are not damaged when an enemy is within 10 m of the explosion, or when an
  enemy within 6 m of you is targeting you. Setting: `[(General)] Protect Resources From Collateral Damage` (on by
  default; outdoors only).
- Throwing the bomb makes a lot of noise.

## Related pages

- [Brokkr](../demigods/brokkr.md)
- [Glossary](../reference/glossary.md)

<!-- Verified against NorseDemigods 1.9.2 -->
