# Titan Arms

Titan Arms is Fenrir's own attribute and the source of his strength: his bare-handed claw attacks are fast, deal
physical and Frost damage, block like a shield and fell trees. In exchange, he cannot use melee weapons or shields.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Demigod** | [Fenrir](../demigods/fenrir.md) |
| **Condition** | Always active; faster without [heavy armor](../reference/glossary.md#heavy-armor) |
| **Config ID** | `TitanArms` |
| **Config section** | `[Attribute Titan Arms]` |

</div>

<!-- IMAGE: Fenrir's frost claws -->

## Claw damage

Bare-handed, Fenrir attacks with natural claws instead of punches. Each hit deals 25% *Blunt*{.dmg .blunt},
25% *Slash*{.dmg .slash} and 50% *Frost*{.dmg .frost} damage.

Damage grows with both skills:

- 4 base + 0.46 [per level](../reference/glossary.md#per-level) of the demigod skill,
- then +0.5% per Unarmed skill level (+50% at Unarmed 100).

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Damage per hit, Unarmed skill 0 | **4** | **27** | **50** |
| Damage per hit, Unarmed skill 100 | **6** | **40.4** | **75** |

## Attack speed

| Situation | Claw attack speed |
| --- | --- |
| No heavy armor | +50% |
| Wearing any heavy armor piece | +20% |

## Blocking

Blocking bare-handed uses your arms as a shield: 1.25 block armor per level (minimum 1).

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Unarmed block armor | 1 | 62.5 | 125 |

- Also applies with fist weapons.
- Parry bonus: ×1.5.

## Felling trees

Bare-handed attacks damage trees. Tree damage and [tool tier](../reference/glossary.md#tool-tier) grow with
the **Unarmed** skill:

| | Unarmed 0 | Unarmed 50 | Unarmed 100 |
| --- | ---: | ---: | ---: |
| Damage to trees *Chop*{.dmg .chop} | 7.5 | 22.5 | 37.5 |

| Unarmed skill | Tool tier | New trees |
| --- | ---: | --- |
| 0–4 | 0 | Beech, pine, fir, Ashlands trees |
| 5–19 | 1 | — |
| 20–34 | 2 | Birch, oak, ancient (swamp) trees |
| 35–49 | 3 | — |
| 50+ | 4 | Yggdrasil shoots |

- In-game message when your tier goes up: *"You can now punch harder trees!"*

## Energy

- 35% chance to regenerate 1 energy when a bare-handed or fist-weapon hit damages an enemy.
- 35% chance to regenerate 1 energy when you block an enemy's attack bare-handed.
- No energy regeneration while an energy-draining ability is active.

## Weapons

- **Melee weapons and shields cannot be equipped.**
- Allowed: fist weapons, bows, crossbows, staffs, pickaxes, the Abyssal Harpoon, the Butcher knife and torches.
- Fist weapons deal **50%** less damage, but their attacks use 50% less stamina.
- Fist weapons that mainly deal *Slash*{.dmg .slash} damage use the claw attack.

## Notes

- Servers can allow melee weapons: `[Attribute Titan Arms] Forbid Melee Weapons`.
- With `[Attribute Titan Arms] Display Natural Claws When Unarmed` = `false`, Fenrir punches instead of clawing, at
  +100% attack speed (+70% with heavy armor).

## Related pages

- [Fenrir](../demigods/fenrir.md)
- [Slash](../abilities/slash.md#frost-fenrir)
- [Enrage](../abilities/enrage.md)

<!-- Verified against NorseDemigods 1.9.1 -->
