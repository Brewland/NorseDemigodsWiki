# Water Shield

Water Shield is Njord's own attribute: after a few seconds out of combat, the nearby waters form a shield around him
that heals him, speeds up his movement and mining, can give him energy and protects him from heat.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Demigod** | [Njord](../demigods/njord.md) |
| **Condition** | After 5 s out of combat; not near a fire |
| **Config ID** | `WaterShield` |
| **Config section** | `[Attribute Water Shield]` |

</div>

<!-- IMAGE: Njord surrounded by the Water Shield bubble -->

## Effects

While the shield is active:

| Effect | Value |
| --- | --- |
| Health restored | 2 every 2 seconds |
| Movement speed | +10% |
| Attack speed with a pickaxe | +30% |
| Chance every second to regenerate 1 energy | 15% |
| Heat (lava and the hot Ashlands sea) | Immune |

- No health regeneration while you are burning, poisoned, frozen, shocked or freezing.
- The shield keeps you Wet.

## How it works

- The shield forms after 5 s without dealing damage and without being hit by an enemy or another player.
- It ends when you deal damage or are hit. The boiling Ashlands sea also ends it.
- It also ends near a fire (when you get the campfire effect). It can form again 2 s after you leave the fire.
- Teleporting or dying ends it; the 5 s count starts again.

## Notes

- **Movement speed:** applies to walking, jogging, sprinting, sneaking and swimming, but not while encumbered, and
  does not change jump height. Adds up with other movement speed bonuses. Setting:
  `[(Special Modifiers)] Special Movement Speed Modifier (%)`.
- With [Aquatic Body](aquatic-body.md) (Njord's default), being kept Wet gives +50% stamina regeneration.

## Related pages

- [Njord](../demigods/njord.md)
- [Aquatic Body](aquatic-body.md)

<!-- Verified against NorseDemigods 1.9.1 -->
