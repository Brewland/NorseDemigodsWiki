# Slash

Slash is a special attack that hits every enemy around you with a sweeping slash and also chops trees. Fenrir's version
uses his claws and deals Frost damage; Surtr's version uses his axe or sword and deals Fire damage.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Fenrir](../demigods/fenrir.md), [Surtr](../demigods/surtr.md) |
| **Input** | ++mouse-middle++<br>(Special attack, unarmed for Fenrir; axes or swords for Surtr) |
| **Energy cost** | 1 |
| **Cooldown** | 3 s |
| **Range** | 3.5 m |
| **Config ID** | `Slash` |
| **Config section** | `[Ability Slash]` (shared by all variants) |

</div>

<!-- IMAGE: in-game screenshot of Fenrir's frost Slash hitting enemies -->

Both variants share one config section: a server change affects Fenrir and Surtr alike.

## Effect

1. You slash in the direction you are facing.
2. Every enemy within 3.5 m of a point just in front of you takes damage and is pushed back slightly.
3. Trees, logs and other destructible objects within 2 m take chop damage.

- Your weapon also swings, hitting with **50%** of its normal damage. The swing costs no stamina.
- Usable while airborne.

## Damage

The damage is based on your normal attack, then split into 75% *Slash*{.dmg .slash} and 25% elemental damage:

| Variant | Damage to enemies | Damage to trees *Chop*{.dmg .chop} |
| --- | --- | --- |
| Frost (Fenrir) | **50%** of your [Titan Arms](../attributes/titan-arms.md) damage per second | **500%** of your Titan Arms tree damage |
| Fire (Surtr) | **100%** of your weapon damage | **500%** of your weapon damage |

## Variants

### Frost (Fenrir)

- Damage: 75% *Slash*{.dmg .slash} + 25% *Frost*{.dmg .frost}.
- Uses Fenrir's claws. It scales with both the demigod skill and the Unarmed skill (see
  [Titan Arms](../attributes/titan-arms.md)).
- Wearing any [heavy armor](../reference/glossary.md#heavy-armor) lowers Titan Arms' attack speed, and with it
  the slash damage.
- Tree damage uses Titan Arms' [tool tier](../reference/glossary.md#tool-tier), which grows with your Unarmed
  skill.

Damage with no heavy armor (75% *Slash*{.dmg .slash} + 25% *Frost*{.dmg .frost}):

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Damage, Unarmed skill 0 | **6** | **40.5** | **75** |
| Damage, Unarmed skill 100 | **9** | **60.6** | **112.5** |

Damage to trees depends on the Unarmed skill only:

| | Unarmed 0 | Unarmed 50 | Unarmed 100 |
| --- | ---: | ---: | ---: |
| Damage to trees *Chop*{.dmg .chop} | 37.5 | 112.5 | 187.5 |

### Fire (Surtr)

- Damage: 75% *Slash*{.dmg .slash} + 25% *Fire*{.dmg .fire}.
- Uses the total damage of your equipped axe or sword.
- Tree damage uses tool tier 1.

## Infused

- You heal for **5%** of the total damage dealt to enemies, up to **20** health per slash.

## Related pages

- [Fenrir](../demigods/fenrir.md)
- [Surtr](../demigods/surtr.md)
- [Titan Arms](../attributes/titan-arms.md)

<!-- Verified against NorseDemigods 1.9.1 -->
