# Lightning Strike

Lightning Strike is Thor's unarmed special attack: a long-range lightning beam that explodes where it hits. It
costs eitr instead of energy and can give energy back on a hit.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Thor](../demigods/thor.md) |
| **Input** | ++mouse-middle++<br>(Special attack, unarmed) |
| **Eitr cost** | 40 |
| **Energy cost** | None |
| **Cooldown** | None |
| **Range** | 80 m |
| **Explosion radius** | 3 m |
| **Config ID** | `LightningStrike` |
| **Config section** | `[Ability Lightning Strike]` |

</div>

<!-- IMAGE: in-game screenshot of a Lightning Strike beam hitting an enemy -->

## Effect

1. Thor fires a lightning beam from his hand toward your aim point.
2. The beam stops at the first enemy or obstacle, up to 80 m away.
3. It explodes there, damaging all enemies within 3 m.
4. If the explosion damages anything: 70% chance to regenerate 1 energy.

## Damage

10 base + 1.4 [per level](../reference/glossary.md#per-level).

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Explosion damage *Lightning*{.dmg .lightning} | **10** | **80** | **150** |

## Infused

- Eitr cost: 40 → 30.
- When the beam hits an enemy: 70% chance to chain to a second enemy up to 15 m away.
- The chain causes a second explosion with the same damage.
- The second enemy must be at least 4.5 m from the first.

## Notes

- No energy regeneration while an energy-draining ability is active, such as
  [Lightning Aura](lightning-aura.md) or [Lightning Storm](lightning-storm.md).
- Damage from this ability gives Thor extra demigod skill experience
  (see [Thor](../demigods/thor.md#demigod-skill-experience)).

## Related pages

- [Thor](../demigods/thor.md)
- [Lightning Storm](lightning-storm.md)

<!-- Verified against NorseDemigods 1.9.2 -->
