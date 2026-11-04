# Kvasir

Kvasir is a blood demigod who warps through space, slashes enemies with knives, charms creatures to fight for him and
heals by killing. He favors bows and knives, and fights best in light armor.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Role** | Once a traveler, teaching and spreading knowledge. Now, there is only darkness, and only blood will satisfy his needs |
| **Element** | *Spirit*{.dmg .spirit} |
| **Favorite weapons** | Bows, knives |
| **Preferred armor** | Light |
| **Config ID** | `Kvasir` |
| **Config section** | `[Demigod Kvasir]` |

</div>

<!-- IMAGE: Kvasir in light armor with a bow and his passive blood effect -->

!!! note
    This is the default loadout. Servers can change which abilities and attributes each demigod has.

!!! quote "Lore"
    Kvasir was extremely wise and traveled far and wide, teaching and spreading knowledge, until the day Fjalar and
    Galar drained him of his blood. Now, Kvasir lives in darkness...

## Abilities

<div class="grid cards" markdown>

-   :material-knife:{ .lg .middle } [**Blood Slash**](../abilities/blood-slash.md)

    ---

    ++mouse-middle++<br>(Special attack, knives or unarmed)

    A wide slash that damages every enemy in front of you.

-   :material-transfer-right:{ .lg .middle } [**Warp**](../abilities/warp.md)

    ---

    ++mouse-side-up++<br>(Ability A)

    Teleport forward. Costs no energy.

-   :material-shield-moon:{ .lg .middle } [**Dark Aura**](../abilities/dark-aura.md)

    ---

    ++mouse-side-down++<br>(Ability B)

    Short aura: physical resistance, stamina and speed.

-   :material-account-heart:{ .lg .middle } [**Charm**](../abilities/charm.md)

    ---

    ++mouse-side-up++ + ++block++<br>(Ability C)

    Turn a creature into a temporary ally, or tame it for good.

-   :material-heart-plus:{ .lg .middle } [**Heal Over Time**](../abilities/heal-over-time.md#blood-kvasir)

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

-   :material-bow-arrow:{ .lg .middle } [**Bloody Archer**](../attributes/bloody-archer.md)

    ---

    Spirit arrows that bounce, an eitr burst, faster shooting and sneaking.

-   :material-treasure-chest:{ .lg .middle } [**Corruption**](../attributes/corruption.md)

    ---

    Cheaper wards that duplicate wood, seeds and fuel in a nearby chest.

-   :material-knife-military:{ .lg .middle } [**Piercing Instincts**](../attributes/piercing-instincts.md)

    ---

    Extra Pierce damage for knives and claws; knives chop and mine.

-   :material-bandage:{ .lg .middle } [**Regenerative Body**](../attributes/regenerative-body.md)

    ---

    Without heavy armor: extra armor, less damage taken; heals Slash wounds.

-   :material-glass-wine:{ .lg .middle } [**Thirsty**](../attributes/thirsty.md)

    ---

    Kills restore health and stamina, and may give energy.

-   :material-heart-pulse:{ .lg .middle } [**Deer Endurance**](../attributes/deer-endurance.md)

    ---

    Faster stamina regeneration that starts sooner.

    Shared with Eir, Fenrir, Freyja, Ullr.

-   :material-rabbit:{ .lg .middle } [**Hare Legs**](../attributes/hare-legs.md)

    ---

    Faster movement, a double jump and cheaper sprinting and jumping.

    Shared with Eir, Fenrir, Freyja, Hraesvelgr, Ullr.

</div>

## Demigod skill experience

Kvasir gains demigod skill experience from dealing damage and from charming creatures.

| Source | Experience gained |
| --- | --- |
| Charming a creature with [Charm](../abilities/charm.md) | 2 per 100 of the creature's maximum health |
| Damage dealt (any source, e.g. weapons) | 1 per 100 damage |

## Infusion

Infusing Kvasir's abilities upgrades all of them at once:

- [Blood Slash](../abilities/blood-slash.md#infused): extra Spirit damage.
- [Warp](../abilities/warp.md#infused): shorter cooldown.
- [Dark Aura](../abilities/dark-aura.md#infused): lasts longer.
- [Charm](../abilities/charm.md#infused): free, shorter cooldown.
- [Heal Over Time](../abilities/heal-over-time.md#infused): removes Burning.

!!! tip "In-game hint"
    *"You can unlock the true potential of your abilities by killing the true king of skeletons. Hildir will know its
    location."*

Kvasir's infusion is not crafted: it comes from a kill.

??? spoiler "Infusion condition (spoiler)"

    Kill **Brenna**, the fire skeleton that guards one of Hildir's chests (vanilla).

    - Kvasir must land the killing blow, or be within 50 m of Brenna when it dies.
    - It happens only once. In-game message when it does: *"You feel more powerful"*.
    - The in-game demigod overview also shows roughly how far Brenna's tomb is from the world spawn, and in which
      direction.

## Class quirks

- **Spirit piercing:** when Kvasir damages an enemy that is immune or very resistant to *Spirit*{.dmg .spirit}, it
  becomes only resistant to Spirit. TODO: verify (whether this already applies to the first hit, and in multiplayer
  when another player's game controls the enemy).

## Related pages

- [Infusion Items](../items/infusion-items.md)
- [Glossary](../reference/glossary.md)

<!-- Verified against NorseDemigods 1.9.1 -->
