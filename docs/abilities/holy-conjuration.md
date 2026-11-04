# Holy Conjuration

Holy Conjuration conjures a fish from the biome you are in, with a chance of extra seeds or a queen bee. It costs no
energy but has a long cooldown.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Eir](../demigods/eir.md) |
| **Input** | ++mouse-side-down++ + ++block++<br>(Ability D) |
| **Energy cost** | None |
| **Cooldown** | 300 s |
| **Config ID** | `HolyConjuration` |
| **Config section** | `[Ability Holy Conjuration]` |

</div>

<!-- IMAGE: in-game screenshot of a fish appearing in front of Eir -->

## Effect

1. A fish appears on the ground about 3 m in front of you. Its quality is 2 or 3.
2. 30% chance to also conjure a bonus item for the biome.

| Biome | Fish | Bonus item (30% chance) |
| --- | --- | --- |
| Meadows | Perch | Queen bee (1) |
| Black Forest | Trollfish | Carrot seeds (7) |
| Swamp | Giant herring | Turnip seeds (7) |
| Mountain | Tetra | Onion seeds (7) |
| Plains | Grouper | None |
| Mistlands | Anglerfish | None |
| Ashlands | Magmafish | None |
| Deep North | Northern salmon | None |
| Ocean | Coral cod | None |

TODO: verify (fish names are the vanilla names of the fish the code spawns per biome).

## Infused

- Also conjures **2 Surtling cores** every time.

## Limits

- Not usable while airborne.

## Notes

- Servers can change the bonus item for each biome: `[Ability Holy Conjuration] Special Items List`.

## Related pages

- [Eir](../demigods/eir.md)

<!-- Verified against NorseDemigods 1.9.1 -->
