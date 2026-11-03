# Lightning Torpedo

Lightning Torpedo is Brokkr's unarmed special attack: a homing torpedo that rises, locks onto an enemy and explodes
on impact with Blunt and Lightning damage. It costs eitr instead of energy and can give energy back on a hit.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Brokkr](../demigods/brokkr.md) |
| **Input** | ++mouse-middle++ (Special attack, unarmed) |
| **Eitr cost** | 20 |
| **Energy cost** | None |
| **Cooldown** | None |
| **Range** | Seeks enemies within 40 m |
| **Explosion radius** | 3 m |
| **Config ID** | `LightningTorpedo` |
| **Config section** | `[Ability Lightning Torpedo]` |

</div>

<!-- IMAGE: in-game screenshot of a Lightning Torpedo curving toward an enemy -->

## Effect

1. Brokkr launches a torpedo from his hand, straight up.
2. If you aim at an enemy within 40 m, the torpedo targets that enemy.
3. Otherwise it targets the **furthest** enemy within 40 m that it can see.
4. It turns toward its target and explodes on impact, damaging all enemies within 3 m.
5. If it hits an enemy: 30% chance to regenerate 1 energy.

- The torpedo can be blocked and dodged.
- It disappears after 20 s if it hits nothing.

## Damage

10 base + 0.9 [per level](../getting-started/glossary.md#per-level), split evenly between the two types.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Explosion damage | **10**<br><span class="nd-split">5 *Blunt*{.dmg .blunt} + 5 *Lightning*{.dmg .lightning}</span> | **55**<br><span class="nd-split">27.5 *Blunt*{.dmg .blunt} + 27.5 *Lightning*{.dmg .lightning}</span> | **100**<br><span class="nd-split">50 *Blunt*{.dmg .blunt} + 50 *Lightning*{.dmg .lightning}</span> |

## Infused

- Eitr cost: 20 → 15.
- The torpedo turns faster toward its target.
- It targets the **closest** enemy instead of the furthest.

## Notes

- No energy regeneration while an energy-draining ability is active.
- Sneak attacks deal ×4 damage.

## Related pages

- [Brokkr](../demigods/brokkr.md)
- [Combustion](combustion.md)

<!-- Verified against NorseDemigods 1.9.1 -->
