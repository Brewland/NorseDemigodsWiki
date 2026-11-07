# Holy Heal

Holy Heal instantly restores a large amount of health to another player under your crosshair, or to yourself if you
are not aiming at an injured player.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Eir](../demigods/eir.md) |
| **Input** | ++mouse-side-up++ + ++block++<br>(Ability C) |
| **Energy cost** | 2 |
| **Cooldown** | 45 s |
| **Range** | 25 m |
| **Config ID** | `HolyHeal` |
| **Config section** | `[Ability Holy Heal]` |

</div>

<!-- IMAGE: in-game screenshot of Eir healing another player -->

## Effect

1. If you aim at an injured, friendly player within 25 m, that player is healed.
2. Otherwise, if you are injured, you heal yourself.
3. If nobody needs healing, nothing happens: no energy is used and no cooldown starts.

## Healing

Healing grows evenly from 50 at level 0 to 300 at level 100.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Healing | **50** | **175** | **300** |

## Infused

- Cooldown: 45 s → 30 s.
- Also removes Burning and Poison from the healed player.

## Notes

- Usable while airborne or swimming.
- Only heals players, not tamed creatures or companions.

## Related pages

- [Eir](../demigods/eir.md)

<!-- Verified against NorseDemigods 1.9.3 -->
