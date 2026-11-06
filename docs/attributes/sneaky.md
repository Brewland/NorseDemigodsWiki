# Sneaky

Sneaky is Ullr's own attribute: while sneaking, he is much harder to see and hear, sneaks faster and can shake off
chasing enemies. His knives deal extra Poison damage and stronger sneak attacks, which give him energy.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Demigod** | [Ullr](../demigods/ullr.md) |
| **Condition** | Always active; stealth bonuses while sneaking |
| **Config ID** | `Sneaky` |
| **Config section** | `[Attribute Sneaky]` |

</div>

<!-- IMAGE: in-game screenshot of Ullr sneaking with his translucent stealth look -->

## Sneaking

| Effect | Value |
| --- | --- |
| Visibility to enemies | −70% |
| Noise you make | −50% |
| Sneak speed | +50% |
| Stamina used when sneaking | −40% |
| Sneak skill experience | ×2 (200%) |

- Sneak speed: only while sneaking, and not while encumbered. Sneaking is never faster than jogging, including with
  armor penalties.
- Does not stack with other sneak speed bonuses: the highest one applies.
- Scaled by `[(Special Modifiers)] Special Movement Speed Modifier (%)`.
- **Losing pursuers:** while you sneak, every second, each enemy at least 15 m away that is targeting you has a 20%
  chance to lose track of you.
- Your body turns translucent and your armor is hidden while you sneak. Setting: `[Attribute Sneaky] Enable Visual
  Effects`.

## Knives

| Effect | Value |
| --- | --- |
| Extra damage as *Poison*{.dmg .poison} | +20% |
| Sneak attack bonus | ×1.5 the knife's own bonus |
| Knives skill experience | ×2 (200%) |

## Sneak attacks

- Each sneak attack on an enemy, with any weapon, regenerates 2 energy.

## Related pages

- [Ullr](../demigods/ullr.md)
- [Wolf Speed](wolf-speed.md)

<!-- Verified against NorseDemigods 1.9.2 -->
