# Heal Over Time

Heal Over Time heals you every second until you are back to full health. It drains energy while active instead of
costing energy up front. Fenrir, Freyja, Kvasir and Ullr each have their own visual theme.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Fenrir](../demigods/fenrir.md), [Freyja](../demigods/freyja.md), [Kvasir](../demigods/kvasir.md), [Ullr](../demigods/ullr.md) |
| **Input** | ++mouse-side-down++ + ++block++<br>(Ability D) |
| **Energy cost** | Needs 1+ energy; drains 1 every second |
| **Cooldown** | None |
| **Duration** | Until full health or out of energy |
| **Config ID** | `HealOverTime` |
| **Config section** | `[Ability Heal Over Time]` (shared by all variants) |

</div>

<!-- IMAGE: in-game screenshot of Fenrir healing with the frost Heal Over Time effect -->

All variants share one config section: a server change affects every demigod that has it.

## Effect

1. Use it while injured. It cannot be used at full health.
2. Every second, you are healed and 1 energy is drained.
3. It stops by itself when your health is full or your energy reaches 0.

- It cannot be turned off early.

## Healing

Healing per second grows evenly from 15 at level 0 to 30 at level 100.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Healing per second | **15** | **22.5** | **30** |

## Variants

All variants have the same values; only the visual and sound effects differ.

### Frost (Fenrir, Ullr)

- Frost visual effects.

### Nature (Freyja)

- Nature visual and sound effects.

### Blood (Kvasir)

- Blood visual and sound effects.

## Infused

- Removes Burning from you every second while active.

## Notes

- While it drains energy, most chances to regenerate energy on a hit (such as from [Titan Arms](../attributes/titan-arms.md)
  or [Ice Shards](ice-shards.md)) do not work.

## Related pages

- [Fenrir](../demigods/fenrir.md)
- [Freyja](../demigods/freyja.md)
- [Kvasir](../demigods/kvasir.md)
- [Ullr](../demigods/ullr.md)

<!-- Verified against NorseDemigods 1.9.3 -->
