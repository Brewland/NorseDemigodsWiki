# Dash

Dash instantly teleports you a short distance forward, damaging every enemy in your path. Thor's version deals
Lightning damage and can dive to the ground from the air; Freyja's version deals Poison damage.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Thor](../demigods/thor.md), Freyja |
| **Input** | ++mouse-side-up++ (Ability A) |
| **Energy cost** | 1 |
| **Cooldown** | 3 s |
| **Range** | 12–18 m, by level |
| **Config ID** | `Dash` |
| **Config section** | `[Ability Dash]` (shared by all variants) |

</div>

<!-- IMAGE: in-game screenshot of Dash with its lightning trail -->

Both variants share one config section: a server change affects Thor and Freyja alike.

## Effect

1. You teleport forward in the direction you are facing.
2. Every enemy along the path takes damage.

## Damage and range

Damage: 10 base + 1.4 [per level](../getting-started/glossary.md#per-level).
Range grows evenly from 12 m to 18 m.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Range | 12 m | 15 m | 18 m |
| Path damage, Thor *Lightning*{.dmg .lightning} | **10** | **80** | **150** |
| Path damage, Freyja *Poison*{.dmg .poison} | **10** | **80** | **150** |

## Variants

### Lightning (Thor)

- Deals *Lightning*{.dmg .lightning} damage.
- **Air dive:** while airborne and looking down, you dash straight to the aimed spot on the ground.
- The spot must be within dash range and at least twice your height away.
- With [Titan Legs](../attributes/movement-and-stamina.md#titan-legs), the dive triggers the landing blast at
  maximum force.

### Nature (Freyja)

- Deals *Poison*{.dmg .poison} damage.
- No air dive.

## Infused

- After a normal dash, you can dash again within 1.5 s.
- The second dash costs no energy and ignores the cooldown.

## Related pages

- [Thor](../demigods/thor.md)
- [Titan Legs](../attributes/movement-and-stamina.md#titan-legs)

<!-- Verified against NorseDemigods 1.9.0 -->
