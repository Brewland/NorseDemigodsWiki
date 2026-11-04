# Abyssal Harpoon

The Abyssal Harpoon is a vanilla weapon that this mod turns into a fishing tool: throw it at a fish in the water to
catch it. The mod also lets you upgrade it.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Type** | Weapon (vanilla item) |
| **Crafting station** | Unchanged (vanilla recipe) |
| **Restricted to** | Anyone |
| **Config ID** | `SpearChitin` |
| **Config section** | `[Harpoon Fishing]` |

</div>

<!-- IMAGE: throwing an Abyssal Harpoon at a fish in the water -->

Harpoon fishing is on by default. Setting: `[Harpoon Fishing] Enable Harpoon Fishing`. When it is off, the
harpoon works as in vanilla.

## Harpoon fishing

1. Throw the harpoon at a fish that is swimming in the water.
2. The fish goes straight into your inventory.

- You do not need to be a demigod.
- The thrown harpoon has a 0.3 m hit radius (vanilla: none), so fish are easier to hit. Setting:
  `[Harpoon Fishing] Harpoon Projectile Collision Radius`.

## Upgrades

The vanilla harpoon cannot be upgraded. With this mod, it goes up to quality 3:

| Upgrade to | Chitin | Durability |
| --- | ---: | ---: |
| Quality 2 | 15 | +25 |
| Quality 3 | 30 | +25 |

- Upgrades cost only chitin.
- Each upgrade needs the crafting station one level higher than the last (vanilla rule).
- Settings: `[Harpoon Fishing] Harpoon Max Quality`, `[Harpoon Fishing] Harpoon Upgrade Chitin Per Level` and
  `[Harpoon Fishing] Harpoon Upgrade Durability Per Level`.

## Buying one

!!! info "If enabled"
    Off by default. Requires `[Merchant] Enable Custom Merchant Items` = `true`.

Haldor sells the Abyssal Harpoon for 350 coins. Setting: `[Merchant] Abyssal Harpoon Price` (`0` removes it from
his shop).

## Related pages

- [Sweet Fish Foods](sweet-fish-foods.md)

<!-- Verified against NorseDemigods 1.9.1 -->
