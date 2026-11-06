# Sturdy Legs

Sturdy Legs is Brokkr's own attribute: he moves faster, jumps higher, uses much less stamina when sprinting and jumping,
and takes reduced fall damage.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Demigod** | [Brokkr](../demigods/brokkr.md) |
| **Condition** | Always active; no speed bonus while encumbered |
| **Config ID** | `SturdyLegs` |
| **Config section** | `[Attribute Sturdy Legs]` |

</div>

<!-- IMAGE: Sturdy Legs attribute icon -->

## Effects

| Effect | Value |
| --- | --- |
| Movement speed | +10% |
| Jump force | +20% |
| Stamina used when sprinting | −40% |
| Stamina used when jumping | −70% |

## Fall damage

- No fall damage from falls of 12 m or less.
- Above 12 m, fall damage rises to 100 at 20 m or higher.
- Fall damage never takes you below 10 health.

## Notes

- **Movement speed:** applies to walking, jogging, sprinting, sneaking and swimming, but not while encumbered, and
  does not change jump height. Adds up with other movement speed bonuses. Setting:
  `[(Special Modifiers)] Special Movement Speed Modifier (%)`.
- The jump bonus adds up with other movement attributes.
- Unlike [Titan Legs](titan-legs.md), Sturdy Legs has no landing blast.

## Related pages

- [Brokkr](../demigods/brokkr.md)
- [Combustion](../abilities/combustion.md)

<!-- Verified against NorseDemigods 1.9.2 -->
