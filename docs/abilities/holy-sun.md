# Holy Sun

Holy Sun brings a piece of the sun down to the spot you aim at. Its beam burns enemies with Fire and Spirit damage
for a few seconds and also burns down trees and breaks rocks and ores.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Eir](../demigods/eir.md) |
| **Input** | ++mouse-side-up++<br>(Ability A) |
| **Energy cost** | 1 |
| **Cooldown** | 5 s |
| **Duration** | About 3 s |
| **Range** | 25 m |
| **Beam radius** | 3 m |
| **Config ID** | `HolySun` |
| **Config section** | `[Ability Holy Sun]` |

</div>

<!-- IMAGE: in-game screenshot of the Holy Sun beam burning enemies -->

## Effect

1. Aim at a spot within 25 m. A small sun appears high above it.
2. Its beam hits the spot every 0.5 s, from 0.5 s to 3.5 s after casting (7 hits).
3. Each hit damages all enemies within 3 m of the spot, and also birds.
4. Each hit also damages trees, rocks and ores within 3 m.
5. If the beam hits a tar pit in the Plains, the pit's tar slowly burns away for as long as the beam lasts. Every
   player nearby sees the tar go down.

## Damage

Each hit: 2 base + 0.48 [per level](../reference/glossary.md#per-level), split evenly between the two types.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Damage per hit | **2**<br><span class="nd-split">1 *Fire*{.dmg .fire} + 1 *Spirit*{.dmg .spirit}</span> | **26**<br><span class="nd-split">13 *Fire*{.dmg .fire} + 13 *Spirit*{.dmg .spirit}</span> | **50**<br><span class="nd-split">25 *Fire*{.dmg .fire} + 25 *Spirit*{.dmg .spirit}</span> |
| Damage per second | **4** | **52** | **100** |
| Damage to trees and ores per hit *Chop*{.dmg .chop} *Pickaxe*{.dmg .pickaxe} | 50 | 100 | 150 |

- Resource damage: 50 base + 1 per level, per hit.
- [Tool tier](../reference/glossary.md#tool-tier) 1.

## Infused

- Beam radius: 3 m → 4 m; the sun is larger.
- Tool tier 1 → 2: also burns birch, oak and ancient trees and breaks silver and obsidian.
- Burns tar 35% faster.

## Limits

- Not usable indoors, such as in dungeons and caves.
- The spot you aim at must be within 25 m.

## Notes

- **Collateral protection:** trees and ores are not damaged when an enemy is within 10 m of the beam, or when an enemy
  within 6 m of you is targeting you. Setting: `[(General)] Protect Resources From Collateral Damage` (on by
  default; outdoors only).
- **Tar burn speed:** setting `[Ability Holy Sun] Tar Volume Burned (u/s)` (default 15; `0` turns tar burning off).

## Related pages

- [Eir](../demigods/eir.md)
- [Glossary](../reference/glossary.md)

<!-- Verified against NorseDemigods 1.9.3 -->
