# Stone Shield

Stone Shield wraps Brokkr in a short-lived stone shield that makes him resistant to physical damage, heals him, restores
stamina, can restore energy and makes him move faster.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Brokkr](../demigods/brokkr.md) |
| **Input** | ++mouse-side-down++ (Ability B) |
| **Energy cost** | None |
| **Cooldown** | 30 s, starts when activated |
| **Duration** | 5 s |
| **Config ID** | `StoneShield` |
| **Config section** | `[Ability Stone Shield]` |

</div>

<!-- IMAGE: in-game screenshot of Brokkr inside the Stone Shield -->

## Effect

While the shield is up:

| Effect | Value |
| --- | --- |
| *Blunt*{.dmg .blunt} *Slash*{.dmg .slash} *Pierce*{.dmg .pierce} resistance | Resistant (unless you are already very resistant or immune) |
| Health restored per second | See the level table below |
| Stamina restored | 20 per second |
| Chance every second to regenerate 1 energy | 50% |
| Movement speed | +20% |

- No stamina regeneration while sprinting, swimming or encumbered.

## Healing

Healing per second grows evenly from 8 at level 0 to 15 at level 100.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Healing per second | **8** | **11.5** | **15** |

## Infused

- Duration: 5 s → 8 s.

## Notes

- **Movement speed:** applies to walking, jogging, sprinting, sneaking and swimming, but not while encumbered, and
  does not change jump height. Adds up with other movement speed bonuses. Setting:
  `[(Special Modifiers)] Special Movement Speed Modifier (%)`.

## Related pages

- [Brokkr](../demigods/brokkr.md)

<!-- Verified against NorseDemigods 1.9.1 -->
