# Fireball

Fireball is Surtr's unarmed special attack: a fireball that explodes on impact with Blunt and Fire damage and also
damages trees. It costs eitr instead of energy and can give energy back on a hit.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Surtr](../demigods/surtr.md) |
| **Input** | ++mouse-middle++<br>(Special attack, unarmed) |
| **Eitr cost** | 20 |
| **Energy cost** | None |
| **Cooldown** | None |
| **Explosion radius** | 3 m |
| **Config ID** | `Fireball` |
| **Config section** | `[Ability Fireball]` |

</div>

<!-- IMAGE: in-game screenshot of Surtr casting a fireball -->

## Effect

1. Surtr casts a fireball toward your aim point, like the Staff of Embers.
2. It explodes where it hits, damaging enemies and trees around it.
3. If it hits an enemy: 30% chance to regenerate 1 energy.

## Damage

5 base + 0.95 [per level](../reference/glossary.md#per-level), split evenly between the two types.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Damage | **5**<br><span class="nd-split">2.5 *Blunt*{.dmg .blunt} + 2.5 *Fire*{.dmg .fire}</span> | **52.5**<br><span class="nd-split">26.25 *Blunt*{.dmg .blunt} + 26.25 *Fire*{.dmg .fire}</span> | **100**<br><span class="nd-split">50 *Blunt*{.dmg .blunt} + 50 *Fire*{.dmg .fire}</span> |
| Damage to trees *Chop*{.dmg .chop} | 50 | 100 | 150 |

- Damage to trees: 50 base + 1 per level. [Tool tier](../reference/glossary.md#tool-tier) 1.

## Infused

- Eitr cost: 20 → 15.

## Notes

- With bare hands, the special attack casts Fireball; with an axe or sword, it uses [Slash](slash.md#fire-surtr).
- No energy regeneration while an energy-draining ability is active.
- Its Fire damage gives Surtr extra demigod skill experience (see
  [Surtr](../demigods/surtr.md#demigod-skill-experience)).

## Related pages

- [Surtr](../demigods/surtr.md)
- [Slash](slash.md)

<!-- Verified against NorseDemigods 1.9.2 -->
