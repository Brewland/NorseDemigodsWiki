# Restoration

Restoration is a channeled ability that heals you and restores energy, stamina and eitr while you hold it.
Channel too long and the gathered energy explodes in a large Lightning blast that burns all your energy.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Thor](../demigods/thor.md), [Njord](../demigods/njord.md) |
| **Input** | ++mouse-side-down++ + ++block++<br>(Ability D), hold |
| **Energy cost** | None |
| **Cooldown** | 30 s, starts when activated |
| **Duration** | While held, up to 10 s |
| **Config ID** | `Restoration` |
| **Config section** | `[Ability Restoration]` (shared by all variants) |

</div>

<!-- IMAGE: in-game screenshot of Thor levitating while channeling Restoration -->

Both variants share one config section: a server change affects Thor and Njord alike.

## Effect

Hold the ability key to channel. You cannot move while channeling. Every second:

| Effect | Value |
| --- | --- |
| Health restored | See the level table below |
| Energy restored | 1 |
| Stamina restored | 20% of your maximum |
| Eitr restored | 20% of your maximum |

- After 5 s of channeling, you become Rested for 180 s.
- An existing Rested effect with less than 180 s left is refreshed to 180 s.
- Channeling stops when you release the key or take damage.

## Healing and blast

Healing per second: 10 base + 0.2 [per level](../reference/glossary.md#per-level).

If you channel for the full 10 s, the energy becomes unstable:

- A warning sound plays shortly before the blast.
- The blast hits all enemies within 12 m.
- It **burns all your energy**.
- Blast damage: 20 base + 2.8 per level, then +5% per energy point you have when it explodes.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Healing per second | **10** | **20** | **30** |
| Maximum energy (no bonuses) | 2 | 7 | 12 |
| Blast with 0 energy *Lightning*{.dmg .lightning} | **20** | **160** | **300** |
| Blast with full energy *Lightning*{.dmg .lightning} | **22** | **216** | **480** |

Bonus maximum energy (for example from [Infused Megingjord](../items/infused-megingjord.md)) makes the blast even
stronger.

## Variants

### Lightning (Thor)

- Lightning visual and sound effects.
- The blast deals *Lightning*{.dmg .lightning} damage.

### Water (Njord)

- Water visual and sound effects.
- Same values; the blast also deals *Lightning*{.dmg .lightning} damage.

## Infused

- Removes Poison from you while channeling.
- Not interrupted by damage that is entirely *Poison*{.dmg .poison} or entirely *Fire*{.dmg .fire}.

## Related pages

- [Njord](../demigods/njord.md)
- [Thor](../demigods/thor.md)

<!-- Verified against NorseDemigods 1.9.2 -->
