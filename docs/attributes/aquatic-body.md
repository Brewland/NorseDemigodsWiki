# Aquatic Body

Aquatic Body is Njord's own attribute: the nearby sea adds Frost damage to his weapons and spreads it to nearby enemies,
and he swims faster and longer, regains stamina while floating and is not slowed by being wet.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Demigod** | [Njord](../demigods/njord.md) |
| **Condition** | Always active; water effects only while swimming or wet |
| **Config ID** | `AquaticBody` |
| **Config section** | `[Attribute Aquatic Body]` |

</div>

<!-- IMAGE: Aquatic Body attribute icon -->

## Weapon damage

Extra damage added to your weapon hits:

| Weapon | Extra damage *Frost*{.dmg .frost} |
| --- | ---: |
| Bows and crossbows | +10% |
| Axes, swords and polearms | +10% |
| Clubs and spears | +5% |

- Knives and unarmed attacks get no extra damage.
- **Frost splash:** hits with axes, swords or polearms also deal **35%** of the hit's damage as *Frost*{.dmg .frost}
  to other enemies within 2 m. Himminafl gets no splash.

## Water

| Effect | Value |
| --- | --- |
| Swim speed | +50% |
| Stamina used when swimming | −50% |
| Stamina regained while floating without moving | 1 every 0.25 s (4 per second) |
| Stamina regeneration while Wet | +50% |
| Swim skill experience | ×3 (300%) |

- Being Wet no longer slows your health, stamina or eitr regeneration.

## Swim speed

- Only while swimming. Also works while encumbered.
- Does not stack with other swim speed bonuses: the highest one applies.
- Movement speed bonuses apply on top when you are not encumbered.

## Resources

| Effect | Value |
| --- | --- |
| Base eitr | +25 |

## Notes

- [Water Shield](water-shield.md) keeps you Wet while it is active, so the stamina bonus applies the whole time.

## Related pages

- [Njord](../demigods/njord.md)
- [Water Shield](water-shield.md)

<!-- Verified against NorseDemigods 1.9.1 -->
