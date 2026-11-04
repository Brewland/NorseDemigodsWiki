# Minions

Minions raises a skeleton warrior that follows Hel and fights for her. Cast it again to raise up to three skeletons;
they grow much stronger with Hel's level and stay until they die.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Hel](../demigods/hel.md) |
| **Input** | ++mouse-side-up++ + ++block++ (Ability C) |
| **Energy cost** | 1 |
| **Cooldown** | 2 s |
| **Duration** | Until killed |
| **Config ID** | `Minions` |
| **Config section** | `[Ability Minions]` |

</div>

<!-- IMAGE: in-game screenshot of Hel with three summoned skeletons -->

## Effect

1. Hel performs a summoning ritual. You cannot move for 1.5 s.
2. A skeleton rises about 5 m in front of you.
3. It follows you and attacks your enemies.

- Up to 3 skeletons at a time. With 3 active, you cannot cast it again (unless infused).
- Each hit on an enemy: 10% chance to regenerate 1 energy for you.
- Skeletons regenerate 2% of their maximum health per second.
- [Sacrifice](sacrifice.md) turns your minions into energy and health.
- They disappear when you teleport, die or log out.

Distance from you:

| Distance | What happens |
| --- | --- |
| 35 m or more | It runs much faster to catch up |
| 50 m or more | It teleports back to about 30 m from you |
| 55 m or more | It is dismissed |

## Stats

Damage and health grow slowly at low levels and sharply at high levels.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Damage per hit *Slash*{.dmg .slash} | **5** | **44** | **100** |
| Maximum health | 25 | 455 | 1250 |

## Infused

- With 3 skeletons active, cast again to summon a **ghost** as well (one at a time).
- The ghost has the same health as a skeleton and deals double damage.
- The ghost cannot be summoned indoors, such as in dungeons and caves.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Ghost damage per hit *Slash*{.dmg .slash} | **10** | **88** | **200** |

## Limits

- Not usable while airborne or swimming.

## Notes

- Bosses deal only 50% damage to summoned companions. Setting: `[Combat] Follower Damage From Boss Modifier (%)`.
- Damage dealt by your minions gives Hel demigod skill experience (see
  [Hel](../demigods/hel.md#demigod-skill-experience)).

## Related pages

- [Hel](../demigods/hel.md)
- [Sacrifice](sacrifice.md)
- [Companions](../companions/index.md)

<!-- Verified against NorseDemigods 1.9.1 -->
