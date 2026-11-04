# Soar

Soar is Hraesvelgr's airborne special attack: a burst of wind that launches him forward through the air. Hold it to
charge a longer, higher launch. He can soar several times before landing.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | [Hraesvelgr](../demigods/hraesvelgr.md) |
| **Input** | ++mouse-middle++ (Special attack while airborne), hold to charge |
| **Energy cost** | None |
| **Cooldown** | 3 s |
| **Cast time** | Up to 8 s of charging (optional) |
| **Config ID** | `Soar` |
| **Config section** | `[Ability Soar]` |

</div>

<!-- IMAGE: in-game screenshot of Hraesvelgr soaring with a wind trail -->

## Effect

1. Jump, then use the special attack while in the air.
2. Release it right away for a quick launch, or keep holding to charge (wind gathers around you).
3. When you release it, or after 8 s of charging, your fall stops and you are launched forward and upward.

The longer you charge, the stronger the launch:

| Charge | Forward force | Upward force |
| --- | ---: | ---: |
| None (quick release) | 70 | 5 |
| Half (4 s) | 175 | 25 |
| Full (8 s) | 280 | 45 |

- Charging starts 0.35 s after you press the key; releasing before that gives a quick launch.
- The launch costs no stamina.
- Fall damage is counted from the height where you launch, not from where your jump started.
- If you land or start swimming while charging, the charge is lost and nothing happens.
- While airborne, the special attack always triggers Soar, whatever weapon you hold.

## Dashes before landing

- You can soar up to **3** times before you touch the ground again.
- The 3 s cooldown applies between launches.
- In-game message when you have used them all: *"You cannot dash again until you land!"*

## Infused

- Up to **5** launches before landing instead of 3.

## Limits

- Only while airborne. Not while encumbered, swimming or sitting.

## Related pages

- [Hraesvelgr](../demigods/hraesvelgr.md)
- [Glide](../attributes/glide.md)

<!-- Verified against NorseDemigods 1.9.1 -->
