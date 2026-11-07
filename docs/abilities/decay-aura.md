# Decay Aura

Decay Aura is a toggle that drains the life of up to five nearby enemies with true damage and heals Hel for part of it.
It drains energy while active instead of costing energy up front.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Hel](../demigods/hel.md) |
| **Input** | ++mouse-side-down++<br>(Ability B) |
| **Energy cost** | Needs 1+ energy; drains 1 every 3 s |
| **Cooldown** | None |
| **Duration** | Until turned off or out of energy |
| **Range** | Catches enemies within 10 m; releases them at 15 m |
| **Config ID** | `DecayAura` |
| **Config section** | `[Ability Decay Aura]` |

</div>

<!-- IMAGE: in-game screenshot of Hel draining nearby enemies with Decay Aura -->

## Effect

1. Use it to turn the aura on; use it again to turn it off.
2. Enemies within 10 m are caught by the aura, up to 5 at a time.
3. Every 0.5 s, each caught enemy takes [true damage](../reference/glossary.md#true-damage).
4. An enemy stays caught until it dies or is 15 m or more away from you.
5. You heal for 40% of the total damage dealt, up to 5 health per second.

- It turns off when your energy reaches 0.
- Usable while airborne or swimming.

## Damage and healing

True damage per second, per enemy: 1 base + 0.14 [per level](../reference/glossary.md#per-level).

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| True damage per second, per enemy | **1** | **8** | **15** |
| Healing per second, 1 enemy caught | **0.4** | **3.2** | **5** |
| Healing per second, 5 enemies caught | **2** | **5** | **5** |

## Infused

While the aura damages enemies, you also regain part of the total damage, with no cap:

- Stamina: 30% of the damage.
- Eitr: 20% of the damage.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Stamina per second, 1 enemy caught | 0.3 | 2.4 | 4.5 |
| Eitr per second, 1 enemy caught | 0.2 | 1.6 | 3 |

## Notes

- While it drains energy, chances to regenerate energy on a hit (such as from [Acid Bolt](acid-bolt.md) or
  [Meteor](meteor.md)) do not work.

## Related pages

- [Hel](../demigods/hel.md)
- [Glossary](../reference/glossary.md)

<!-- Verified against NorseDemigods 1.9.3 -->
