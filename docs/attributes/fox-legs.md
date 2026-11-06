# Fox Legs

Fox Legs is Hel's own attribute: she moves faster, jumps higher, uses less stamina when sprinting and jumping, and takes
reduced fall damage.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Demigod** | [Hel](../demigods/hel.md) |
| **Condition** | Always active; no speed bonus while encumbered |
| **Config ID** | `FoxLegs` |
| **Config section** | `[Attribute Fox Legs]` |

</div>

<!-- IMAGE: Fox Legs attribute icon -->

## Effects

| Effect | Value |
| --- | --- |
| Movement speed | +10% |
| Jump force | +15% |
| Stamina used when sprinting | −40% |
| Stamina used when jumping | −40% |

## Fall damage

- No fall damage from falls of 12 m or less.
- Above 12 m, fall damage rises to 100 at 20 m or higher.
- Fall damage never takes you below 10 health.

## Notes

- **Movement speed:** applies to walking, jogging, sprinting, sneaking and swimming, but not while encumbered, and
  does not change jump height. Adds up with other movement speed bonuses. Setting:
  `[(Special Modifiers)] Special Movement Speed Modifier (%)`.
- The jump bonus adds up with other movement attributes.
- Unlike [Hare Legs](hare-legs.md) and [Titan Legs](titan-legs.md), Fox Legs has no double jump or landing blast.

## Related pages

- [Hel](../demigods/hel.md)

<!-- Verified against NorseDemigods 1.9.2 -->
