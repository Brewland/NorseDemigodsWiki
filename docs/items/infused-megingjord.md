# Infused Megingjord

Infused Megingjord is an upgraded version of the vanilla Megingjord belt: while you wear it, you can carry much
more and have more maximum energy.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Type** | Equipment (belt) |
| **Restricted to** | Anyone (the energy bonus needs a demigod) |
| **Stack size** | 1 |
| **Config ID** | `InfusedBeltStrength` |
| **Config section** | `[Enhanced Megingjord]` |

</div>

<!-- IMAGE: Infused Megingjord in the inventory, with its tooltip -->

## Effect

While equipped:

| Effect | Value |
| --- | --- |
| Carry weight | +300 |
| Maximum energy | +3 |

- The +300 replaces the vanilla Megingjord's +150 carry weight; they do not add up.
- Taking the belt off lowers your energy to your new maximum.
- Bonus maximum energy also makes [Restoration](../abilities/restoration.md)'s blast stronger.

## Recipe

??? spoiler "Recipe (spoiler)"

    Craft it at a Forge (level 7+).

    - The Megingjord is used up.
    - With [Blacksmith](../attributes/blacksmith.md) (Brokkr), a level 6 Forge counts as level 7.

    | Material | Amount |
    | --- | --- |
    | Megingjord | 1 |
    | Thunderstone | 20 |

Servers can change the second material and its amount: `[Enhanced Megingjord] Infused Megingjord Cost Item Name`
and `[Enhanced Megingjord] Infused Megingjord Cost Item Quantity`.

## Notes

- Settings for the bonuses: `[Enhanced Megingjord] Infused Megingjord Increased Max Weight` and
  `[Enhanced Megingjord] Infused Megingjord Increased Energy`.

## Related pages

- [Restoration](../abilities/restoration.md)
- [Blacksmith](../attributes/blacksmith.md)

<!-- Verified against NorseDemigods 1.9.3 -->
