# Soul Reaper

Soul Reaper is Hel's own attribute: when she kills an enemy, its soul may be reaped, and its body explodes with Blunt
and Poison damage to enemies around it.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Demigod** | [Hel](../demigods/hel.md) |
| **Condition** | Enemies you kill within 40 m of you; at most once every 3 s |
| **Config ID** | `SoulReaper` |
| **Config section** | `[Attribute Soul Reaper]` |

</div>

<!-- IMAGE: a corpse exploding from Soul Reaper -->

## Effect

1. You land the killing blow on an enemy within 40 m of you.
2. 50% chance its body explodes.
3. The explosion hits every enemy within 4 m of the body. It also hits birds.

- At most one explosion every 3 s.
- Kills by your minions do not count.
- The explosion makes noise that alerts nearby enemies.

## Damage

5 base + 0.7 [per level](../getting-started/glossary.md#per-level), split evenly between the two types.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Explosion damage | **5**<br><span class="nd-split">2.5 *Blunt*{.dmg .blunt} + 2.5 *Poison*{.dmg .poison}</span> | **40**<br><span class="nd-split">20 *Blunt*{.dmg .blunt} + 20 *Poison*{.dmg .poison}</span> | **75**<br><span class="nd-split">37.5 *Blunt*{.dmg .blunt} + 37.5 *Poison*{.dmg .poison}</span> |

## Related pages

- [Hel](../demigods/hel.md)

<!-- Verified against NorseDemigods 1.9.1 -->
