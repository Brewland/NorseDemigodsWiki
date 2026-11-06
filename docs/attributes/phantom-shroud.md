# Phantom Shroud

Phantom Shroud is Hel's own attribute: after a few seconds out of combat, she wraps herself in darkness that speeds up
her eitr and stamina regeneration and her movement, and halves the physical damage of the first hit she takes.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Demigod** | [Hel](../demigods/hel.md) |
| **Condition** | After 5 s out of combat, only when not wearing any [heavy armor](../reference/glossary.md#heavy-armor) |
| **Config ID** | `PhantomShroud` |
| **Config section** | `[Attribute Phantom Shroud]` |

</div>

<!-- IMAGE: Hel wrapped in the dark mist of Phantom Shroud -->

## Effects

While the shroud is active:

| Effect | Value |
| --- | --- |
| Eitr regeneration | +100% |
| Stamina regeneration | +100% |
| Movement speed | +10% |
| *Blunt*{.dmg .blunt} *Slash*{.dmg .slash} *Pierce*{.dmg .pierce} damage of the first hit taken | −50% |

## How it works

- The shroud forms after 5 s without dealing damage and without being hit by an enemy or another player.
- It ends when you deal damage or are hit. The boiling Ashlands sea also ends it.
- Damage from your abilities counts too, such as [Decay Aura](../abilities/decay-aura.md) hitting enemies.
- Sitting down or wearing any heavy armor removes it. It returns as soon as you stand up or take the armor off, if you
  have been out of combat for 5 s.

## Notes

- **Movement speed:** applies to walking, jogging, sprinting, sneaking and swimming, but not while encumbered, and
  does not change jump height. Adds up with other movement speed bonuses. Setting:
  `[(Special Modifiers)] Special Movement Speed Modifier (%)`.

## Related pages

- [Hel](../demigods/hel.md)
- [Celestial Body](celestial-body.md)
- [Glossary](../reference/glossary.md)

<!-- Verified against NorseDemigods 1.9.2 -->
