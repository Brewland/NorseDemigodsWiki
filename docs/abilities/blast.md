# Blast

Blast is a short-range push for Ullr: he thrusts his hand forward and a blast of force hits every enemy in front of him
with Blunt damage, pushing them away.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Ullr](../demigods/ullr.md) |
| **Input** | ++mouse-side-up++<br>(Ability A) |
| **Energy cost** | 1 |
| **Cooldown** | 3 s |
| **Range** | About 11 m in front of you, 5 m wide |
| **Config ID** | `Blast` |
| **Config section** | `[Ability Blast]` |

</div>

<!-- IMAGE: in-game screenshot of Ullr's blast pushing enemies away -->

## Effect

1. You turn in the direction you are looking and thrust your hand forward. Your weapons are put away for a moment.
2. 0.3 s later, the blast hits every enemy in front of you and pushes them away (push force 250).
3. Your weapons come back 0.3 s after the blast.

- If your attack is interrupted before the blast (for example, you are staggered), there is no blast.
- Hiding the weapons can be turned off. Setting: `[Ability Blast] Hide Weapons`.
- It makes some noise, which can alert enemies.

## Damage

5 base + 0.7 [per level](../reference/glossary.md#per-level).

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Damage *Blunt*{.dmg .blunt} | **5** | **40** | **75** |

## Infused

- Push force: +100% (250 → 500).
- Every enemy hit is staggered.

## Limits

- Usable while airborne or swimming. Not usable while sitting.

## Notes

- Bosses are not staggered.

## Related pages

- [Ullr](../demigods/ullr.md)

<!-- Verified against NorseDemigods 1.9.3 -->
