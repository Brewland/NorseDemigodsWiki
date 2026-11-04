# Sense Creatures

Sense Creatures lets Ullr feel where nearby prey is: for a moment, markers around him point towards every huntable
animal within 70 m.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Ullr](../demigods/ullr.md) |
| **Input** | ++mouse-side-down++<br>(Ability B) |
| **Energy cost** | None |
| **Cooldown** | 3 s |
| **Duration** | 1 s |
| **Range** | 70 m |
| **Config ID** | `SenseCreatures` |
| **Config section** | `[Ability Sense Creatures]` |

</div>

<!-- IMAGE: in-game screenshot of the red markers around Ullr pointing towards prey -->

## Effect

1. Use the ability. For 1 s, a red marker appears around you for each prey animal within 70 m.
2. Each marker sits on the side of the animal's direction. The further away the animal, the smaller its marker.

- Prey: boars, deer, wolves, lox, hares and asksvin (and some creatures from other mods).
- Tamed animals and companions are not shown.
- Servers can change the list: `[Ability Sense Creatures] Prey List`.

## Infused

- Every other hostile creature within 70 m is shown too, with a purple marker.

## Limits

- Usable while airborne or swimming.

## Related pages

- [Ullr](../demigods/ullr.md)
- [Hunter](../attributes/hunter.md)

<!-- Verified against NorseDemigods 1.9.1 -->
