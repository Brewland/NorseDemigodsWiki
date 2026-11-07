# Combustion

Combustion is Brokkr's airborne special attack: an explosion under his feet that launches him forward, or straight
up if he is not moving. It costs no energy, but the blast is loud enough to attract enemies from far away.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Brokkr](../demigods/brokkr.md) |
| **Input** | ++mouse-middle++<br>(Special attack while airborne) |
| **Energy cost** | None |
| **Cooldown** | 5 s |
| **Config ID** | `Combustion` |
| **Config section** | `[Ability Combustion]` |

</div>

<!-- IMAGE: in-game screenshot of Brokkr launching forward with Combustion -->

## Effect

Jump, then use the special attack while in the air:

| Situation | Launch |
| --- | --- |
| Moving | Forward and slightly up (forward force 50, upward force 10) |
| Not moving | Straight up (upward force 20) |

- Your falling speed is cancelled before the launch.
- The launch counts as a new starting height for fall damage.
- Works with any weapon, or unarmed.

## Infused

- Cooldown: 5 s → 3 s.
- Forward launch force +50%.

## Limits

- Only while airborne.
- Not while sitting, attacking, dodging or staggered.

## Notes

- The explosion makes a lot of noise and alerts enemies far away.

## Related pages

- [Brokkr](../demigods/brokkr.md)
- [Sturdy Legs](../attributes/sturdy-legs.md)

<!-- Verified against NorseDemigods 1.9.3 -->
