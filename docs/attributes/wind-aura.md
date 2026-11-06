# Wind Aura

Wind Aura is Hraesvelgr's own attribute: out of combat, a refreshing aura makes him chop and mine faster, move faster
and regenerate stamina.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Demigod** | [Hraesvelgr](../demigods/hraesvelgr.md) |
| **Condition** | Out of combat for 5 s; not while swimming |
| **Config ID** | `WindAura` |
| **Config section** | `[Attribute Wind Aura]` |

</div>

<!-- IMAGE: in-game screenshot of Hraesvelgr with the Wind Aura active -->

## Effects

While the aura is active:

| Effect | Value |
| --- | --- |
| Attack speed with axes and pickaxes | +30% |
| Movement speed | +10% |
| Stamina regeneration | 10 per second |
| Stamina used when sprinting in the air | None |

- Stamina regenerates while you are airborne, or on the ground when you are not sprinting or encumbered.

## Activation

1. The aura turns on after 5 s without dealing damage or taking damage from enemies or players.
2. It turns off as soon as you hit something or are hit, then the 5 s start again.

- Damage from your [Energy Wisp](../abilities/energy-wisp.md) does not count as combat.
- The aura is removed while swimming and never turns on in water, so its bonuses never apply there.
- It also turns off when you teleport or die.

## Notes

- **Movement speed:** applies to walking, jogging, sprinting, sneaking and swimming, but not while encumbered, and
  does not change jump height. Adds up with other movement speed bonuses. Setting:
  `[(Special Modifiers)] Special Movement Speed Modifier (%)`.

## Related pages

- [Hraesvelgr](../demigods/hraesvelgr.md)

<!-- Verified against NorseDemigods 1.9.2 -->
