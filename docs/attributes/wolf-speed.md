# Wolf Speed

Wolf Speed makes you faster on foot, while sneaking and while swimming, and makes sprinting cheaper. It adds to the
bonuses of leg attributes such as [Hare Legs](hare-legs.md).

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Demigods** | [Fenrir](../demigods/fenrir.md), [Freyja](../demigods/freyja.md), [Ullr](../demigods/ullr.md) |
| **Condition** | Always active; no movement or sneak speed bonus while encumbered |
| **Config ID** | `WolfSpeed` |
| **Config section** | `[Attribute Wolf Speed]` |

</div>

<!-- IMAGE: Wolf Speed attribute icon -->

## Effects

| Effect | Value |
| --- | --- |
| Movement speed | +10% |
| Sneak speed | +50% |
| Swim speed | +25% |
| Stamina used when sprinting | −30% |
| Run skill experience | ×1.5 (150%) |

## Sneak speed

- Only while sneaking, and not while encumbered.
- Sneaking is never faster than jogging, including with armor penalties.
- Does not stack with other sneak speed bonuses: the highest one applies.
- Scaled by `[(Special Modifiers)] Special Movement Speed Modifier (%)`.
- The movement speed bonus applies on top.

## Swim speed

- Only while swimming. Also works while encumbered.
- Does not stack with other swim speed bonuses: the highest one applies.
- Scaled by `[(Special Modifiers)] Special Movement Speed Modifier (%)`.
- The movement speed bonus applies on top when you are not encumbered.

## Notes

- **Movement speed:** applies to walking, jogging, sprinting, sneaking and swimming, but not while encumbered, and
  does not change jump height. Adds up with other movement speed bonuses. Setting:
  `[(Special Modifiers)] Special Movement Speed Modifier (%)`.
- With Hare Legs as well (all three default owners have both), movement speed is +20% and sprinting uses 70% less
  stamina.

## Related pages

- [Fenrir](../demigods/fenrir.md)
- [Freyja](../demigods/freyja.md)
- [Ullr](../demigods/ullr.md)
- [Hare Legs](hare-legs.md)

<!-- Verified against NorseDemigods 1.9.3 -->
