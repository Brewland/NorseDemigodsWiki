# Poison Cloud

Poison Cloud curses the ground around Freyja: every nearby enemy takes Poison damage, and deathsquitos appear and fight
for her for 30 seconds.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Freyja](../demigods/freyja.md) |
| **Input** | ++mouse-side-down++<br>(Ability B) |
| **Energy cost** | 2 |
| **Cooldown** | 45 s |
| **Duration** | 30 s (deathsquitos) |
| **Range** | 5 m around you |
| **Config ID** | `PoisonCloud` |
| **Config section** | `[Ability Poison Cloud]` |

</div>

<!-- IMAGE: in-game screenshot of the Poison Cloud burst with deathsquitos around Freyja -->

## Effect

1. A poison burst hits every enemy within 5 m of you.
2. 3 deathsquitos appear around you and attack your enemies.
3. After 30 s, they disappear.

- Casting again removes the deathsquitos from the previous cast. Setting: `[Ability Poison Cloud] Replace Summons`.
- The deathsquitos are smaller than wild ones.
- They disappear if they get 55 m or more away from you, and when you teleport, die or log out.

## Damage

Burst: 10 base + 1.9 [per level](../reference/glossary.md#per-level).
Deathsquito hits: the same amount, split 75% *Pierce*{.dmg .pierce} and 25% *Poison*{.dmg .poison}.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Burst damage *Poison*{.dmg .poison} | **10** | **105** | **200** |
| Deathsquito damage per hit | **10**<br><span class="nd-split">7.5 *Pierce*{.dmg .pierce} + 2.5 *Poison*{.dmg .poison}</span> | **105**<br><span class="nd-split">78.75 *Pierce*{.dmg .pierce} + 26.25 *Poison*{.dmg .poison}</span> | **200**<br><span class="nd-split">150 *Pierce*{.dmg .pierce} + 50 *Poison*{.dmg .poison}</span> |

- The deathsquitos keep the health of a wild deathsquito; it does not grow with your level.

## Infused

- Deathsquitos per cast: 3 → 5.

## Limits

- Not usable while airborne or swimming.

## Notes

- Bosses deal only 50% damage to summoned companions. Setting: `[Combat] Follower Damage From Boss Modifier (%)`.

## Related pages

- [Freyja](../demigods/freyja.md)
- [Companions](../companions/index.md)

<!-- Verified against NorseDemigods 1.9.1 -->
