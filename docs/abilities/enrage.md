# Enrage

Enrage is a toggled buff for Fenrir: his bare-handed hits deal extra Spirit damage and spread Frost damage to nearby
enemies, and he takes half damage from every source. It drains energy while active.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Fenrir](../demigods/fenrir.md) |
| **Input** | ++mouse-side-up++<br>(Ability A) |
| **Energy cost** | Needs 1+ energy; drains 1 every 2 s |
| **Cooldown** | None |
| **Duration** | Until turned off or out of energy |
| **Config ID** | `Enraged` |
| **Config section** | `[Ability Enraged]` |

</div>

<!-- IMAGE: in-game screenshot of Fenrir with the Enrage frost aura -->

## Effect

Press once to turn it on, again to turn it off. While active:

| Effect | Value |
| --- | --- |
| Extra damage on bare-handed melee hits *Spirit*{.dmg .spirit} | +50% of the hit's damage |
| Splash to other enemies within 3 m *Frost*{.dmg .frost} | **50%** of the hit's damage |
| Damage taken (all types) | −50% |
| Stamina regeneration | 5 per second |

- The bonus and splash apply to bare hands only, not fist weapons.
- Enemies that are immune or very resistant to *Spirit*{.dmg .spirit} become only resistant to it when you hit them.
- Turns off by itself when your energy reaches 0.
- Turning it off within the first 2 s still costs 1 energy.
- No stamina regeneration while sprinting, swimming or encumbered.

## Infused

A spirit aura damages all enemies within 5 m every second: 0.25 per level.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Aura damage per second *Spirit*{.dmg .spirit} | **0** | **12.5** | **25** |

## Notes

- Usable while airborne or swimming.
- While Enrage drains energy, most chances to regenerate energy on a hit (such as from [Titan Arms](../attributes/titan-arms.md)
  or [Ice Shards](ice-shards.md)) do not work.

## Related pages

- [Fenrir](../demigods/fenrir.md)
- [Titan Arms](../attributes/titan-arms.md)

<!-- Verified against NorseDemigods 1.9.1 -->
