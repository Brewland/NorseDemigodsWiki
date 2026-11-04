# Hare Legs

Hare Legs makes you faster, lets you jump a second time in mid-air, makes sprinting and jumping cheaper and reduces
fall damage.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Demigods** | [Eir](../demigods/eir.md), [Fenrir](../demigods/fenrir.md), [Freyja](../demigods/freyja.md), [Hraesvelgr](../demigods/hraesvelgr.md), [Kvasir](../demigods/kvasir.md), [Ullr](../demigods/ullr.md) |
| **Condition** | Always active; no speed bonus while encumbered |
| **Config ID** | `HareLegs` |
| **Config section** | `[Attribute Hare Legs]` |

</div>

<!-- IMAGE: Hare Legs attribute icon -->

## Effects

| Effect | Value |
| --- | --- |
| Movement speed | +10% |
| Jump force | +5% |
| Stamina used when sprinting | −40% |
| Stamina used when jumping | −70% |

## Double jump

- Press jump again while in the air to jump a second time.
- Once per jump; landing resets it.
- Not while looking steeply down, or after falling more than 3 m below the highest point of your jump.

## Fall damage

- No fall damage from falls of 12 m or less.
- Above 12 m, fall damage rises to 100 at 20 m or higher.
- Fall damage never takes you below 10 health.

## Notes

- **Movement speed:** applies to walking, jogging, sprinting, sneaking and swimming, but not while encumbered, and
  does not change jump height. Adds up with other movement speed bonuses. Setting:
  `[(Special Modifiers)] Special Movement Speed Modifier (%)`.

## Related pages

- [Eir](../demigods/eir.md)
- [Fenrir](../demigods/fenrir.md)
- [Freyja](../demigods/freyja.md)
- [Hraesvelgr](../demigods/hraesvelgr.md)
- [Kvasir](../demigods/kvasir.md)
- [Ullr](../demigods/ullr.md)
- [Wolf Speed](wolf-speed.md)

<!-- Verified against NorseDemigods 1.9.1 -->
