# Crush

Crush is an airborne special attack: you leap up and forward, then strike from above, and a hard landing triggers
Titan Legs' landing blast at full force. Njord's version has a water and lightning look; Surtr's version sets him on fire.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Njord](../demigods/njord.md), [Surtr](../demigods/surtr.md) |
| **Input** | ++mouse-middle++<br>(Special attack while airborne) |
| **Energy cost** | 1 |
| **Cooldown** | 10 s |
| **Config ID** | `Crush` |
| **Config section** | `[Ability Crush]` (shared by all variants) |

</div>

<!-- IMAGE: in-game screenshot of Surtr crushing enemies from above -->

Both variants share one config section: a server change affects Njord and Surtr alike.

## Effect

1. Jump, then use the special attack while in the air, at least 1 m above the ground.
2. Your falling speed is cancelled and you are pushed up and forward (upward force 7, forward force 5).
3. You strike on the way down with your weapon's special attack. The strike costs no stamina.
4. When you land, [Titan Legs](../attributes/titan-legs.md)' landing blast triggers at maximum force if you were still
   in the attack or falling fast (10 m/s or more).

- While airborne, the special attack always triggers Crush, whatever weapon you hold.
- It cancels slow falling (such as from the Feather cape) and gliding effects.
- Landing in water ends it without a landing blast.
- The strike deals your weapon's normal special-attack damage, but always uses the knife's special-attack animation.
  It gets no sneak-attack bonus.
- With a spear, the strike hits in melee in front of you instead of throwing: the spear stays in your hand and deals
  the same damage as its throw.

## Variants

### Lightning (Njord)

- Water visual effects when you leap.
- The infused landing explosion deals *Lightning*{.dmg .lightning} damage.

### Fire (Surtr)

- You burst into flames during the leap.
- The infused landing explosion deals *Fire*{.dmg .fire} damage.

## Infused

- Cooldown: 10 s → 5 s.
- Landing explosion: every enemy within 5 m of where you land takes damage. It also hits birds.

Explosion damage: 1 [per level](../reference/glossary.md#per-level), with no base damage.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Landing explosion, Njord *Lightning*{.dmg .lightning} | **0** | **50** | **100** |
| Landing explosion, Surtr *Fire*{.dmg .fire} | **0** | **50** | **100** |

## Limits

- Only while airborne, with at least 1 m of open space right below you. Terrain, buildings and ships count as ground.
- A normal standing jump is high enough; a jump with no stamina left is not. Dropping off a ledge or cliff also works.
- Not while encumbered, sitting, attacking, dodging or staggered.

## Related pages

- [Njord](../demigods/njord.md)
- [Surtr](../demigods/surtr.md)
- [Titan Legs](../attributes/titan-legs.md)

<!-- Verified against NorseDemigods 1.9.3 -->
