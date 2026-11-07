# Dark Aura

Dark Aura surrounds Kvasir with a short-lived aura of dark energy that makes him resistant to physical damage, restores
stamina and makes him move faster.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Kvasir](../demigods/kvasir.md) |
| **Input** | ++mouse-side-down++<br>(Ability B) |
| **Energy cost** | 2 |
| **Cooldown** | 30 s, starts when activated |
| **Duration** | 7 s |
| **Config ID** | `DarkAura` |
| **Config section** | `[Ability Dark Aura]` |

</div>

<!-- IMAGE: in-game screenshot of Kvasir inside the Dark Aura -->

## Effect

While the aura is active:

| Effect | Value |
| --- | --- |
| *Blunt*{.dmg .blunt} *Slash*{.dmg .slash} *Pierce*{.dmg .pierce} resistance | Resistant (unless you are already very resistant or immune) |
| Stamina restored | 10 per second |
| Movement speed | +10% |

- No stamina regeneration while sprinting, swimming or encumbered.
- It cannot be turned off early.

## Infused

- Duration: 7 s → 10 s.

## Limits

- Usable while airborne or swimming.

## Notes

- **Movement speed:** applies to walking, jogging, sprinting, sneaking and swimming, but not while encumbered, and
  does not change jump height. Adds up with other movement speed bonuses. Setting:
  `[(Special Modifiers)] Special Movement Speed Modifier (%)`.

## Related pages

- [Kvasir](../demigods/kvasir.md)

<!-- Verified against NorseDemigods 1.9.3 -->
