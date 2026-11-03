# Lightning Storm

Lightning Storm is a toggled ability for Thor that calls down lightning on random nearby enemies several times per
second. It drains energy while active and cannot be used indoors.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Thor](../demigods/thor.md) |
| **Input** | ++mouse-side-up++ + ++block++ (Ability C) |
| **Energy cost** | Needs 1+ energy; drains 1 every second |
| **Cooldown** | 10 s, starts when activated |
| **Duration** | Until turned off, out of energy or no enemy in range |
| **Range** | 10 m around you |
| **Config ID** | `LightningStorm` |
| **Config section** | `[Ability Lightning Storm]` |

</div>

<!-- IMAGE: in-game screenshot of Lightning Storm striking a group of enemies -->

## Effect

- Press once to start the storm, again to stop it.
- Lightning strikes **4 times per second**.
- Each strike hits one random enemy within 10 m.

The storm stops by itself when:

- your energy reaches 0, or
- a strike finds no enemy in range.

Stopping it within the first second still costs 1 energy.

## Damage

Each strike: 5 base + 0.45 [per level](../getting-started/glossary.md#per-level).

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Damage per strike *Lightning*{.dmg .lightning} | **5** | **27.5** | **50** |
| Damage per second, 4 strikes *Lightning*{.dmg .lightning} | **20** | **110** | **200** |

- Damage per second assumes every strike hits.
- With several enemies in range, strikes are spread randomly between them.

## Infused

- Each strike: 10% chance to cause an explosion.
- The explosion deals the strike's damage as *Fire*{.dmg .fire} to all enemies within 3 m of the struck enemy.

## Limits

- Not usable indoors, such as in dungeons and caves.
- In-game message: *"Ever heard of a lightning storm inside a cave?"*

## Notes

- While the storm drains energy, [Lightning Strike](lightning-strike.md) cannot regenerate energy.

## Related pages

- [Thor](../demigods/thor.md)
- [Lightning Aura](lightning-aura.md)

<!-- Verified against NorseDemigods 1.9.0 -->
