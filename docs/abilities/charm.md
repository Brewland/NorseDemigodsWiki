# Charm

Charm turns a creature under Kvasir's crosshair into a temporary ally that fights on his side. Sometimes it tames the
creature for good.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Kvasir](../demigods/kvasir.md) |
| **Input** | ++mouse-side-up++ + ++block++ (Ability C) |
| **Energy cost** | 1 |
| **Cooldown** | 10 s |
| **Duration** | 15–30 s, by level |
| **Range** | 20 m |
| **Config ID** | `Charm` |
| **Config section** | `[Ability Charm]` |

</div>

<!-- IMAGE: in-game screenshot of a charmed creature fighting for Kvasir -->

## Effect

1. Aim at a creature within 20 m and use the ability. You cheer.
2. If the creature can be tamed, you may tame it permanently (see [Taming](#taming)).
3. Otherwise, it is charmed: it joins your side and fights your enemies until the charm ends.

- A charmed creature does not attack buildings.
- The charm ends when its time runs out, when the creature dies or when it gets 55 m or more away from you.
- All your charms end when you teleport or die.
- You can have several charmed creatures at once.
- Each cast gives demigod skill experience (see [Kvasir](../demigods/kvasir.md#demigod-skill-experience)).

## Targets

- Hostile creatures, or tameable creatures that are not tamed yet.
- Not bosses, players, or animals that never fight (such as deer).
- Its maximum health must not be above the limit for your level: 20
  [per level](../getting-started/glossary.md#per-level).
- No energy is spent and no cooldown starts when there is no valid target.

## Scaling

The charm duration grows evenly from 15 s at level 0 to 30 s at level 100.

| | Lv 0 | Lv 50 | Lv 100 |
| --- | ---: | ---: | ---: |
| Maximum health of the target | 0 | 1000 | 2000 |
| Charm duration | 15 s | 22 s | 30 s |

- At level 0, no creature can be charmed.
- The duration is rounded to whole seconds (22.5 s at level 50 shows as 22 s).

## Taming

If the creature can be tamed (in vanilla: boars, wolves, lox and other tameable creatures):

| Case | Chance to tame it for good |
| --- | ---: |
| You have not started taming it | 10% |
| It is already being tamed (fed) | 30% |

- A tamed creature stays tamed and no longer despawns. It is not charmed: the charm duration does not apply.

## Infused

- Energy cost: 1 → none.
- Cooldown: 10 s → 5 s.

## Limits

- Usable while airborne or swimming.

## Related pages

- [Kvasir](../demigods/kvasir.md)
- [Companions](../companions/index.md)

<!-- Verified against NorseDemigods 1.9.1 -->
