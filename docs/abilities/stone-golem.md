# Stone Golem

Stone Golem summons a friendly stone golem that follows Brokkr and fights for him for 60 seconds. It grows much
stronger with Brokkr's level and can give him energy when it hits an enemy.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Brokkr](../demigods/brokkr.md) |
| **Input** | ++mouse-side-up++ + ++block++<br>(Ability C) |
| **Energy cost** | 3 |
| **Cooldown** | 120 s |
| **Duration** | 60 s |
| **Config ID** | `ElementalGolem` |
| **Config section** | `[Ability Elemental Golem]` |

</div>

<!-- IMAGE: in-game screenshot of the Stone Golem fighting next to Brokkr -->

## Effect

1. Brokkr cheers and a golem appears about 5 m in front of him.
2. The golem follows you and attacks your enemies.
3. Each hit on an enemy: 50% chance to regenerate 1 energy for you.
4. After 60 s it crumbles.

- Casting again replaces the current golem.
- It regenerates about 1% of its maximum health per second.
- It disappears if it gets 65 m or more away from you, and when you teleport, die or log out.
- When more than 35 m away, it moves much faster to catch up.

## Stats

Damage and health grow slowly at low levels and sharply at high levels.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Damage per hit | **10**<br><span class="nd-split">7.5 *Blunt*{.dmg .blunt} + 2.5 *Pierce*{.dmg .pierce}</span> | **77**<br><span class="nd-split">57.75 *Blunt*{.dmg .blunt} + 19.25 *Pierce*{.dmg .pierce}</span> | **200**<br><span class="nd-split">150 *Blunt*{.dmg .blunt} + 50 *Pierce*{.dmg .pierce}</span> |
| Maximum health | 50 | 735 | 2000 |

Resistances:

- *Blunt*{.dmg .blunt} *Slash*{.dmg .slash} *Pierce*{.dmg .pierce} Resistant
- *Fire*{.dmg .fire} Very resistant
- *Frost*{.dmg .frost} *Lightning*{.dmg .lightning} Weak
- *Poison*{.dmg .poison} Immune

## Infused

- Cooldown: 120 s → 90 s.

## Limits

- Not usable indoors, such as in dungeons and caves.

## Notes

- Bosses deal only 50% damage to summoned companions. Setting: `[Combat] Follower Damage From Boss Modifier (%)`.

## Related pages

- [Brokkr](../demigods/brokkr.md)
- [Companions](../companions/index.md)

<!-- Verified against NorseDemigods 1.9.2 -->
