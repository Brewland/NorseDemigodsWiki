# Fenrir

Fenrir is a frost demigod who fights bare-handed: his claws hit hard enough to fell trees, and his summoned Ulv fights
at his side. He cannot use melee weapons or shields, and fights best in light armor.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Role** | Accompanied by a wolf, lands destructive punches strong enough to bring down trees |
| **Element** | *Frost*{.dmg .frost} |
| **Favorite weapons** | Fists |
| **Preferred armor** | Light |
| **Config ID** | `Fenrir` |
| **Config section** | `[Demigod Fenrir]` |

</div>

<!-- IMAGE: Fenrir with his frost claws and his summoned Ulv -->

!!! note
    This is the default loadout. Servers can change which abilities and attributes each demigod has.

!!! quote "Lore"
    Fenrir, son of the trickster god Loki, has incomparable destructive strength, often likened to that of a titan.
    All the Viking gods, including the god Odin, feared him, so much so that he was nicknamed the titan of the
    apocalypse.

## Abilities

<div class="grid cards" markdown>

-   :material-slash-forward:{ .lg .middle } [**Slash**](../abilities/slash.md#frost-fenrir)

    ---

    ++mouse-middle++<br>(Special attack, unarmed)

    Claw sweep that hits all nearby enemies and chops trees.

-   :material-snowflake:{ .lg .middle } [**Ice Shards**](../abilities/ice-shards.md)

    ---

    ++block++ + ++mouse-middle++<br>(Special attack while blocking, unarmed)

    Fire ice shards from your hands. Costs eitr.

-   :material-emoticon-angry:{ .lg .middle } [**Enrage**](../abilities/enrage.md)

    ---

    ++mouse-side-up++<br>(Ability A)

    Toggle: Spirit bonus and Frost splash on hits, half damage taken.

-   :material-snowflake-variant:{ .lg .middle } [**Frost Nova**](../abilities/frost-nova.md)

    ---

    ++mouse-side-down++<br>(Ability B)

    Frost burst that damages all enemies around you.

-   :material-paw:{ .lg .middle } [**Summon Wolf**](../abilities/summon-wolf.md#ulv-fenrir)

    ---

    ++mouse-side-up++ + ++block++<br>(Ability C)

    Summon your Ulv companion, which grows stronger with you.

-   :material-heart-plus:{ .lg .middle } [**Heal Over Time**](../abilities/heal-over-time.md#frost-fenrir-ullr)

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

-   :material-thermometer-high:{ .lg .middle } [**Boiling Blood**](../attributes/boiling-blood.md)

    ---

    Rest anywhere and regenerate health fast while sitting; weak to Poison.

-   :material-snowman:{ .lg .middle } [**Frost Body**](../attributes/frost-body.md)

    ---

    Extra armor without heavy armor, Frost bonus for bows and staffs, Frost resistance.

-   :material-boxing-glove:{ .lg .middle } [**Titan Arms**](../attributes/titan-arms.md)

    ---

    Fast, strong claw attacks that block and fell trees; no melee weapons.

-   :material-heart-pulse:{ .lg .middle } [**Deer Endurance**](../attributes/deer-endurance.md)

    ---

    Faster stamina regeneration that starts sooner.

    Shared with Eir, Freyja, Kvasir, Ullr.

-   :material-rabbit:{ .lg .middle } [**Hare Legs**](../attributes/hare-legs.md)

    ---

    Faster movement, a double jump and cheaper sprinting and jumping.

    Shared with Eir, Freyja, Hraesvelgr, Kvasir, Ullr.

-   :material-speedometer:{ .lg .middle } [**Wolf Speed**](../attributes/wolf-speed.md)

    ---

    Faster movement, sneaking and swimming, cheaper sprinting.

    Shared with Freyja, Ullr.

</div>

## Demigod skill experience

Fenrir gains demigod skill experience only while unarmed (bare hands or fist weapons), plus from his wolf's damage.

| Source | Experience gained |
| --- | --- |
| Damage dealt while unarmed | 1 per 100 damage |
| Each hit while unarmed | 0.005 per demigod level (0.25 at level 50, 0.5 at level 100) |
| Damage blocked bare-handed | 2 per 100 damage |
| Damage dealt by your summoned wolf | 2 per 100 damage |

- Damage dealt with bows, crossbows or staffs gives no demigod skill experience.
- Fist weapons count as unarmed for damage, but not for blocking.

## Infusion

Infusing Fenrir's abilities upgrades all of them at once:

- [Slash](../abilities/slash.md#infused): heals you for part of the damage dealt.
- [Ice Shards](../abilities/ice-shards.md#infused): cheaper.
- [Enrage](../abilities/enrage.md#infused): a Spirit aura damages nearby enemies.
- [Frost Nova](../abilities/frost-nova.md#infused): staggers enemies.
- [Summon Wolf](../abilities/summon-wolf.md#infused): your wolf reflects Frost damage at attackers.
- [Heal Over Time](../abilities/heal-over-time.md#infused): removes Burning.

!!! tip "In-game hint"
    *"You can unlock the true potential of your abilities by crafting and consuming an infused material at a
    highly equipped forge. Fenring is your flesh, and its flesh is yours; these creatures roam high in the mountains
    at night. Nothing is infused without Odin's thunderstones."*

??? spoiler "Infusion recipe (spoiler)"

    Craft an **Infused Claws** at a Forge (level 7+) and consume it.

    - Only Fenrir can consume it.
    - It can be consumed only once.

    | Material | Amount |
    | --- | --- |
    | Thunderstone | 40 |
    | Wolf claw | 20 |
    | Fenring trophy | 1 |

## Class quirks

- **Unarmed only:** [Titan Arms](../attributes/titan-arms.md) stops Fenrir from equipping melee weapons and shields.
- **Unarmed skill:** it only rises through the mod, not through normal vanilla gains:
    - each unarmed melee hit on an enemy: 0.1, plus 1 per 100 damage;
    - each bare-handed hit on a tree: the same amount.

### Fenris set

In-game hint: *"Your Fenris Set is your best friend after your wolf, lent by your sister Hel."*

The mod changes the Fenris armor set for every player:

| Effect | Value |
| --- | --- |
| Movement speed per piece (except the helmet) | +5% |
| Full set: *Fire*{.dmg .fire} *Slash*{.dmg .slash} | Resistant |
| Full set: *Pierce*{.dmg .pierce} | Slightly resistant |
| Full set: skill bonus | +30 |
| Full set, Fenrir only: armor | +18 |

TODO: verify (the full-set skill bonus is assumed to be the vanilla set's Unarmed bonus).

### Berserkir set

- Full set, Fenrir only: +12 armor. TODO: verify (display name of the set).

## Related pages

- [Infusion Items](../items/infusion-items.md)
- [Titan Arms](../attributes/titan-arms.md)
- [Glossary](../reference/glossary.md)

<!-- Verified against NorseDemigods 1.9.1 -->
