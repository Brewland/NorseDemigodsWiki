# Companions

Several demigods can summon creatures that follow them and fight, or gather resources, for them. This page compares
every companion and lists the rules they share; each ability page has the full details.

<!-- IMAGE: several summoned companions (stone golem, wolf, skeletons) fighting next to their demigods -->

## Overview

<div class="nd-overview" markdown>

| Companion | Ability | Demigod | Job | How many | Lasts |
| --- | --- | --- | --- | --- | --- |
| Charmed creature | [Charm](../abilities/charm.md) | [Kvasir](../demigods/kvasir.md) | Fights | No limit | 15–30 s, by level |
| Deathsquito | [Poison Cloud](../abilities/poison-cloud.md) | [Freyja](../demigods/freyja.md) | Fights | 3 (5 infused) | 30 s |
| Ghost | [Minions](../abilities/minions.md#infused), infused | [Hel](../demigods/hel.md) | Fights | 1, once 3 skeletons are out | Until killed |
| Neck | [Neck](../abilities/neck.md) | [Njord](../demigods/njord.md) | Catches fish, chops wood | 1 (2 infused) | Until dismissed or killed |
| Skeleton | [Minions](../abilities/minions.md) | [Hel](../demigods/hel.md) | Fights | Up to 3 | Until killed |
| Stone golem | [Stone Golem](../abilities/stone-golem.md) | [Brokkr](../demigods/brokkr.md) | Fights | 1 | 60 s |
| Surtling | [Summon Surtling](../abilities/summon-surtling.md) | [Surtr](../demigods/surtr.md) | Fights | 1 (2 infused) | 30 s |
| Ulv | [Summon Wolf](../abilities/summon-wolf.md#ulv-fenrir) | [Fenrir](../demigods/fenrir.md) | Fights | 1 | Until dismissed or killed |
| Wolf | [Summon Wolf](../abilities/summon-wolf.md#wolf-ullr) | [Ullr](../demigods/ullr.md) | Fights | 1 | Until dismissed or killed |

</div>

## How companions work

- Companions follow you and attack your enemies. Deathsquitos and charmed creatures do not follow you: they attack
  enemies nearby.
- The neck never fights: it catches fish and chops wood near you.
- All companions disappear when you teleport, die or log out, and all charms end.
- Damage and health are set when you summon the companion: a level gained counts from your next summon. Your wolf is
  the exception: it grows stronger as soon as you level up.
- Bosses deal only 50% damage to summoned companions. Setting: `[Combat] Follower Damage From Boss Modifier (%)`.
  Charmed creatures take full damage from bosses.
- Charmed creatures keep their own damage and health. When the charm ends, they go back to their own side.

### Summon Wolf is different

- Your Ulv or wolf has a name and can be commanded like a tamed creature.
- Dismissing it, teleporting, dying, logging out or leaving it too far behind keeps its name, health, feeding and
  stars for the next summon.
- If it dies, it is lost for good: your next summon is a new companion with no stars.
- Feeding it (+25% damage) and stars (+25% maximum health each) are explained on the
  [Summon Wolf](../abilities/summon-wolf.md#feeding) page.

## Damage

Most companions' damage per hit grows slowly at low levels and sharply at high levels.

| Companion | Damage types | Lv 0 | Lv 50 | Lv 100 |
| --- | --- | ---: | ---: | ---: |
| Deathsquito | 75% *Pierce*{.dmg .pierce}<br>25% *Poison*{.dmg .poison} | **10** | **105** | **200** |
| Ghost | *Slash*{.dmg .slash} | **10** | **88** | **200** |
| Skeleton | *Slash*{.dmg .slash} | **5** | **44** | **100** |
| Stone golem | 75% *Blunt*{.dmg .blunt}<br>25% *Pierce*{.dmg .pierce} | **10** | **77** | **200** |
| Surtling | 75% *Fire*{.dmg .fire}<br>25% *Blunt*{.dmg .blunt} | **10** | **59** | **150** |
| Ulv | 75% *Slash*{.dmg .slash}<br>25% *Pierce*{.dmg .pierce} | **5** | **31** | **80** |
| Wolf | *Slash*{.dmg .slash} | **5** | **31** | **80** |

- Deathsquito damage grows evenly with level: 10 base + 1.9
  [per level](../reference/glossary.md#per-level).
- A fed Ulv or wolf deals 25% more.
- The neck does not fight. Its chop damage to trees is on the [Neck](../abilities/neck.md#stats) page.

## Health

Maximum health grows slowly at low levels and sharply at high levels.

| Companion | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Neck | 20 | 80 | 200 |
| Skeleton or ghost | 25 | 455 | 1250 |
| Stone golem | 50 | 735 | 2000 |
| Surtling | 25 | 190 | 500 |
| Ulv or wolf, no stars | 100 | 1125 | 3000 |
| Ulv or wolf, 2 stars | 150 | 1685 | 4500 |

- Deathsquitos keep the health of a wild deathsquito; it does not grow with your level.

## Energy and regeneration

Each hit a companion lands on an enemy may regenerate 1 energy for you.

| Companion | Energy chance per hit | Health regeneration |
| --- | ---: | --- |
| Neck | None | 5% of maximum health per second |
| Skeleton or ghost | 10% | 2% of maximum health per second |
| Stone golem | 50% | 1% of maximum health per second |
| Surtling | 50% | 5% of maximum health per second |
| Ulv or wolf | 50% | 5% of maximum health every 5 s (2% in combat) |

- Deathsquitos and charmed creatures give no energy and get no extra regeneration.

## Distance from you

| Companion | Runs much faster to catch up | Teleports back to about 30 m from you | Disappears |
| --- | --- | --- | --- |
| Charmed creature | No | No | 55 m or more (the charm ends) |
| Deathsquito | No | No | 55 m or more |
| Neck | No | No | No (it only works within 50 m of you) |
| Skeleton or ghost | 35 m or more | 50 m or more | 55 m or more |
| Stone golem or surtling | 35 m or more | No | 65 m or more |
| Ulv or wolf | 35 m or more | 50 m or more | 55 m or more |

## Permanent bonuses

- [Infused Morgenheart](../items/permanent-consumables.md#infused-morgenheart): +25% damage and +25% maximum health
  for summoned companions. Companions already out get the health bonus right away.
- [Infused Liquid Frost](../items/permanent-consumables.md#infused-liquid-frost): +20% damage for summoned
  companions too. It multiplies with Infused Morgenheart.
- The damage bonuses apply to the companions that fight. The neck's chop damage is unchanged.
- Neither applies to charmed creatures.
- The values on this page are without these bonuses.

## Interactions

- **Demigod skill experience:** [Hel](../demigods/hel.md#demigod-skill-experience) gains experience from her
  minions' damage, [Fenrir](../demigods/fenrir.md#demigod-skill-experience) from his Ulv's damage and
  [Surtr](../demigods/surtr.md#demigod-skill-experience) from his surtlings' Fire damage.
- [Sacrifice](../abilities/sacrifice.md) (Hel) turns her skeletons and ghost into energy and health.
- [Burning Ground](../abilities/burning-ground.md) never hits companions.
- [Holy Heal](../abilities/holy-heal.md) does not heal companions.
- [Sense Creatures](../abilities/sense-creatures.md) does not show companions.
- Companions never drop extra skins ([Hunter](../attributes/hunter.md)) or coins ([Raider](../attributes/raider.md)),
  and do not count for [Thirsty](../attributes/thirsty.md).
- Kills by your minions do not count for [Soul Reaper](../attributes/soul-reaper.md).
- A creature that [Charm](../abilities/charm.md#taming) tames for good becomes a normal tamed creature, not a
  companion: none of the rules on this page apply to it.

## Wisps

[Nature Wisp](../abilities/nature-wisp.md) (Freyja) and [Energy Wisp](../abilities/energy-wisp.md) (Hraesvelgr) are
summoned helpers, but not creatures: enemies cannot attack them, and the companion rules on this page do not apply.

## Related pages

- [Stone Golem](../abilities/stone-golem.md)
- [Summon Surtling](../abilities/summon-surtling.md)
- [Summon Wolf](../abilities/summon-wolf.md)
- [Minions](../abilities/minions.md)
- [Neck](../abilities/neck.md)
- [Poison Cloud](../abilities/poison-cloud.md)
- [Charm](../abilities/charm.md)
- [Permanent Consumables](../items/permanent-consumables.md)

<!-- Verified against NorseDemigods 1.9.1 -->
