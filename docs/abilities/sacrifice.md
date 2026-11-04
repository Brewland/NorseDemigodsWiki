# Sacrifice

Sacrifice turns Hel's minions into energy and health. Without minions, it burns her own health instead, turning 15
health into 1 energy every second.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Hel](../demigods/hel.md) |
| **Input** | ++mouse-side-down++ + ++block++<br>(Ability D) |
| **Energy cost** | None |
| **Cooldown** | 10 s, starts when activated |
| **Duration** | Instant with minions; otherwise until energy is full or stopped |
| **Config ID** | `Sacrifice` |
| **Config section** | `[Ability Sacrifice]` |

</div>

<!-- IMAGE: in-game screenshot of Hel sacrificing her skeletons -->

## Effect

With minions (skeletons or a ghost from [Minions](minions.md)):

1. All your minions are destroyed.
2. You gain 1 energy and 50 health per minion.

Without minions, it works as a toggle:

1. Every second, you lose 15 health and gain 1 energy.
2. It stops by itself when your energy is full, or when your health would drop below 25.
3. Use it again to stop it early.

- Without minions, it cannot be started below 40 health. A lone ghost counts as a minion.
- Energy never goes above your maximum.
- Usable while airborne or swimming.

## Infused

- Each sacrificed skeleton explodes, hitting enemies within 5 m of it. The ghost does not explode.
- Without minions: you also regain 30 eitr every second.

Explosion damage: 2 per type [per level](../reference/glossary.md#per-level), with no base damage.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Explosion damage per skeleton | **0** | **200**<br><span class="nd-split">100 *Blunt*{.dmg .blunt} + 100 *Poison*{.dmg .poison}</span> | **400**<br><span class="nd-split">200 *Blunt*{.dmg .blunt} + 200 *Poison*{.dmg .poison}</span> |

## Related pages

- [Hel](../demigods/hel.md)
- [Minions](minions.md)
- [Drain Blood](drain-blood.md)

<!-- Verified against NorseDemigods 1.9.1 -->
