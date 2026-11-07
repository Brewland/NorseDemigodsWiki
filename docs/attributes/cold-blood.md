# Cold Blood

Cold Blood is Surtr's own attribute: fire he causes himself heals him instead of hurting him, and smoke does not bother
him. In exchange, he is weak to Frost.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Demigod** | [Surtr](../demigods/surtr.md) |
| **Condition** | Always active |
| **Config ID** | `ColdBlood` |
| **Config section** | `[Attribute Cold Blood]` |

</div>

<!-- IMAGE: Surtr healing inside his own Burning Ground -->

## Effects

Fire damage from yourself, from someone who is not your enemy, or from no attacker at all:

- deals you no damage;
- heals you for **50%** of it instead, up to **25** health per hit;
- dries you off (removes Wet).

Fire damage from enemies hurts as normal.

Your own [Burning Ground](../abilities/burning-ground.md) never damages you. While you stand in it, it heals you
this way once per second, based on its Fire damage.

| Effect | Value |
| --- | --- |
| Smoked | Immune |

## Weakness

- *Frost*{.dmg .frost} Weak (unless something else already changes your Frost resistance).

## Related pages

- [Surtr](../demigods/surtr.md)
- [Burning Ground](../abilities/burning-ground.md)
- [Flame Body](flame-body.md)

<!-- Verified against NorseDemigods 1.9.3 -->
