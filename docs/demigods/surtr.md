# Surtr

Surtr is a fire demigod who burns everything around him with his weapons, fireballs, burning ground and summoned
surtlings, and even burns his own blood for energy. He favors axes, swords and polearms, and is built to fight in heavy
armor.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Role** | Burns everything around by using weapons, spells, and even minions |
| **Element** | *Fire*{.dmg .fire} |
| **Favorite weapons** | Axes<br>Swords<br>Polearms |
| **Preferred armor** | Heavy |
| **Config ID** | `Surtr` |
| **Config section** | `[Demigod Surtr]` |

</div>

<!-- IMAGE: Surtr in heavy armor with his passive flame effect -->

!!! note
    This is the default loadout. Servers can change which abilities and attributes each demigod has.

!!! quote "Lore"
    Surtr is a true force of nature, bringing massive destruction and spreading chaos in his path. He cares nothing
    about other living beings, killing his own species and himself in order to destroy all the worlds and every
    other being in fire.

## Abilities

<div class="grid cards" markdown>

-   :material-fire:{ .lg .middle } [**Fireball**](../abilities/fireball.md)

    ---

    ++mouse-middle++<br>(Special attack, unarmed)

    Fireball that explodes on impact and damages trees. Costs eitr.

-   :material-slash-forward:{ .lg .middle } [**Slash**](../abilities/slash.md#fire-surtr)

    ---

    ++mouse-middle++<br>(Special attack, axes or swords)

    Sweep that hits all nearby enemies and chops trees.

-   :material-arrow-collapse-down:{ .lg .middle } [**Crush**](../abilities/crush.md#fire-surtr)

    ---

    ++mouse-middle++<br>(Special attack while airborne)

    Leap and strike from above, landing with a blast.

-   :material-campfire:{ .lg .middle } [**Burning Ground**](../abilities/burning-ground.md)

    ---

    ++mouse-side-up++<br>(Ability A)

    Set the ground around you on fire for 6 s.

-   :material-shield-sun:{ .lg .middle } [**Elemental Shield**](../abilities/elemental-shield.md#fire-surtr)

    ---

    ++mouse-side-down++<br>(Ability B)

    Three charges of damage reduction, Fire immunity and speed.

-   :material-emoticon-devil:{ .lg .middle } [**Summon Surtling**](../abilities/summon-surtling.md)

    ---

    ++mouse-side-up++ + ++block++<br>(Ability C)

    Summon a surtling that fights for you for 30 s.

-   :material-heart-minus:{ .lg .middle } [**Drain Blood**](../abilities/drain-blood.md)

    ---

    ++mouse-side-down++ + ++block++<br>(Ability D)

    Toggle: turn your own health into energy.

-   :material-bed:{ .lg .middle } [**Teleport**](../abilities/teleport.md)

    ---

    ++p++<br>(Teleport)

    Teleport to your bed and back. Shared by all demigods.

</div>

## Attributes

<div class="grid cards" markdown>

-   :material-thermometer-low:{ .lg .middle } [**Cold Blood**](../attributes/cold-blood.md)

    ---

    Your own fire heals you; immune to smoke, weak to Frost.

-   :material-fire-circle:{ .lg .middle } [**Flame Body**](../attributes/flame-body.md)

    ---

    Fire bonus damage and splash, extra eitr and energy, Fire resistance.

-   :material-arm-flex:{ .lg .middle } [**Bear Strength**](../attributes/bear-strength.md)

    ---

    Less armor slowdown, more carry weight, stronger melee hits.

    Shared with Njord, Thor.

-   :material-shoe-print:{ .lg .middle } [**Titan Legs**](../attributes/titan-legs.md)

    ---

    Faster movement, higher jumps and a blast when landing from high up.

    Shared with Njord, Thor.

</div>

## Demigod skill experience

Surtr gains demigod skill experience from dealing and taking damage, with a bonus for Fire damage.

| Source | Experience gained |
| --- | --- |
| *Fire*{.dmg .fire} damage dealt | 0.5 per 100 Fire damage (on top of the row below) |
| Damage dealt (any source, e.g. weapons) | 0.75 per 100 damage |
| *Fire*{.dmg .fire} damage dealt by your surtlings | 0.5 per 100 Fire damage |
| Damage taken | 2 per 100 damage |

## Infusion

Infusing Surtr's abilities upgrades all of them at once:

- [Fireball](../abilities/fireball.md#infused): cheaper.
- [Slash](../abilities/slash.md#infused): heals you for part of the damage dealt.
- [Crush](../abilities/crush.md#infused): shorter cooldown, a Fire explosion on landing.
- [Burning Ground](../abilities/burning-ground.md#infused): a large explosion; removes Poison and Frost from you.
- [Elemental Shield](../abilities/elemental-shield.md#infused): reflects damage, restores eitr and stamina.
- [Summon Surtling](../abilities/summon-surtling.md#infused): two surtlings at once.
- [Drain Blood](../abilities/drain-blood.md#infused): also restores stamina.

!!! tip "In-game hint"
    *"You can unlock the true potential of your abilities by crafting and consuming an infused material at a highly
    equipped forge. Surtling is your soul, and its soul is yours; these creatures like heat. Nothing is infused
    without Odin's thunderstones."*

??? spoiler "Infusion recipe (spoiler)"

    Craft an **Infused Surtling** at a Forge (level 7+) and consume it.

    - Only Surtr can consume it.
    - It can be consumed only once.

    | Material | Amount |
    | --- | --- |
    | Thunderstone | 40 |
    | Surtling core | 30 |
    | Surtling trophy | 1 |

## Class quirks

- **Special attack by weapon:** with bare hands, the special attack casts [Fireball](../abilities/fireball.md); with
  an axe or sword, it uses [Slash](../abilities/slash.md#fire-surtr). In the air, it always uses
  [Crush](../abilities/crush.md#fire-surtr).

## Related pages

- [Infusion Items](../items/infusion-items.md)
- [Glossary](../reference/glossary.md)

<!-- Verified against NorseDemigods 1.9.1 -->
