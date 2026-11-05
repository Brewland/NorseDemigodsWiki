# Permanent Consumables

Permanent consumables are crafted items that any demigod can consume for a lasting bonus, such as more health,
armor, eitr or faster energy regeneration. The bonuses stay when you switch to another demigod.

## How they work

- Only demigods can consume them.
- The effect is permanent. Most items can be consumed once; Infused Hard Antlers and Infused Leather Scraps can be
  consumed up to 5 times each, and each one adds to the effect.
- If you are already at the limit, nothing happens and the item is not used up.
- Effects stay when you switch demigods with the [Demigod Runestone](demigod-runestone.md).
- Your consumed effects are listed in the in-game compendium, under "ND: Acquired Attributes".
- Recipes and crafting stations are in spoiler boxes below.
- With [Blacksmith](../attributes/blacksmith.md) (Brokkr), crafting stations count as one level higher.
- Damage, healing and summon values on the other pages of this wiki assume no Infused Liquid Frost and no Infused
  Morgenheart.

## Overview

<div class="nd-overview" markdown>

| Item | Effect | Consume limit |
| --- | --- | --- |
| [Infused Bloodbag](#infused-bloodbag) | +20 maximum health | Once |
| [Infused Chitin](#infused-chitin) | +5 block armor (+10 with tower shields) | Once |
| [Infused Earthbreaker](#infused-earthbreaker) | +1 tool tier for some abilities and attributes | Once |
| [Infused Grand Earthbreaker](#infused-grand-earthbreaker) | +3 tool tier instead of +1 | Once, after Infused Earthbreaker |
| [Infused Eitr](#infused-eitr) | +25 base eitr, faster eitr regeneration | Once |
| [Infused Hard Antlers](#infused-hard-antlers) | +3% melee attack speed each | 5 times |
| [Infused Leather Scraps](#infused-leather-scraps) | −10% energy regeneration time each | 5 times |
| [Infused Liquid Frost](#infused-liquid-frost) | +20% ability and attribute damage and healing | Once |
| [Infused Morgenheart](#infused-morgenheart) | +25% damage, +25% health for summons | Once |
| [Infused Serpent Scale](#infused-serpent-scale) | +5 armor | Once |

</div>

## Infused Bloodbag

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Type** | Consumable (permanent effect) |
| **Effect** | +20 maximum health |
| **Restricted to** | Any demigod |
| **Stack size** | 1 |
| **Consume limit** | Once |
| **Config ID** | `InfusedBloodbag` |
| **Config section** | `[Attribute Infused Bloodbag]` |

</div>

<!-- IMAGE: Infused Bloodbag in the inventory -->

??? spoiler "Recipe (spoiler)"

    Craft it at a Forge (level 3+).

    | Material | Amount |
    | --- | --- |
    | Thunderstone | 10 |
    | Bloodbag | 50 |

## Infused Chitin

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Type** | Consumable (permanent effect) |
| **Effect** | +5 block armor (+10 with tower shields) |
| **Restricted to** | Any demigod |
| **Stack size** | 1 |
| **Consume limit** | Once |
| **Config ID** | `InfusedChitin` |
| **Config section** | `[Attribute Infused Chitin]` |

</div>

<!-- IMAGE: Infused Chitin in the inventory -->

| Blocking with | Block armor |
| --- | --- |
| Shields (except tower shields) | +5 |
| Tower shields | +10 |
| Two-handed weapons | +5 |
| Bare hands with [Titan Arms](../attributes/titan-arms.md) (Fenrir) | +5 |

- Shields without a parry bonus count as tower shields.

??? spoiler "Recipe (spoiler)"

    Craft it at a Forge (level 3+).

    | Material | Amount |
    | --- | --- |
    | Thunderstone | 10 |
    | Bronze | 10 |
    | Chitin | 50 |

## Infused Earthbreaker

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Type** | Consumable (permanent effect) |
| **Effect** | +1 [tool tier](../reference/glossary.md#tool-tier) for the abilities and attributes below |
| **Restricted to** | Any demigod |
| **Stack size** | 1 |
| **Consume limit** | Once |
| **Config ID** | `InfusedEarthbreaker` |
| **Config section** | `[Attribute Infused Earthbreaker]` |

</div>

<!-- IMAGE: Infused Earthbreaker in the inventory -->

It applies to the abilities and attributes that let you damage trees, rocks and ores with their own tool tier:

- Abilities: [Acid Bolt](../abilities/acid-bolt.md), [Bomb](../abilities/bomb.md),
  [Energy Wisp](../abilities/energy-wisp.md), [Fireball](../abilities/fireball.md),
  [Holy Sun](../abilities/holy-sun.md), [Ice Shards](../abilities/ice-shards.md), [Meteor](../abilities/meteor.md),
  [Poison Javelin](../abilities/poison-javelin.md), [Slash](../abilities/slash.md), [Vortex](../abilities/vortex.md).
- Attributes: [Piercing Instincts](../attributes/piercing-instincts.md), [Titan Arms](../attributes/titan-arms.md).

??? spoiler "Recipe (spoiler)"

    Craft it at a Forge (level 1+).

    | Material | Amount |
    | --- | --- |
    | Bronze pickaxe | 1 |
    | Hard antler | 2 |

## Infused Grand Earthbreaker

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Type** | Consumable (permanent effect) |
| **Effect** | +3 [tool tier](../reference/glossary.md#tool-tier) (replaces Infused Earthbreaker's +1) |
| **Restricted to** | Any demigod |
| **Stack size** | 1 |
| **Consume limit** | Once, after Infused Earthbreaker |
| **Config ID** | `InfusedEarthbreakerGrand` |
| **Config section** | `[Attribute Infused Earthbreaker]` (shared with Infused Earthbreaker) |

</div>

<!-- IMAGE: Infused Grand Earthbreaker in the inventory -->

An upgrade of [Infused Earthbreaker](#infused-earthbreaker): the same abilities and attributes get a bigger bonus.

- You must consume Infused Earthbreaker first.
- After Infused Grand Earthbreaker, Infused Earthbreaker can no longer be consumed.

??? spoiler "Recipe (spoiler)"

    Craft it at a Forge (level 3+).

    | Material | Amount |
    | --- | --- |
    | Black metal pickaxe | 1 |
    | Dragon tear | 1 |
    | Wisp | 3 |

## Infused Eitr

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Type** | Consumable (permanent effect) |
| **Effect** | +25 base eitr<br>+5% eitr regeneration per unspent energy point |
| **Restricted to** | Any demigod |
| **Stack size** | 1 |
| **Consume limit** | Once |
| **Config ID** | `InfusedEitr` |
| **Config section** | `[Attribute Infused Eitr]` |

</div>

<!-- IMAGE: Infused Eitr in the inventory -->

The regeneration bonus depends on how much energy you have right now:

| Unspent energy | 2 | 7 | 12 |
| --- | ---: | ---: | ---: |
| Eitr regeneration | +10% | +35% | +60% |

- Your maximum energy is 2 at demigod skill level 0 and 12 at level 100 (default settings, no bonuses).

??? spoiler "Recipe (spoiler)"

    Craft it at a Galdr table (level 3+).

    | Material | Amount |
    | --- | --- |
    | Thunderstone | 40 |
    | Refined eitr | 60 |

## Infused Hard Antlers

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Type** | Consumable (permanent effect) |
| **Effect** | +3% attack speed with melee weapons, per item consumed |
| **Restricted to** | Any demigod |
| **Stack size** | 1 |
| **Consume limit** | 5 times |
| **Config ID** | `InfusedHardAntlers` |
| **Config section** | `[Attribute Infused Hard Antlers]` |

</div>

<!-- IMAGE: Infused Hard Antlers in the inventory -->

| Items consumed | 1 | 2 | 3 | 4 | 5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Attack speed | +3% | +6% | +9% | +12% | +15% |

- Any melee weapon; not with bare hands.

??? spoiler "Recipe (spoiler)"

    Craft it at a Forge (level 3+).

    | Material | Amount |
    | --- | --- |
    | Surtling core | 5 |
    | Hard antler | 3 |

## Infused Leather Scraps

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Type** | Consumable (permanent effect) |
| **Effect** | −10% energy regeneration time, per item consumed |
| **Restricted to** | Any demigod |
| **Stack size** | 1 |
| **Consume limit** | 5 times |
| **Config ID** | `InfusedLeatherScraps` |
| **Config section** | `[Attribute Infused Leather Scraps]` |

</div>

<!-- IMAGE: Infused Leather Scraps in the inventory -->

Energy regenerates on its own, 1 point every 10 seconds. Each item consumed shortens that time by 10% of the
default:

| Items consumed | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Time per energy point | 10 s | 9 s | 8 s | 7 s | 6 s | 5 s |

- The default time is a setting: `[Energy] Energy Regeneration Period (seconds)`.

??? spoiler "Recipe (spoiler)"

    Craft it at a Forge (level 3+).

    | Material | Amount |
    | --- | --- |
    | Thunderstone | 5 |
    | Leather scraps | 50 |

## Infused Liquid Frost

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Type** | Consumable (permanent effect) |
| **Effect** | +20% flat ability and attribute damage<br>+20% flat ability and attribute healing |
| **Restricted to** | Any demigod |
| **Stack size** | 1 |
| **Consume limit** | Once |
| **Config ID** | `InfusedLiquidFrost` |
| **Config section** | `[Attribute Infused Liquid Frost]` |

</div>

<!-- IMAGE: Infused Liquid Frost in the inventory -->

- "Flat" means fixed amounts, such as an ability's base damage and its damage per level. Percentage-based effects
  (for example "+10% extra damage") are unchanged.

??? spoiler "Recipe (spoiler)"

    Craft it at a Galdr table (level 3+).

    | Material | Amount |
    | --- | --- |
    | Thunderstone | 40 |
    | Liquid frost | 80 |
    | Barka trophy | 1 |

## Infused Morgenheart

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Type** | Consumable (permanent effect) |
| **Effect** | +25% summoned creature damage<br>+25% summoned creature maximum health |
| **Restricted to** | Any demigod |
| **Stack size** | 1 |
| **Consume limit** | Once |
| **Config ID** | `InfusedMorgenHeart` |
| **Config section** | `[Attribute Infused Morgen Heart]` |

</div>

<!-- IMAGE: Infused Morgenheart in the inventory -->

- Applies to the creatures of [Minions](../abilities/minions.md), [Neck](../abilities/neck.md),
  [Poison Cloud](../abilities/poison-cloud.md), [Stone Golem](../abilities/stone-golem.md),
  [Summon Surtling](../abilities/summon-surtling.md) and [Summon Wolf](../abilities/summon-wolf.md).
- Not to creatures turned into allies by [Charm](../abilities/charm.md).
- Summons that are already out get the health bonus right away.

??? spoiler "Recipe (spoiler)"

    Craft it at a Galdr table (level 3+).

    | Material | Amount |
    | --- | --- |
    | Thunderstone | 40 |
    | Charred bone | 80 |
    | Morgen heart | 1 |

## Infused Serpent Scale

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Type** | Consumable (permanent effect) |
| **Effect** | +5 armor |
| **Restricted to** | Any demigod |
| **Stack size** | 1 |
| **Consume limit** | Once |
| **Config ID** | `InfusedSerpentScale` |
| **Config section** | `[Attribute Infused Serpent Scale]` |

</div>

<!-- IMAGE: Infused Serpent Scale in the inventory -->

??? spoiler "Recipe (spoiler)"

    Craft it at a Forge (level 3+).

    | Material | Amount |
    | --- | --- |
    | Thunderstone | 10 |
    | Serpent scale | 10 |

## Related pages

- [Infusion Items](infusion-items.md)
- [Demigod Runestone](demigod-runestone.md)
- [Glossary](../reference/glossary.md)

<!-- Verified against NorseDemigods 1.9.1 -->
