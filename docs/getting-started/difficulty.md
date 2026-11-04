# Difficulty

The mod's Difficulty setting makes enemies hit harder, to balance the power of demigods. **Unlike most difficulty
settings, it raises damage after blocking, armor and resistances, so shields and armor stay useful.**

<!-- IMAGE: the Difficulty setting in a configuration manager -->

## Why change it

- The mod is balanced close to vanilla, but once you get used to your demigod you may feel overpowered.
- The default is `Vanilla`, which changes nothing. **Expert** is the recommended difficulty.
- Server admins set it: `[(Difficulty)] Difficulty`. It applies to every player on the server, demigod or not.
- Valheim's world modifiers, or another difficulty mod, work too, and add up with it.

## Difficulties

| Difficulty | Base damage | Final damage<br>(enemies) | Final damage<br>(bosses) |
| --- | ---: | ---: | ---: |
| Vanilla (default) | +0% | +0% | +0% |
| Novice | +0% | +25% | +50% |
| Adept | +0% | +50% | +100% |
| Expert (recommended) | +0% | +75% | +150% |
| Elite | +0% | +100% | +200% |
| Hardcore | +25% | +100% | +200% |
| Insane | +50% | +100% | +200% |

- **Final damage** is added at the very end, after your shield, armor and resistances have reduced the hit.
- **Base damage** raises the damage of enemies' attacks before anything reduces them, like Valheim's world
  modifiers. Only Hardcore and Insane change it. Tamed creatures are not affected.
- Only damage that creatures (monsters and bosses) deal to players changes. Burning and poison caused by a
  creature's attack count as that creature's damage, at its value (the boss value for bosses).

Not changed by the final damage:

- Damage from other players or from yourself.
- Falls, falling trees and logs, drowning and freezing.
- Lava, the Ashlands ocean and fires such as campfires and cinder fire.
- Turrets, traps and smoke.

## Why final damage keeps shields useful

Valheim's blocking and armor work best against small hits: the bigger the hit, the less of it they stop. A
setting that raises base damage (like world modifiers and most difficulty mods) makes every hit bigger before your
shield and armor see it, so they become much weaker.

The mod's final damage leaves blocking and armor working against the hit's normal size, then raises only what
gets through:

- Small hits that your shield or armor almost stop stay small.
- Your shield and armor stop the same share of each hit as in vanilla.
- Blocking costs the same stamina and causes the same stagger as in vanilla.

Example (vanilla rules, numbers for illustration): a hit of 60 against a shield with a block power of 50, without
body armor.

| Setting | Damage that gets through |
| --- | ---: |
| No change | 18 |
| Base damage +75%, e.g. a world modifier (hit of 105) | 55 |
| Final damage +75% (Expert) | 31.5 |

## Other difficulty settings

Also in `[(Difficulty)]`, all for server admins:

| Setting | Default | What it does |
| --- | --- | --- |
| `Deer Run Speed Modifier (%)` | 100% | How fast deer run, to make up for demigods' speed (up to 300%). |
| `World Creatures Spawn Amount (%)` | 100% | Bigger groups, for creatures that spawn in groups (up to 300%). |
| `World Creatures Spawn Frequency (%)` | 100% | Creatures spawn more often (up to 500%). |
| `World Creatures Exempt` | A list | Creatures the two spawn settings never change, such as boars, deer, trolls, lox and serpents. |
| `Ammo Consumption (%)` | 100% | Share of shots that use up an arrow or bolt. At 50%, about 1 shot in 2 uses ammo. |

## Related pages

- [Optional Features](optional-features.md)
- [Installing the Mod](installing-the-mod.md#settings)

<!-- Verified against NorseDemigods 1.9.1 -->
