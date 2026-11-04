# Whirlwind

Whirlwind is Hraesvelgr's special attack while blocking: he spins in place with his sword or polearm, damaging every
enemy around him and pushing them away.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Hraesvelgr](../demigods/hraesvelgr.md) |
| **Input** | ++block++ + ++mouse-middle++ (Special attack while blocking, swords or polearms) |
| **Energy cost** | 1 |
| **Cooldown** | 10 s |
| **Range** | 4 m around you |
| **Config ID** | `Whirlwind` |
| **Config section** | `[Ability Whirlwind]` |

</div>

<!-- IMAGE: in-game screenshot of Hraesvelgr spinning in a whirlwind -->

## Effect

1. Hold block with a sword or polearm equipped and use the special attack.
2. You spin in place. The spin costs no stamina and deals no damage by itself.
3. 0.4 s later, a whirlwind bursts out: every enemy within 4 m takes damage and is pushed away (push force 150).

- It also hits birds.
- It also hits destructible objects in the area. Objects are not hit while an enemy is within 10 m, or an enemy
  within 6 m of you is targeting you. Setting: `[(General)] Protect Resources From Collateral Damage` (on by default;
  outdoors only).
- Casting is loud and alerts enemies nearby.

## Damage

The whirlwind deals **100%** of your weapon damage (50% *Blunt*{.dmg .blunt} + 50% *Slash*{.dmg .slash}), whatever the
weapon's own damage types.

- The weapon damage is the weapon's listed damage (its quality counts, your skill does not).

## Infused

The whirlwind also deals *Lightning*{.dmg .lightning} damage: 0.5 [per level](../getting-started/glossary.md#per-level),
with no base damage.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Extra damage *Lightning*{.dmg .lightning} | **0** | **25** | **50** |

## Limits

- Not usable while airborne, swimming or sitting.

## Related pages

- [Hraesvelgr](../demigods/hraesvelgr.md)
- [Cleave](cleave.md)

<!-- Verified against NorseDemigods 1.9.1 -->
