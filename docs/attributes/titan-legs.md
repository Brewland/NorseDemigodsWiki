# Titan Legs

Titan Legs makes you faster and lighter on your feet, reduces fall damage, and turns hard landings into a blast
that damages nearby enemies.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Demigods** | [Njord](../demigods/njord.md), [Surtr](../demigods/surtr.md), [Thor](../demigods/thor.md) |
| **Condition** | Always active; no speed bonus while encumbered |
| **Config ID** | `TitanLegs` |
| **Config section** | `[Attribute Titan Legs]` |

</div>

<!-- IMAGE: Titan Legs attribute icon -->

## Effects

| Effect | Value |
| --- | --- |
| Movement speed | +10% |
| Jump force | +15% |
| Stamina used when sprinting | −40% |
| Stamina used when jumping | −40% |
| Landing blast radius | 4 m |

## Landing blast

- Triggers when you land from a fall of about 8 m or more.
- Hits enemies within 4 m and pushes them away.
- Also damages nearby trees, rocks and other destructible objects.
- Does not damage buildings placed by players.

Damage: 10 base + 1.4 [per level](../reference/glossary.md#per-level), scaled from 75% to 125%. Longer falls
and closer enemies take more.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Average damage *Blunt*{.dmg .blunt} | **10** | **80** | **150** |
| Damage range *Blunt*{.dmg .blunt} | **7.5–12.5** | **60–100** | **112.5–187.5** |

Thor's [Dash](../abilities/dash.md#lightning-thor) air dive triggers the blast at maximum force. So does a hard landing
after Njord's or Surtr's [Crush](../abilities/crush.md).

## Fall damage

- No fall damage from falls of 12 m or less.
- Above 12 m, fall damage rises to 100 at 20 m or higher.
- Fall damage never takes you below 10 health.

## Themes

- Njord and Thor: blue theme. Surtr: brown theme.
- Only the landing blast's visual and sound effects differ.

## Notes

- **Movement speed:** applies to walking, jogging, sprinting, sneaking and swimming, but not while encumbered, and
  does not change jump height. Adds up with other movement speed bonuses. Setting:
  `[(Special Modifiers)] Special Movement Speed Modifier (%)`.

## Related pages

- [Njord](../demigods/njord.md)
- [Surtr](../demigods/surtr.md)
- [Thor](../demigods/thor.md)
- [Dash](../abilities/dash.md)
- [Crush](../abilities/crush.md)

<!-- Verified against NorseDemigods 1.9.1 -->
