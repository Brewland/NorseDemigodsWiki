# Bloody Archer

Bloody Archer is Kvasir's own attribute: his arrows deal extra Spirit damage and bounce to other enemies, full eitr
turns into a burst of true damage, and he shoots and sneaks faster.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Demigod** | [Kvasir](../demigods/kvasir.md) |
| **Condition** | Always active; draw and reload bonuses only without [heavy armor](../getting-started/glossary.md#heavy-armor) |
| **Config ID** | `BloodyArcher` |
| **Config section** | `[Attribute Bloody Archer]` |

</div>

<!-- IMAGE: in-game screenshot of a blood bolt bouncing between enemies -->

## Bows and crossbows

| Effect | Value |
| --- | --- |
| Extra damage as *Spirit*{.dmg .spirit} | +30% |
| Bow draw speed, without heavy armor | +25% |
| Crossbow reload time, without heavy armor | −30% |
| Bows and Crossbows skill experience | ×2 (200%) |

- "Without heavy armor" means no [heavy armor](../getting-started/glossary.md#heavy-armor) piece at all.

## Blood bolt

When an arrow or bolt hits an enemy, a blood bolt jumps from it to the closest other enemy:

1. It jumps to up to **2** other enemies, one after the other.
2. Each jump looks for an enemy within 15 m of the last one hit, with nothing in the way.
3. Each jump deals the arrow's damage, reduced by 30% per jump: **70%** on the first jump, **49%** on the second.

## Eitr burst

When your eitr is full, your next hit on an enemy while you hold a bow or crossbow consumes all of it and deals **2**
extra [true damage](../getting-started/glossary.md#true-damage) per eitr point.

- Example: with 60 full eitr, the hit deals **120** extra true damage and your eitr drops to 0.
- You need some maximum eitr (for example, from eitr food).

## Sneaking

| Effect | Value |
| --- | --- |
| Sneak speed | +25% |
| Stamina used when sneaking | −40% |

- Sneak speed: only while sneaking, and not while encumbered. Sneaking is never faster than jogging, including with
  armor penalties.
- Does not stack with other sneak speed bonuses: the highest one applies.

## Related pages

- [Kvasir](../demigods/kvasir.md)
- [Hunter](hunter.md)

<!-- Verified against NorseDemigods 1.9.1 -->
