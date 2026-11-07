# Cleave

Cleave is Hraesvelgr's sword and polearm special attack: a blast of air in front of him that deals Blunt damage based
on his weapon and pushes enemies away.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Hraesvelgr](../demigods/hraesvelgr.md) |
| **Input** | ++mouse-middle++<br>(Special attack, swords or polearms) |
| **Energy cost** | 1 |
| **Cooldown** | 5 s |
| **Range** | About 11 m in front of you, 5 m wide |
| **Config ID** | `Cleave` |
| **Config section** | `[Ability Cleave]` |

</div>

<!-- IMAGE: in-game screenshot of Hraesvelgr's air blast pushing enemies back -->

## Effect

1. You swing your weapon in the direction you are looking. The swing hits with **50%** of its normal damage and costs
   no stamina.
2. Shortly after (0.5 s with swords, 0.3 s with polearms), a blast of air bursts forward.
3. Every enemy in the blast takes damage and is pushed away (push force 250).

- It also hits destructible objects in the area. Objects are not hit while an enemy is within 10 m, or an enemy
  within 6 m of you is targeting you. Setting: `[(General)] Protect Resources From Collateral Damage` (on by default;
  outdoors only).
- Casting is loud and alerts enemies nearby.

## Damage

The blast deals **100%** of your weapon damage as *Blunt*{.dmg .blunt}, whatever the weapon's own damage types.

- The weapon damage is the weapon's listed damage (its quality counts, your skill does not).

## Infused

The blast also deals *Lightning*{.dmg .lightning} damage: 0.5 [per level](../reference/glossary.md#per-level),
with no base damage.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Extra damage *Lightning*{.dmg .lightning} | **0** | **25** | **50** |

## Limits

- Not usable while swimming or sitting.
- While airborne, the special attack triggers [Soar](soar.md) instead.

## Related pages

- [Hraesvelgr](../demigods/hraesvelgr.md)
- [Whirlwind](whirlwind.md)

<!-- Verified against NorseDemigods 1.9.3 -->
