# Wind Shield

Wind Shield wraps Hraesvelgr in a barrier of wind for 10 seconds that makes him resistant to physical damage and heals
him every second. Once infused, he can cast it on another player.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Hraesvelgr](../demigods/hraesvelgr.md) |
| **Input** | ++mouse-side-down++ + ++block++<br>(Ability D) |
| **Energy cost** | 2 |
| **Cooldown** | 25 s, starts when activated |
| **Duration** | 10 s |
| **Config ID** | `WindShield` |
| **Config section** | `[Ability Wind Shield]` |

</div>

<!-- IMAGE: in-game screenshot of Hraesvelgr inside the Wind Shield -->

## Effect

While the shield is up:

| Effect | Value |
| --- | --- |
| *Blunt*{.dmg .blunt} *Slash*{.dmg .slash} *Pierce*{.dmg .pierce} resistance | Resistant (unless you are already very resistant or immune) |
| Health restored per second | See the level table below |

- It cannot be cast while you already have a Wind Shield. No energy is spent and no cooldown starts.

## Healing

Healing per second grows evenly from 2 at level 0 to 7 at level 100.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Healing per second | **2** | **4.5** | **7** |

## Infused

- Aim at a friendly player within 25 m to give them the shield instead. Without a player under your crosshair, you get
  it yourself.
- The ally gets the same resistances, duration and healing.
- Casting it on an ally always costs energy and starts the cooldown, even if they already have a shield.

## Limits

- Usable while airborne or swimming.

## Related pages

- [Hraesvelgr](../demigods/hraesvelgr.md)

<!-- Verified against NorseDemigods 1.9.2 -->
