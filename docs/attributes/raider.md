# Raider

Raider is Njord's own attribute: he attacks faster with polearms and two-handed clubs, fallen enemies may drop coins,
and his ship sails faster with the wind always at its back.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Demigod** | [Njord](../demigods/njord.md) |
| **Condition** | Always active; sailing bonuses while on board a ship |
| **Config ID** | `Raider` |
| **Config section** | `[Attribute Raider]` |

</div>

<!-- IMAGE: Njord sailing a longship with Raider -->

## Attack speed

| Weapon | Attack speed |
| --- | ---: |
| Polearms | +20% |
| Two-handed clubs | +20% |

## Coins

- When an enemy dies within 50 m of you: 40% chance it also drops coins. It doesn't have to be your kill.
- Amount: 1 coin per 20 points of the enemy's maximum health, rounded down. Example: 200 health gives 10 coins.
- If several players with Raider are nearby, only the closest one counts.
- Only creatures that can attack drop coins: nearly all monsters and most wild animals, such as boars, wolves and
  lox. Harmless creatures such as deer and hares never do.
- Tamed creatures and summoned companions never drop coins.

## Sailing

While you are on board a ship:

| Effect | Value |
| --- | --- |
| Sailing speed | +50% |
| Wind | Always from behind the ship |

- It works for the whole ship, whoever steers it. Several players with Raider do not add up.

## Related pages

- [Njord](../demigods/njord.md)

<!-- Verified against NorseDemigods 1.9.3 -->
