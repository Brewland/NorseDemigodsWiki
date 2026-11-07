# Energy

Energy is the resource demigods spend to cast most abilities. It regenerates over time, many abilities and
attributes give it back, and your maximum energy grows with your demigod skill level.

<!-- IMAGE: the energy meter in the HUD, showing energy and level -->

## How it works

- Most abilities cost energy. Each ability page shows its cost in the infobox; some cost eitr instead.
- You cannot cast an ability without enough energy for it.
- Your energy is saved when you log out and comes back when you log in (up to your current maximum).
- You start with 0 energy after you die or choose a demigod.
- The energy meter at the bottom left shows your energy, your maximum and your demigod skill level. While a
  draining ability is active, it shows that ability's name instead of the level.

## Maximum energy

You get 1 more maximum energy every 10 demigod skill levels.

| Demigod skill level | Maximum energy |
| ---: | ---: |
| 0 | 2 |
| 10 | 3 |
| 20 | 4 |
| 30 | 5 |
| 40 | 6 |
| 50 | 7 |
| 60 | 8 |
| 70 | 9 |
| 80 | 10 |
| 90 | 11 |
| 100 | 12 |

Bonuses on top:

| Source | Bonus |
| --- | --- |
| [Infused Megingjord](../items/infused-megingjord.md) (worn) | +3 |
| [Thunder Forger](../attributes/thunder-forger.md) (Brokkr) | +1 |

## Regeneration

- You regain 1 energy every 10 seconds on your own.
- **Spending energy restarts the countdown:** the next point comes a full 10 seconds after you last spent energy.
- [Infused Leather Scraps](../items/permanent-consumables.md#infused-leather-scraps) shortens the time, down to 5
  seconds after 5 items.

### Draining abilities

Some abilities stay active and drain energy instead of costing it once:

| Ability | Demigods | Drains 1 energy every |
| --- | --- | --- |
| [Decay Aura](../abilities/decay-aura.md) | Hel | 3 s |
| [Enrage](../abilities/enrage.md) | Fenrir | 2 s |
| [Heal Over Time](../abilities/heal-over-time.md) | Fenrir, Freyja, Kvasir, Ullr | 1 s |
| [Lightning Aura](../abilities/lightning-aura.md) | Thor | 4 s |
| [Lightning Storm](../abilities/lightning-storm.md) | Thor | 1 s |

- They need at least 1 energy to start, and stop when your energy runs out.
- Turning one off before its first drain still costs 1 energy.
- **No regeneration while one is active:** each drain restarts the countdown, so passive regeneration never
  happens. Most chances to regain energy on a hit or block are also blocked (see the table below).

## Getting energy back

Each page has the exact chance or amount.

| Source | Demigods | When | Blocked while draining |
| --- | --- | --- | --- |
| [Acid Bolt](../abilities/acid-bolt.md), [Meteor](../abilities/meteor.md) | Hel | Chance when it hits an enemy | Yes |
| [Fireball](../abilities/fireball.md) | Surtr | Chance when it hits an enemy | Yes |
| [Holy Strike](../abilities/holy-strike.md) | Eir | Chance when it strikes an enemy | Yes |
| [Ice Shards](../abilities/ice-shards.md) | Fenrir | Chance for each shard that hits an enemy | Yes |
| [Lightning Bolt](../abilities/lightning-bolt.md) | Njord | Chance when it hits an enemy | Yes |
| [Lightning Strike](../abilities/lightning-strike.md) | Thor | Chance when the explosion damages anything | Yes |
| [Lightning Torpedo](../abilities/lightning-torpedo.md) | Brokkr | Chance when it hits an enemy | Yes |
| [Poison Javelin](../abilities/poison-javelin.md) | Freyja | Chance when it hits an enemy | Yes |
| [Hunter](../attributes/hunter.md) | Ullr | Chance when an arrow or bolt hits an enemy | Yes |
| [Titan Arms](../attributes/titan-arms.md) | Fenrir | Chance on bare-handed or fist-weapon hits, and on bare-handed blocks | Yes |
| [Valkyrie](../attributes/valkyrie.md) | Eir, Freyja | Chance when blocking an enemy's attack or hitting it with a thrown spear | Yes |
| [Drain Blood](../abilities/drain-blood.md) | Surtr | Turns health into energy | No |
| [Sacrifice](../abilities/sacrifice.md) | Hel | Turns minions (or health) into energy | No |
| [Restoration](../abilities/restoration.md) | Njord, Thor | Restores energy while you channel it | No |
| [Stone Shield](../abilities/stone-shield.md) | Brokkr | Chance every second while active | No |
| [Telekinesis](../abilities/telekinesis.md) | Hraesvelgr | Chance to refund its energy cost | No |
| [Flame Body](../attributes/flame-body.md) | Surtr | Chance every second | No |
| [Static Body](../attributes/static-body.md) | Thor | Chance every second | No |
| [Water Shield](../attributes/water-shield.md) | Njord | Chance every second while the shield is up | No |
| [Sneaky](../attributes/sneaky.md) | Ullr | Each sneak attack | No |
| [Thirsty](../attributes/thirsty.md) | Kvasir | Chance on each kill | No |
| [Thorn Body](../attributes/thorn-body.md) | Freyja | 1 energy every 5 s near a tree | No |
| [Companions](../companions/index.md#energy-and-regeneration) | Several | Chance when a companion hits an enemy | No |

## Default values

| Setting | Default | Config |
| --- | --- | --- |
| Maximum energy at level 0 | 2 | `[Energy] Energy At Base Level` |
| Maximum energy at level 100 | 12 | `[Energy] Energy At Max Level` |
| Time to regenerate 1 energy | 10 s | `[Energy] Energy Regeneration Period (seconds)` (`0` turns it off) |

## Related pages

- [Progression](progression.md)
- [Abilities](../abilities/index.md)
- [Infused Megingjord](../items/infused-megingjord.md)
- [Permanent Consumables](../items/permanent-consumables.md#infused-leather-scraps)

<!-- Verified against NorseDemigods 1.9.3 -->
