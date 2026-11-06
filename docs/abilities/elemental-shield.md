# Elemental Shield

Elemental Shield surrounds you with a shield of three charges that reduces physical damage from every hit, makes you
immune to one element and makes you faster. Eir's holy version blocks Spirit; Surtr's fire version blocks Fire.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Eir](../demigods/eir.md), [Surtr](../demigods/surtr.md) |
| **Input** | ++mouse-side-down++<br>(Ability B) |
| **Energy cost** | 2 |
| **Cooldown** | 15 s |
| **Duration** | Until all 3 charges are used |
| **Config ID** | `ElementalShield` |
| **Config section** | `[Ability Elemental Shield]` (shared by all variants) |

</div>

<!-- IMAGE: in-game screenshot of Eir's holy Elemental Shield -->

Both variants share one config section: a server change affects Eir and Surtr alike.

## Effect

Casting gives you **3 charges** (the maximum). While you have charges:

| Effect | Value |
| --- | --- |
| Physical damage reduction per hit | See the level table below |
| Element immunity | Spirit (Eir) or Fire (Surtr) |
| Health restored | 1 every 2 seconds |
| Movement speed | +10% |

- The reduction applies to each hit after armor and resistances, and only lowers its *Blunt*{.dmg .blunt},
  *Slash*{.dmg .slash} and *Pierce*{.dmg .pierce} part.
- On hits that also deal elemental damage, the physical part is reduced by less than the full amount.
- A charge is used when a melee hit from an enemy deals physical damage of at least 10% of your current health.
- Ranged hits never use a charge.
- The shield ends when the last charge is used. There is no time limit.
- No health regeneration while you are burning, poisoned, frozen, shocked or freezing.

## Damage reduction

2 base + 0.1 [per level](../reference/glossary.md#per-level).

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Damage reduced per hit | 2 | 7 | 12 |

The in-game tooltip and status show this value multiplied by the server's `Difficulty` setting.

## Variants

### Holy (Eir)

- *Spirit*{.dmg .spirit} Immune while you have charges.
- Infused reflection deals half *Fire*{.dmg .fire} and half *Spirit*{.dmg .spirit} damage.

### Fire (Surtr)

- *Fire*{.dmg .fire} Immune while you have charges.
- Infused reflection deals *Fire*{.dmg .fire} damage.

## Infused

While you have charges:

- Every melee hit from an enemy reflects damage back at it: 0.5 per level.
- Eitr restored: 1 per second, also while sprinting or swimming.
- Stamina restored: 2 per second (not while sprinting, swimming or encumbered).
- Like the health regeneration, neither works while you are burning, poisoned, frozen, shocked or freezing.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Reflected damage | **0** | **25** | **50** |

## Limits

- You cannot cast it while you still have 3 charges.

## Notes

- **Movement speed:** applies to walking, jogging, sprinting, sneaking and swimming, but not while encumbered, and
  does not change jump height. Adds up with other movement speed bonuses. Setting:
  `[(Special Modifiers)] Special Movement Speed Modifier (%)`.

## Related pages

- [Eir](../demigods/eir.md)
- [Surtr](../demigods/surtr.md)

<!-- Verified against NorseDemigods 1.9.2 -->
