# Energy Wisp

Energy Wisp summons a glowing wisp that follows Hraesvelgr and lights up his surroundings. Every so often it heals a
badly injured player, attacks the closest enemy with Lightning or mines the rock or ore vein he last hit.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Hraesvelgr](../demigods/hraesvelgr.md) |
| **Input** | ++mouse-side-up++ + ++block++<br>(Ability C) |
| **Energy cost** | None |
| **Cooldown** | 15 s, starts when summoned |
| **Duration** | Until dismissed |
| **Range** | Acts within 20 m of you |
| **Config ID** | `EnergyWisp` |
| **Config section** | `[Ability Energy Wisp]` |

</div>

<!-- IMAGE: in-game screenshot of the Energy Wisp firing a beam at an enemy -->

## Effect

1. Use the ability to summon the wisp. It follows you and lights up everything within 20 m.
2. After resting, it looks for something to do within 20 m of you, in this order:
    1. A friendly player (you first) below 35% health: it heals them.
    2. The closest enemy: it attacks it.
    3. The large rock or ore vein you last hit yourself: it mines it.
3. It acts for up to 5 s, then rests again for 5–15 s (10 s on average).
4. Use the ability again to dismiss it.

- If its target dies early, it switches to a new one of the same kind.
- It does not start a new action after you sprint for 5 s or more, until you stop sprinting for 1 s.
- It stops what it is doing when it gets 55 m or more away from you.
- Indoors (such as in dungeons and caves) it only mines. In-game message when summoned there:
  *"The wisp lacks space..."*
- It comes back by itself after you teleport. It disappears when you die.
- Its attacks and mining make some noise, which can alert enemies.

## Attack

Each second while attacking: 1 base + 0.39 [per level](../reference/glossary.md#per-level).

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Damage per second *Lightning*{.dmg .lightning} | **1** | **20.5** | **40** |

## Healing

- It heals a friendly player whose health is below 35%, until they reach 50% health or 5 s pass.
- You come first; then the player with the lowest health, then the closest one.

Healing per second grows evenly from 5 at level 0 to 10 at level 100.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Healing per second | **5** | **7.5** | **10** |

## Mining

- It only mines the large rock or ore vein you hit last, if your hit damaged it in the last 300 s.
- Each second, it deals *Pickaxe*{.dmg .pickaxe} damage within 2 m of the point it aims at:
  200% of its attack damage.
- [Tool tier](../reference/glossary.md#tool-tier) 1. It ignores veins it cannot mine.
- It also mines the parts of the vein below the ground. Setting: `[Ability Energy Wisp] Mine Ores Below Surface`.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Damage to ores per second *Pickaxe*{.dmg .pickaxe} | **2** | **41** | **80** |

## Infused

- Healing starts below 90% health instead of 35%, and goes on until full health (or 5 s).
- Mining tool tier: 1 → 2.

## Limits

- Usable while airborne or swimming.

## Related pages

- [Hraesvelgr](../demigods/hraesvelgr.md)
- [Glossary](../reference/glossary.md)

<!-- Verified against NorseDemigods 1.9.3 -->
