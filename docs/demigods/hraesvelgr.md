# Hraesvelgr

Hraesvelgr is an eagle demigod who glides through the air, pulls enemies to him with telekinesis and blasts them with
wind. He favors swords and polearms, and is built to fight in heavy armor.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Role** | A highly mobile eagle demigod that glides through the air, using telekinesis and destructive blasts to eliminate enemies |
| **Element** | *Lightning*{.dmg .lightning} |
| **Favorite weapons** | Swords, polearms |
| **Preferred armor** | Heavy |
| **Config ID** | `Hraesvelgr` |
| **Config section** | `[Demigod Hraesvelgr]` |

</div>

<!-- IMAGE: Hraesvelgr gliding through the air with his passive wind effect -->

!!! note
    This is the default loadout. Servers can change which abilities and attributes each demigod has.

!!! quote "Lore"
    Hraesvelgr is the great giant who sits at the edge of the heavens clad in the guise of a colossal eagle. With every
    mighty beat of his wings, he stirs the freezing currents of air, sending forth the winds that sweep across Midgard.

## Abilities

<div class="grid cards" markdown>

-   :material-weather-windy:{ .lg .middle } [**Cleave**](../abilities/cleave.md)

    ---

    ++mouse-middle++ (Special attack, swords or polearms)

    A blast of air in front of you that pushes enemies away.

-   :material-weather-hurricane:{ .lg .middle } [**Whirlwind**](../abilities/whirlwind.md)

    ---

    ++block++ + ++mouse-middle++ (Special attack while blocking, swords or polearms)

    Spin in place, damaging and pushing away all enemies around you.

-   :material-airplane-takeoff:{ .lg .middle } [**Soar**](../abilities/soar.md)

    ---

    ++mouse-middle++ (Special attack while airborne)

    Launch yourself forward through the air; hold to charge.

-   :material-magnet:{ .lg .middle } [**Telekinesis**](../abilities/telekinesis.md)

    ---

    ++mouse-side-up++ (Ability A)

    Lift an enemy or cart and pull it to you.

-   :material-rotate-orbit:{ .lg .middle } [**Vortex**](../abilities/vortex.md)

    ---

    ++mouse-side-down++ (Ability B)

    Channel a vortex that pulls in objects, then explodes.

-   :material-star-shooting:{ .lg .middle } [**Energy Wisp**](../abilities/energy-wisp.md)

    ---

    ++mouse-side-up++ + ++block++ (Ability C)

    Summon a wisp that heals, attacks enemies and mines ore.

-   :material-shield-airplane:{ .lg .middle } [**Wind Shield**](../abilities/wind-shield.md)

    ---

    ++mouse-side-down++ + ++block++ (Ability D)

    A wind barrier: physical resistance and healing for 10 s.

-   :material-bed:{ .lg .middle } [**Teleport**](../abilities/teleport.md)

    ---

    ++p++ (Teleport)

    Teleport to your bed and back. Shared by all demigods.

</div>

## Attributes

<div class="grid cards" markdown>

-   :material-sword:{ .lg .middle } [**Eagle Agility**](../attributes/eagle-agility.md)

    ---

    Faster attacks with swords and polearms, faster movement.

-   :material-lungs:{ .lg .middle } [**Eagle Endurance**](../attributes/eagle-endurance.md)

    ---

    More stamina, faster stamina regeneration, cheaper attacks.

-   :material-bullseye-arrow:{ .lg .middle } [**Eagle Precision**](../attributes/eagle-precision.md)

    ---

    Pierce splash for swords and polearms, extra Pierce damage, better arrows.

-   :material-compass:{ .lg .middle } [**Eagle Sense**](../attributes/eagle-sense.md)

    ---

    Stand still to see wind trails that lead you home.

-   :material-feather:{ .lg .middle } [**Glide**](../attributes/glide.md)

    ---

    Always fall slowly, with no fall damage.

-   :material-weather-windy-variant:{ .lg .middle } [**Wind Aura**](../attributes/wind-aura.md)

    ---

    Out of combat: faster chopping and mining, speed and stamina.

-   :material-bird:{ .lg .middle } [**Eagle Strength**](../attributes/eagle-strength.md)

    ---

    Less armor slowdown, more carry weight, faster chopping and mining.

    Shared with Eir, Freyja.

-   :material-rabbit:{ .lg .middle } [**Hare Legs**](../attributes/hare-legs.md)

    ---

    Faster movement, a double jump and cheaper sprinting and jumping.

    Shared with Eir, Fenrir, Freyja, Kvasir, Ullr.

</div>

## Demigod skill experience

Hraesvelgr gains demigod skill experience from dealing damage and from being in the air.

| Source | Experience gained |
| --- | --- |
| Damage dealt (any source, e.g. weapons) | 0.75 per 100 damage |
| Time airborne (gliding, soaring, falling) | 0.25% of a level per second |

- Short hops do not count: you must be at least 1 m above the ground you left, or in the air for 1 s.
- Swimming does not count as airborne.

## Infusion

Infusing Hraesvelgr's abilities upgrades all of them at once:

- [Cleave](../abilities/cleave.md#infused): extra Lightning damage.
- [Whirlwind](../abilities/whirlwind.md#infused): extra Lightning damage.
- [Soar](../abilities/soar.md#infused): 5 launches before landing instead of 3.
- [Telekinesis](../abilities/telekinesis.md#infused): longer range, heavier and larger targets.
- [Vortex](../abilities/vortex.md#infused): the explosion also chops trees.
- [Energy Wisp](../abilities/energy-wisp.md#infused): heals up to full health, mines harder ores.
- [Wind Shield](../abilities/wind-shield.md#infused): can be cast on another player.

!!! tip "In-game hint"
    *"You can unlock the true potential of your abilities by crafting and consuming an infused material at a highly
    equipped forge. Scale the freezing peaks to claim the frozen tears of the dragon queen who rules the frost. Nothing
    is infused without Odin's thunderstones."*

??? spoiler "Infusion recipe (spoiler)"

    Craft an **Infused Dragon Tear** at a Forge (level 7+) and consume it.

    - Only Hraesvelgr can consume it.
    - It can be consumed only once.

    | Material | Amount |
    | --- | --- |
    | Thunderstone | 40 |
    | Greydwarf eye | 80 |
    | Dragon tear | 1 |

## Related pages

- [Glossary](../getting-started/glossary.md)

<!-- Verified against NorseDemigods 1.9.1 -->
