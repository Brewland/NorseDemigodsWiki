# Summon Surtling

Summon Surtling calls a surtling that follows Surtr and fights for him for 30 seconds with Fire and Blunt damage. It grows
much stronger with Surtr's level and can give him energy when it hits an enemy.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Surtr](../demigods/surtr.md) |
| **Input** | ++mouse-side-up++ + ++block++ (Ability C) |
| **Energy cost** | 2 |
| **Cooldown** | 60 s |
| **Duration** | 30 s |
| **Config ID** | `Surtling` |
| **Config section** | `[Ability Surtling]` |

</div>

<!-- IMAGE: in-game screenshot of a summoned surtling fighting next to Surtr -->

## Effect

1. A surtling appears about 5 m in front of you.
2. It follows you and attacks your enemies.
3. After 30 s, it disappears.

- Each hit on an enemy: 50% chance to regenerate 1 energy for you.
- It regenerates 5% of its maximum health per second.
- Casting again replaces the current surtling. Setting: `[Ability Surtling] Replace Summons`.
- When 35 m or more away from you, it moves much faster to catch up.
- It disappears 5 s after you log out, and when you teleport or die.

## Stats

Damage and health grow slowly at low levels and sharply at high levels.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Damage per hit | **10**<br><span class="nd-split">7.5 *Fire*{.dmg .fire} + 2.5 *Blunt*{.dmg .blunt}</span> | **59**<br><span class="nd-split">44.25 *Fire*{.dmg .fire} + 14.75 *Blunt*{.dmg .blunt}</span> | **150**<br><span class="nd-split">112.5 *Fire*{.dmg .fire} + 37.5 *Blunt*{.dmg .blunt}</span> |
| Maximum health | 25 | 190 | 500 |

## Infused

- Summons 2 surtlings at once, one on each side of you.

## Limits

- Not usable indoors, such as in dungeons and caves.
- Not usable while swimming.

## Notes

- Bosses deal only 50% damage to summoned companions. Setting: `[Combat] Follower Damage From Boss Modifier (%)`.
- Its Fire damage gives Surtr extra demigod skill experience (see
  [Surtr](../demigods/surtr.md#demigod-skill-experience)).

## Related pages

- [Surtr](../demigods/surtr.md)

<!-- Verified against NorseDemigods 1.9.1 -->
