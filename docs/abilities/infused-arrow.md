# Infused Arrow

Infused Arrow is Ullr's bow and crossbow special attack: it charges his next arrow with extra Frost damage, and the arrow spreads
part of its damage as Frost to enemies around the spot it hits.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Ullr](../demigods/ullr.md) |
| **Input** | ++mouse-middle++ (Special attack, bows or crossbows) |
| **Energy cost** | 1 |
| **Cooldown** | 1 s |
| **Duration** | 5 s, or until you shoot |
| **Config ID** | `InfusedArrow` |
| **Config section** | `[Ability Infused Arrow]` |

</div>

<!-- IMAGE: in-game screenshot of Ullr shooting an infused arrow with a blue trail -->

## Effect

1. With a bow or crossbow equipped, use the special attack. Your hand glows.
2. Shoot within 5 s. The arrow or bolt gets extra *Frost*{.dmg .frost} damage and a blue trail.
3. Where the arrow hits (an enemy or anything else), every other enemy within 2 m takes **35%** of the arrow's total
   damage as *Frost*{.dmg .frost}. It also hits birds.

- Use the special attack again to cancel it. The energy is not refunded.
- If you do not shoot within 5 s, the infusion ends.

## Damage

Extra damage on the arrow: 10 base + 1.4 [per level](../getting-started/glossary.md#per-level).

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Extra damage *Frost*{.dmg .frost} | **10** | **80** | **150** |

- The extra damage is added to your weapon and ammo damage. The splash is based on the total.

## Infused

The splash becomes a bigger explosion:

- Radius: 2 m → 5 m.
- It deals **35%** of the arrow's total damage, split into 50% *Blunt*{.dmg .blunt} + 50% *Frost*{.dmg .frost}.
- It hits every enemy within 5 m, including the one the arrow hit, and also birds.
- It also hits destructible objects in the area.

## Limits

- Usable while airborne or swimming.

## Related pages

- [Ullr](../demigods/ullr.md)
- [Hunter](../attributes/hunter.md)

<!-- Verified against NorseDemigods 1.9.1 -->
