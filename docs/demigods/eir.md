# Eir

Eir is a holy demigod and healer who heals her allies, protects herself with a holy shield and burns enemies with Fire
and Spirit damage. She favors spears, swords and shields, and fights in heavy or light armor.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Role** | Heals, conjures an elemental shield and even organic matter, bringing light to even the depths of the underworld |
| **Element** | *Spirit*{.dmg .spirit} *Fire*{.dmg .fire} |
| **Favorite weapons** | Spears, swords, shields |
| **Preferred armor** | Heavy and light |
| **Config ID** | `Eir` |
| **Config section** | `[Demigod Eir]` |

</div>

<!-- IMAGE: Eir with a spear and shield and her passive holy aura -->

!!! note
    This is the default loadout. Servers can change which abilities and attributes each demigod has.

!!! quote "Lore"
    Eir is a member of the Ásynjur and the healer among them. Her role with Menglod at Lyfjaberg, the hill of
    healing, confers upon her great powers of medicine and midwifery. As a Valkyrie, she has the gift of healing
    powers for warriors on the battlefield.

## Abilities

<div class="grid cards" markdown>

-   :material-star-four-points:{ .lg .middle } [**Holy Strike**](../abilities/holy-strike.md)

    ---

    ++mouse-middle++ (Special attack, unarmed)

    Instant holy fire on the enemy under your crosshair. Costs eitr.

-   :material-rotate-3d-variant:{ .lg .middle } [**Stagger**](../abilities/stagger.md)

    ---

    ++block++ + ++mouse-middle++ (Special attack while blocking, spears)

    Spin with your spear, staggering all nearby enemies.

-   :material-weather-sunny:{ .lg .middle } [**Holy Sun**](../abilities/holy-sun.md)

    ---

    ++mouse-side-up++ (Ability A)

    Sun beam that burns enemies, trees, rocks and ores.

-   :material-shield-sun:{ .lg .middle } [**Elemental Shield**](../abilities/elemental-shield.md#holy-eir)

    ---

    ++mouse-side-down++ (Ability B)

    Three charges of damage reduction, Spirit immunity and speed.

-   :material-hand-heart:{ .lg .middle } [**Holy Heal**](../abilities/holy-heal.md)

    ---

    ++mouse-side-up++ + ++block++ (Ability C)

    Heal another player or yourself instantly.

-   :material-fish:{ .lg .middle } [**Holy Conjuration**](../abilities/holy-conjuration.md)

    ---

    ++mouse-side-down++ + ++block++ (Ability D)

    Conjure a fish, with a chance of seeds or a queen bee.

-   :material-bed:{ .lg .middle } [**Teleport**](../abilities/teleport.md)

    ---

    ++p++ (Teleport)

    Teleport to your bed and back. Shared by all demigods.

</div>

## Attributes

<div class="grid cards" markdown>

-   :material-white-balance-sunny:{ .lg .middle } [**Holy Body**](../attributes/holy-body.md)

    ---

    Spirit bonus damage and splash, extra health and eitr, Spirit resistance.

-   :material-flare:{ .lg .middle } [**Purity**](../attributes/purity.md)

    ---

    Without heavy armor: more Spirit damage, eitr and eitr regeneration.

-   :material-heart-pulse:{ .lg .middle } [**Deer Endurance**](../attributes/deer-endurance.md)

    ---

    Faster stamina regeneration that starts sooner.

    Shared with Fenrir, Freyja, Kvasir, Ullr.

-   :material-bird:{ .lg .middle } [**Eagle Strength**](../attributes/eagle-strength.md)

    ---

    Less armor slowdown, more carry weight, faster chopping and mining.

    Shared with Freyja, Hraesvelgr.

-   :material-rabbit:{ .lg .middle } [**Hare Legs**](../attributes/hare-legs.md)

    ---

    Faster movement, a double jump and cheaper sprinting and jumping.

    Shared with Fenrir, Freyja, Hraesvelgr, Kvasir, Ullr.

-   :material-shield-sword:{ .lg .middle } [**Valkyrie**](../attributes/valkyrie.md)

    ---

    Stronger shield blocks that restore energy, stronger thrown spears that return.

    Shared with Freyja.

</div>

## Demigod skill experience

Eir gains demigod skill experience from dealing damage and from blocking.

| Source | Experience gained |
| --- | --- |
| Damage blocked (shield or weapon) | 3 per 100 damage |
| Damage dealt (any source, e.g. weapons) | 0.75 per 100 damage |

## Infusion

Infusing Eir's abilities upgrades all of them at once:

- [Holy Strike](../abilities/holy-strike.md#infused): cheaper.
- [Stagger](../abilities/stagger.md#infused): the stagger wave also deals Blunt damage.
- [Holy Sun](../abilities/holy-sun.md#infused): wider beam, burns harder trees and ores.
- [Elemental Shield](../abilities/elemental-shield.md#infused): reflects damage, restores eitr and stamina.
- [Holy Heal](../abilities/holy-heal.md#infused): shorter cooldown, cures Burning and Poison.
- [Holy Conjuration](../abilities/holy-conjuration.md#infused): also conjures 2 Surtling cores.

!!! tip "In-game hint"
    *"You can unlock the true potential of your abilities by crafting and consuming an infused material at a
    modestly upgraded forge. With a touch of lightning, everything else you need can be conjured by your own
    abilities."*

??? spoiler "Infusion recipe (spoiler)"

    Craft an **Infused Honey** at a Forge (level 3+) and consume it.

    - Only Eir can consume it.
    - It can be consumed only once.

    | Material | Amount |
    | --- | --- |
    | Honey | 50 |
    | Hard antler | 15 |
    | Perch | 1 |

## Class quirks

- **Spirit piercing:** when Eir damages an enemy that is immune or very resistant to *Spirit*{.dmg .spirit}, it
  becomes only resistant to Spirit. TODO: verify (whether this already applies to the first hit, and in multiplayer
  when another player's game controls the enemy).

## Related pages

- [Glossary](../getting-started/glossary.md)

<!-- Verified against NorseDemigods 1.9.1 -->
