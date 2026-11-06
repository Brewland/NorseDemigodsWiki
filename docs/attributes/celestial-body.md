# Celestial Body

Celestial Body is Hel's own attribute: armor never slows her down, her weapons deal extra Spirit or Poison damage, her
favorite weapons spread damage and heal her, and her eitr regenerates faster when she wears no heavy armor.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Demigod** | [Hel](../demigods/hel.md) |
| **Condition** | Always active; the eitr regeneration bonus only when not wearing any [heavy armor](../reference/glossary.md#heavy-armor) |
| **Config ID** | `CelestialBody` |
| **Config section** | `[Attribute Celestial Body]` |

</div>

<!-- IMAGE: Celestial Body attribute icon -->

## Armor

- The movement penalty of your helmet, chest and leg armor is ignored.
- Weapons, shields and other equipment still slow you as normal.

## Weapon damage

Extra damage added to your melee weapon hits:

| Weapon | Extra damage |
| --- | ---: |
| Two-handed axes, two-handed swords, polearms and knives | +20% *Spirit*{.dmg .spirit} |
| Other melee weapons (one-handed axes and swords, clubs, spears) | +10% *Poison*{.dmg .poison} |

- Bows, crossbows and unarmed attacks get no extra damage.
- **Splash:** hits with two-handed axes, two-handed swords, polearms or knives also deal **50%** of the hit's damage to
  other enemies within 2 m, half *Spirit*{.dmg .spirit} and half *Poison*{.dmg .poison}.
- **Healing:** these hits heal you for **10%** of the damage dealt (the hit plus the splash), up to **10** health per
  hit.
- Himminafl gets no splash and no healing.

## Resources

| Effect | Value |
| --- | --- |
| Base eitr | +50 |
| Eitr regeneration when not wearing any heavy armor | +50% |

## Related pages

- [Hel](../demigods/hel.md)
- [Phantom Shroud](phantom-shroud.md)
- [Glossary](../reference/glossary.md)

<!-- Verified against NorseDemigods 1.9.2 -->
