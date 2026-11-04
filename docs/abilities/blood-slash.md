# Blood Slash

Blood Slash is Kvasir's knife and unarmed special attack: a wide slash that damages every enemy in front of him with
Slash damage that grows with his level.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Kvasir](../demigods/kvasir.md) |
| **Input** | ++mouse-middle++<br>(Special attack, knives or unarmed) |
| **Energy cost** | 1 |
| **Cooldown** | 3 s |
| **Range** | 9 m in front of you, 6 m wide |
| **Config ID** | `BloodSlash` |
| **Config section** | `[Ability Blood Slash]` |

</div>

<!-- IMAGE: in-game screenshot of Kvasir's blood slash hitting several enemies -->

## Effect

1. You slash in the direction you are looking.
2. Every enemy in an area 9 m long, 6 m wide and 4 m high in front of you takes damage and is pushed back slightly.
3. Your weapon also swings, hitting with **50%** of its normal damage. The swing costs no stamina.

- It also hits destructible objects in the area.

## Damage

5 base + 0.7 [per level](../reference/glossary.md#per-level).

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Damage *Slash*{.dmg .slash} | **5** | **40** | **75** |

- The damage does not depend on your weapon.

## Infused

The slash also deals **20%** of its damage as *Spirit*{.dmg .spirit}.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Total damage | **6**<br><span class="nd-split">5 *Slash*{.dmg .slash} + 1 *Spirit*{.dmg .spirit}</span> | **48**<br><span class="nd-split">40 *Slash*{.dmg .slash} + 8 *Spirit*{.dmg .spirit}</span> | **90**<br><span class="nd-split">75 *Slash*{.dmg .slash} + 15 *Spirit*{.dmg .spirit}</span> |

## Limits

- Usable while airborne. Not usable while swimming or sitting.

## Related pages

- [Kvasir](../demigods/kvasir.md)
- [Piercing Instincts](../attributes/piercing-instincts.md)

<!-- Verified against NorseDemigods 1.9.1 -->
