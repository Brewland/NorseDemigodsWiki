# Summon Wolf

Summon Wolf calls a loyal wolf companion that stays with you until you dismiss it or it dies. It grows bigger,
healthier and stronger with your demigod skill level, gains stars by fighting and remembers its name between
summons. Fenrir summons an Ulv; Ullr summons a wolf.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Fenrir](../demigods/fenrir.md), [Ullr](../demigods/ullr.md) |
| **Input** | ++mouse-side-up++ + ++block++ (Ability C) |
| **Energy cost** | None |
| **Cooldown** | 50 s |
| **Duration** | Until dismissed or killed |
| **Config ID** | `Wolf` |
| **Config section** | `[Ability Wolf]` (shared by all variants) |

</div>

<!-- IMAGE: in-game screenshot of Fenrir with his summoned Ulv -->

Both variants share one config section: a server change affects Fenrir and Ullr alike.

## Effect

1. You cheer and your companion appears about 5 m in front of you.
2. It follows you, fights your enemies and can be commanded like a tamed creature.
3. Use the ability again to dismiss it.

- Each hit on an enemy: 50% chance to regenerate 1 energy for you.
- It remembers its name, health and feeding between summons.
- Teleporting, dying or logging out dismisses it, just like using the ability again. Summon it again afterwards.
- **If it dies, it is lost for good:** your next summon is a new companion with no stars, no hits and no name.
- It flees when its health is low (30%).
- Hits from bosses deal only 50% damage to it.

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
| Damage per hit | **5** | **31** | **80** |
| Damage per hit when fed (+25%) | **6.25** | **38.75** | **100** |
| Maximum health, no stars | 100 | 1125 | 3000 |
| Maximum health, 2 stars | 150 | 1685 | 4500 |
| Size | 60% | 80% | 100% |

- The size also gets a small fixed bonus on top, which differs between the Ulv and the wolf.

### Feeding

- Feed it like a tamed wolf. While it is fed (happy), it deals **25%** more damage.
- Feeding lasts 3600 s.
- In-game message when it gets hungry again: *"Your wolf is no longer happy"*.

### Stars

- After 40 hits on enemies it gains 1 star; after 100 hits, 2 stars.
- Each star adds 25% maximum health.
- The hit count is kept between summons, but resets to 0 when it dies: it loses its stars.

### Regeneration

- Out of combat: 5% of its maximum health every 5 seconds.
- In combat: 40% of that (2% every 5 seconds).

## Variants

### Ulv (Fenrir)

- Damage: 75% *Slash*{.dmg .slash} + 25% *Pierce*{.dmg .pierce}.
- *Fire*{.dmg .fire} *Frost*{.dmg .frost} Resistant
- *Poison*{.dmg .poison} Weak
- Cannot swim.
- Fenrir gains extra demigod skill experience from its damage (see
  [Fenrir](../demigods/fenrir.md#demigod-skill-experience)).

### Wolf (Ullr)

- Damage: 100% *Slash*{.dmg .slash}.
- *Frost*{.dmg .frost} Resistant
- Has a ghostly look. Setting: `[Ability Wolf] Apply Ghost Effect`.

## Infused

- **5%** of the damage your companion takes is reflected back at the attacker as *Frost*{.dmg .frost} damage.
- Does not work against bosses.

## Limits

- Not usable indoors, such as in dungeons and caves.

## Related pages

- [Fenrir](../demigods/fenrir.md)
- [Ullr](../demigods/ullr.md)
- [Companions](../companions/index.md)

<!-- Verified against NorseDemigods 1.9.1 -->
