# Lightning Aura

Lightning Aura is a toggled buff for Thor that makes him attack and move faster and regenerate stamina. It drains
energy over time instead of costing energy up front.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Thor](../demigods/thor.md) |
| **Input** | ++mouse-side-down++ (Ability B) |
| **Energy cost** | Needs 1+ energy; drains 1 every 4 s |
| **Cooldown** | None |
| **Duration** | Until turned off or out of energy |
| **Config ID** | `LightningAura` |
| **Config section** | `[Ability Lightning Aura]` |

</div>

<!-- IMAGE: in-game screenshot of Thor with Lightning Aura active -->

## Effect

Press once to turn it on, again to turn it off. While active:

| Effect | Value |
| --- | --- |
| Attack speed, two-handed melee weapons | +35% |
| Attack speed, other melee weapons | +15% |
| Movement speed (all movement, including swimming) | +20% |
| Stamina regeneration (not while running) | 10 per second |

- Turns off by itself when your energy reaches 0.
- Turning it off within the first 4 s still costs 1 energy.
- No stamina regeneration while running, swimming or encumbered.
- No speed bonus while encumbered.

## Infused

An electric shield revolves around you while the aura is active:

- *Blunt*{.dmg .blunt} Resistant (unless you are already very resistant or immune).
- *Lightning*{.dmg .lightning} Immune.

## Notes

- While the aura drains energy, [Lightning Strike](lightning-strike.md) cannot regenerate energy.

## Related pages

- [Thor](../demigods/thor.md)
- [Lightning Storm](lightning-storm.md)

<!-- Verified against NorseDemigods 1.9.0 -->
