# Neck

Neck summons a friendly neck that gathers resources for Njord: it catches fish for him and chops logs, trees and
bushes. It does not fight, and stays until you dismiss it or it dies.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Njord](../demigods/njord.md) |
| **Input** | ++mouse-side-up++ + ++block++ (Ability C) |
| **Energy cost** | None |
| **Cooldown** | 30 s, starts when summoned |
| **Duration** | Until dismissed or killed |
| **Range** | Works within 50 m of you |
| **Config ID** | `Neck` |
| **Config section** | `[Ability Neck]` |

</div>

<!-- IMAGE: in-game screenshot of Njord's ghostly neck chopping a tree -->

## Effect

1. A neck appears about 3 m in front of you.
2. It goes to the closest resource within 50 m of you that it can work on:
    - fish swimming in the water: it catches them for you;
    - logs, trees, small trees, bushes and stumps: it chops them.
3. With nothing to do, it follows you.
4. Use the ability again to dismiss it.

- It hits once per second.
- It ignores enemies and does not fight.
- It regenerates 5% of its maximum health per second.
- It is immune to heat (lava and the hot Ashlands sea) and takes no damage from falling trees.
- It has a ghostly look. Setting: `[Ability Neck] Apply Ghost Effect`.
- It disappears when you teleport, die or log out.
- **If enabled:** with `[Ability Neck] Flee From Enemies` = `true`, it flees from enemies instead of ignoring them.

## Stats

Damage grows evenly with level; health grows slowly at low levels and sharply at high levels.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Damage per hit *Chop*{.dmg .chop} | 10 | 20 | 30 |
| Maximum health | 20 | 80 | 200 |

- [Tool tier](../getting-started/glossary.md#tool-tier) 0: beech, pine, fir and Ashlands trees.
- Servers can change which bushes and small objects it chops: `[Ability Neck] Destructibles List`.

## Infused

- Summons 2 necks instead of 1, one on each side of you. Two necks never work on the same resource.
- Tool tier 0 → 5: they can chop every tree, including birch, oak, ancient trees and Yggdrasil shoots.

## Limits

- Not usable indoors, such as in dungeons and caves.

## Notes

- Bosses deal only 50% damage to summoned companions. Setting: `[Combat] Follower Damage From Boss Modifier (%)`.

## Related pages

- [Njord](../demigods/njord.md)
- [Glossary](../getting-started/glossary.md)
- [Companions](../companions/index.md)

<!-- Verified against NorseDemigods 1.9.1 -->
