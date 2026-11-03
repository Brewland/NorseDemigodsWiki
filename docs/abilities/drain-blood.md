# Drain Blood

Drain Blood burns Surtr's own health to fuel his energy: every second, it turns 15 health into 1 energy until his
energy is full. Infused, it also restores stamina.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Surtr](../demigods/surtr.md) |
| **Input** | ++mouse-side-down++ + ++block++ (Ability D) |
| **Energy cost** | None |
| **Cooldown** | 30 s, starts when activated |
| **Duration** | Until energy is full or stopped |
| **Config ID** | `DrainBlood` |
| **Config section** | `[Ability Drain Blood]` |

</div>

<!-- IMAGE: in-game screenshot of Surtr burning while using Drain Blood -->

## Effect

1. Use it to start; use it again to stop it early.
2. Every second, you lose 15 health and gain 1 energy.
3. It stops by itself when your energy is full, or when your health would drop below 25.

- It cannot be started below 40 health, or with full energy.
- Usable while airborne.

## Infused

- You also regain 35 stamina every second.
- It keeps going until both your energy and your stamina are full, and can be started with full energy if your stamina
  is not full.

## Limits

- Not while encumbered, swimming, attacking, dodging or staggered.

## Related pages

- [Surtr](../demigods/surtr.md)
- [Sacrifice](sacrifice.md)

<!-- Verified against NorseDemigods 1.9.1 -->
