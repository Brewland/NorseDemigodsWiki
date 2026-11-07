# Freyja

Freyja is a nature demigod and Valkyrie who throws poison javelins, curses the ground with poison and calls on
deathsquitos and a helpful wisp. She favors spears, swords and shields, and is built to fight in heavy armor.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Role** | A member of the family of Valkyries. Calls upon nature for help and even a wisp to cultivate crops |
| **Element** | *Poison*{.dmg .poison} |
| **Favorite weapons** | Spears<br>Swords<br>Shields |
| **Preferred armor** | Heavy |
| **Config ID** | `Freyja` |
| **Config section** | `[Demigod Freyja]` |

</div>

<!-- IMAGE: Freyja with a spear and shield and her passive poison aura -->

!!! note
    This is the default loadout. Servers can change which abilities and attributes each demigod has.

!!! quote "Lore"
    Freyja, the most renowned of the Norse goddesses and the most beautiful of the Ásynjur, is famous for her love of
    beauty and fine material possessions. Like the Valkyries, Freyja surveyed the battlefields to find the souls of
    the valiant.

## Abilities

<div class="grid cards" markdown>

-   :material-spear:{ .lg .middle } [**Poison Javelin**](../abilities/poison-javelin.md)

    ---

    ++mouse-middle++<br>(Special attack, unarmed)

    Throw a poison javelin that pierces enemies. Costs eitr.

-   :material-rotate-3d-variant:{ .lg .middle } [**Stagger**](../abilities/stagger.md)

    ---

    ++block++ + ++mouse-middle++<br>(Special attack while blocking, spears)

    Spin with your spear, staggering all nearby enemies.

-   :material-run-fast:{ .lg .middle } [**Dash**](../abilities/dash.md#nature-freyja)

    ---

    ++mouse-side-up++<br>(Ability A)

    Teleport forward, damaging enemies in your path.

-   :material-biohazard:{ .lg .middle } [**Poison Cloud**](../abilities/poison-cloud.md)

    ---

    ++mouse-side-down++<br>(Ability B)

    Poison burst around you that also summons deathsquitos.

-   :material-sprout:{ .lg .middle } [**Nature Wisp**](../abilities/nature-wisp.md)

    ---

    ++mouse-side-up++ + ++block++<br>(Ability C)

    Summon a wisp that catches fish, grows crops and brings wood.

-   :material-heart-plus:{ .lg .middle } [**Heal Over Time**](../abilities/heal-over-time.md#nature-freyja)

    ---

    ++mouse-side-down++ + ++block++<br>(Ability D)

    Heal every second until full health, draining energy.

-   :material-bed:{ .lg .middle } [**Teleport**](../abilities/teleport.md)

    ---

    ++p++<br>(Teleport)

    Teleport to your bed and back. Shared by all demigods.

</div>

## Attributes

<div class="grid cards" markdown>

-   :material-cactus:{ .lg .middle } [**Thorn Body**](../attributes/thorn-body.md)

    ---

    Poison bonus damage and splash, extra health and eitr, energy from trees.

-   :material-heart-pulse:{ .lg .middle } [**Deer Endurance**](../attributes/deer-endurance.md)

    ---

    Faster stamina regeneration that starts sooner.

    Shared with Eir, Fenrir, Kvasir, Ullr.

-   :material-bird:{ .lg .middle } [**Eagle Strength**](../attributes/eagle-strength.md)

    ---

    Less armor slowdown, more carry weight, faster chopping and mining.

    Shared with Eir, Hraesvelgr.

-   :material-rabbit:{ .lg .middle } [**Hare Legs**](../attributes/hare-legs.md)

    ---

    Faster movement, a double jump and cheaper sprinting and jumping.

    Shared with Eir, Fenrir, Hraesvelgr, Kvasir, Ullr.

-   :material-shield-sword:{ .lg .middle } [**Valkyrie**](../attributes/valkyrie.md)

    ---

    Stronger shield blocks that restore energy, stronger thrown spears that return.

    Shared with Eir.

-   :material-speedometer:{ .lg .middle } [**Wolf Speed**](../attributes/wolf-speed.md)

    ---

    Faster movement, sneaking and swimming, cheaper sprinting.

    Shared with Fenrir, Ullr.

</div>

## Demigod skill experience

Freyja gains demigod skill experience from dealing damage and from blocking.

| Source | Experience gained |
| --- | --- |
| Damage blocked (shield or weapon) | 3 per 100 damage |
| Damage dealt (any source, e.g. weapons) | 0.75 per 100 damage |

## Infusion

Infusing Freyja's abilities upgrades all of them at once:

- [Poison Javelin](../abilities/poison-javelin.md#infused): cheaper.
- [Stagger](../abilities/stagger.md#infused): the stagger wave also deals Blunt damage.
- [Dash](../abilities/dash.md#infused): a free second dash.
- [Poison Cloud](../abilities/poison-cloud.md#infused): 5 deathsquitos instead of 3.
- [Nature Wisp](../abilities/nature-wisp.md#infused): a chance of Fine wood.
- [Heal Over Time](../abilities/heal-over-time.md#infused): removes Burning.

!!! tip "In-game hint"
    *"You can unlock the true potential of your abilities by crafting and consuming an infused material at a
    modestly upgraded forge. Can roots and bright green guck give even more life to an ancient seed?"*

??? spoiler "Infusion recipe (spoiler)"

    Craft an **Infused Ancient Seed** at a Forge (level 3+) and consume it.

    - Only Freyja can consume it.
    - It can be consumed only once.

    | Material | Amount |
    | --- | --- |
    | Guck | 150 |
    | Root | 30 |
    | Ancient seed | 1 |

## Class quirks

- **Poison piercing:** Freyja's hits treat enemies that are immune or very resistant to *Poison*{.dmg .poison} as only
  resistant to it, from the first hit, also in multiplayer. Hits from other players and companions are not affected.

## Related pages

- [Ability Infusion Items](../items/ability-infusion-items.md)
- [Glossary](../reference/glossary.md)

<!-- Verified against NorseDemigods 1.9.3 -->
