# Lightning Bolt

Lightning Bolt is Njord's unarmed special attack: a fast lightning bolt that explodes on impact with Blunt and Lightning
damage. It costs eitr instead of energy and can give energy back on a hit.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Njord](../demigods/njord.md) |
| **Input** | ++mouse-middle++<br>(Special attack, unarmed) |
| **Eitr cost** | 20 |
| **Energy cost** | None |
| **Cooldown** | None |
| **Explosion radius** | 3 m |
| **Config ID** | `LightningBolt` |
| **Config section** | `[Ability Lightning Bolt]` |

</div>

<!-- IMAGE: in-game screenshot of a Lightning Bolt hitting an enemy -->

## Effect

1. Njord casts a lightning bolt toward your aim point.
2. It explodes where it hits, damaging all enemies within 3 m.
3. If it hits an enemy: 30% chance to regenerate 1 energy.

- The bolt can be blocked and dodged.
- It disappears after 20 s if it hits nothing.

## Damage

5 base + 0.95 [per level](../reference/glossary.md#per-level), split evenly between the two types.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Explosion damage | **5**<br><span class="nd-split">2.5 *Blunt*{.dmg .blunt} + 2.5 *Lightning*{.dmg .lightning}</span> | **52.5**<br><span class="nd-split">26.25 *Blunt*{.dmg .blunt} + 26.25 *Lightning*{.dmg .lightning}</span> | **100**<br><span class="nd-split">50 *Blunt*{.dmg .blunt} + 50 *Lightning*{.dmg .lightning}</span> |

## Infused

- Eitr cost: 20 → 15.

## Notes

- No energy regeneration while an energy-draining ability is active.
- Its Lightning damage gives Njord extra demigod skill experience (see
  [Njord](../demigods/njord.md#demigod-skill-experience)).

## Related pages

- [Njord](../demigods/njord.md)

<!-- Verified against NorseDemigods 1.9.1 -->
