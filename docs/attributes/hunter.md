# Hunter

Hunter is Ullr's own attribute: his arrows and spears deal extra Poison damage, he shoots faster without heavy armor,
his arrow hits can give energy, and hunted animals drop twice the skins and feathers.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Demigod** | [Ullr](../demigods/ullr.md) |
| **Condition** | Always active; draw and reload bonuses only without [heavy armor](../getting-started/glossary.md#heavy-armor) |
| **Config ID** | `Hunter` |
| **Config section** | `[Attribute Hunter]` |

</div>

<!-- IMAGE: in-game screenshot of Ullr hunting a deer with a bow -->

## Weapons

| Effect | Value |
| --- | --- |
| Extra damage as *Poison*{.dmg .poison}, bows and crossbows | +20% |
| Extra damage as *Poison*{.dmg .poison}, spears | +20% |
| Bow draw speed, without heavy armor | +25% |
| Crossbow reload time, without heavy armor | −30% |
| Chance to regenerate 1 energy when an arrow or bolt hits an enemy | 50% |
| Bows and Crossbows skill experience | ×2 (200%) |

- "Without heavy armor" means no [heavy armor](../getting-started/glossary.md#heavy-armor) piece at all.

## Skins and feathers

- When an enemy dies within 50 m of you, it drops twice the usual skins. It doesn't have to be your kill.
- Skins: leather scraps, deer hide, wolf pelt, lox pelt, scale hide and asksvin hide (and some skins from other mods).
  Servers can change the list: `[Attribute Hunter] Skin Drop List`.
- Birds (seagulls, crows and ash crows) killed within 50 m of you drop twice the feathers.
- If several players with Hunter are nearby, only the closest one counts. Several Hunters do not add up.
- Tamed creatures and summoned companions never drop extra skins.

## Notes

- No energy regeneration while an energy-draining ability is active.

## Related pages

- [Ullr](../demigods/ullr.md)
- [Bloody Archer](bloody-archer.md)
- [Sense Creatures](../abilities/sense-creatures.md)

<!-- Verified against NorseDemigods 1.9.1 -->
