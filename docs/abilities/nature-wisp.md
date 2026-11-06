# Nature Wisp

Nature Wisp summons a wisp that works for Freyja: it catches nearby fish, makes crops grow much faster and brings wood
out of runestones. It stays until you dismiss it.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Freyja](../demigods/freyja.md) |
| **Input** | ++mouse-side-up++ + ++block++<br>(Ability C) |
| **Energy cost** | None |
| **Cooldown** | 30 s, starts when summoned |
| **Duration** | Until dismissed |
| **Range** | Works within 50 m of where it was summoned (fish: 20 m) |
| **Config ID** | `NatureWisp` |
| **Config section** | `[Ability Nature Wisp]` |

</div>

<!-- IMAGE: in-game screenshot of the Nature Wisp hovering over a field of crops -->

## Effect

1. Freyja releases the wisp from her hand. It rises about 5 m above the spot.
2. Every second, it looks for work around that spot, in this order:
    1. Fish swimming within 20 m: it catches them for you.
    2. Growing crops within 50 m: it makes them grow faster.
    3. Runestones within 50 m (the lore stones found in the world): it brings wood out of them.
3. Use the ability again to dismiss it.

- **Wood first:** if you aim at a runestone (its text must be visible) when you summon the wisp, it gathers wood before
  tending crops. Fish still come first.
- The wisp stays where you summoned it. It disappears if you get 100 m or more away from it.
- It disappears when you teleport or die.

## Crops

Every second, the wisp takes a share of a crop's total growth time off its remaining time: 5% base + 0.2%
[per level](../reference/glossary.md#per-level).

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Growth per second | 5% | 15% | 25% |
| Time to grow a freshly planted crop | 20 s | About 7 s | 4 s |

- Only healthy crops that are still growing.

## Wood

Time per piece of wood grows shorter evenly from 5 s at level 0 to 2.5 s at level 100.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Time per piece of wood | 5 s | 3.75 s | 2.5 s |

- The wood drops at the runestone.
- The wisp stops gathering while 500 pieces it brought are still lying on the ground. Setting:
  `[Ability Nature Wisp] Wood Max Count`.

## Infused

- Each time the wisp brings wood: 20% chance of an extra Fine wood.

## Limits

- Not usable while airborne or swimming.

## Related pages

- [Freyja](../demigods/freyja.md)

<!-- Verified against NorseDemigods 1.9.2 -->
