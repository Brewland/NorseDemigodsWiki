# Meteor

Meteor calls a meteor down from the sky onto the spot you aim at. It deals Blunt and Fire damage where it lands and
knocks down trees. It costs eitr instead of energy and can give energy back on a hit.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Hel](../demigods/hel.md) |
| **Input** | ++mouse-side-up++<br>(Ability A) |
| **Eitr cost** | 50 |
| **Energy cost** | None |
| **Cooldown** | 5 s |
| **Range** | 30 m |
| **Explosion radius** | 5 m |
| **Config ID** | `Meteor` |
| **Config section** | `[Ability Meteor]` |

</div>

<!-- IMAGE: in-game screenshot of a meteor falling on a group of enemies -->

## Effect

1. Aim at a spot within 30 m and cast. Hel cheers.
2. A meteor falls from 50 m above that spot and explodes where it lands.
3. The explosion damages enemies and trees around it.
4. If it hits an enemy: 70% chance to regenerate 1 energy.

- Casting is loud and alerts enemies nearby.

## Damage

10 base + 1.4 [per level](../reference/glossary.md#per-level), split evenly between the two types.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Damage | **10**<br><span class="nd-split">5 *Blunt*{.dmg .blunt} + 5 *Fire*{.dmg .fire}</span> | **80**<br><span class="nd-split">40 *Blunt*{.dmg .blunt} + 40 *Fire*{.dmg .fire}</span> | **150**<br><span class="nd-split">75 *Blunt*{.dmg .blunt} + 75 *Fire*{.dmg .fire}</span> |
| Damage to trees *Chop*{.dmg .chop} | 200 | 400 | 600 |

- Damage to trees: 200 base + 4 per level. [Tool tier](../reference/glossary.md#tool-tier) 1.

## Infused

- Eitr cost: 50 → 30.

## Limits

- Not usable indoors, such as in dungeons and caves.
- You must aim at something within 30 m.
- Not usable while swimming.

## Notes

- **Collateral protection:** trees and ores are not damaged when an enemy is within 10 m of the explosion, or when an
  enemy within 6 m of you is targeting you. Setting: `[(General)] Protect Resources From Collateral Damage` (on by
  default; outdoors only).
- No energy regeneration while an energy-draining ability is active, such as [Decay Aura](decay-aura.md).

## Related pages

- [Hel](../demigods/hel.md)
- [Glossary](../reference/glossary.md)

<!-- Verified against NorseDemigods 1.9.3 -->
