# Holy Strike

Holy Strike is Eir's unarmed special attack: holy fire instantly strikes the enemy under your crosshair with Fire and
Spirit damage. It costs eitr instead of energy and can give energy back on a hit.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Eir](../demigods/eir.md) |
| **Input** | ++mouse-middle++<br>(Special attack, unarmed) |
| **Eitr cost** | 20 |
| **Energy cost** | None |
| **Cooldown** | None |
| **Range** | 20 m |
| **Config ID** | `HolyStrike` |
| **Config section** | `[Ability Holy Strike]` |

</div>

<!-- IMAGE: in-game screenshot of a Holy Strike hitting an enemy -->

## Effect

1. Aim at an enemy within 20 m.
2. Holy fire strikes it instantly. There is no projectile to dodge.
3. 30% chance to regenerate 1 energy.

- The cast animation deals no damage by itself and costs no stamina.

## Damage

5 base + 1.45 [per level](../reference/glossary.md#per-level), split evenly between the two types.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Damage | **5**<br><span class="nd-split">2.5 *Fire*{.dmg .fire} + 2.5 *Spirit*{.dmg .spirit}</span> | **77.5**<br><span class="nd-split">38.75 *Fire*{.dmg .fire} + 38.75 *Spirit*{.dmg .spirit}</span> | **150**<br><span class="nd-split">75 *Fire*{.dmg .fire} + 75 *Spirit*{.dmg .spirit}</span> |

## Infused

- Eitr cost: 20 → 15.

## Limits

- Only works when an enemy is under your crosshair within range. Otherwise nothing happens and no eitr is used.

## Notes

- Usable while airborne or swimming.
- No energy regeneration while an energy-draining ability is active.

## Related pages

- [Eir](../demigods/eir.md)
- [Holy Sun](holy-sun.md)

<!-- Verified against NorseDemigods 1.9.3 -->
