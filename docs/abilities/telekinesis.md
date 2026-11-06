# Telekinesis

Telekinesis lets Hraesvelgr grab an enemy under his crosshair, lift it into the air and pull it to him, staggering it.
It can also lift a cart and launch it where he aims.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Hraesvelgr](../demigods/hraesvelgr.md) |
| **Input** | ++mouse-side-up++<br>(Ability A) |
| **Energy cost** | 1 |
| **Cooldown** | 1 s |
| **Range** | 30 m |
| **Config ID** | `Telekinesis` |
| **Config section** | `[Ability Telekinesis]` |

</div>

<!-- IMAGE: in-game screenshot of an enemy caught in Telekinesis, floating towards Hraesvelgr -->

## Effect on enemies

1. Aim at an enemy within 30 m and use the ability. A bubble of wind wraps around it.
2. If it stands on the ground, it is lifted 5 m up over 1 s (1 m indoors), then held for 0.5 s.
3. It is pulled to just in front of you over 1.5 s and staggered as the pull starts.
4. When it reaches you: 50% chance to refund the energy spent.

- The enemy cannot move while it is held, and it is alerted.
- An enemy already in the air is pulled straight to you.
- You can hold several enemies at once (one cast per enemy).

## Effect on carts

1. Aim at a cart and use the ability. It is lifted 8 m up over 1 s.
2. It is held in the air for 3 s. Use the ability again during that time to launch it towards your crosshair. The
   second cast is free.
3. Otherwise, it is pulled to you after the 3 s.
4. When it arrives: 70% chance to refund the energy spent.

- The cart takes no damage from impacts while you move it.
- Only one cart at a time, and only while you are not holding an enemy.
- A cart another player is pulling or has open cannot be taken.

## Target limits

| Target | Maximum mass | Maximum size |
| --- | ---: | ---: |
| Enemy | 20 | 3.5 m |
| Cart | 120 | 3.5 m |

- Mass is the game's physics mass, not the carry weight. Size is the larger of the target's height and width.
- Bosses, players and swimming enemies cannot be pulled.
- No energy is spent and no cooldown starts when there is no valid target.

## Infused

| | Normal | Infused |
| --- | ---: | ---: |
| Range | 30 m | 45 m |
| Maximum enemy mass | 20 | 50 |
| Maximum enemy size | 3.5 m | 6.25 m |
| Maximum cart mass | 120 | 250 |
| Maximum cart size | 3.5 m | 6.25 m |

## Limits

- Usable while airborne. Not usable while swimming.

## Notes

- Bosses are not staggered (they cannot be pulled at all).

## Related pages

- [Hraesvelgr](../demigods/hraesvelgr.md)
- [Vortex](vortex.md)

<!-- Verified against NorseDemigods 1.9.2 -->
