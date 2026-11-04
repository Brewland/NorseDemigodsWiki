# Controls and Hotkeys

Abilities use the side mouse buttons, your block key and your weapon's special attack by default. Every key can
be changed in your settings.

<!-- IMAGE: the ND: Abilities compendium page listing ability keys -->

## Default keys

| Command | Default key | Notes |
| --- | --- | --- |
| Ability A | ++mouse-side-up++ | Change it if your mouse has no side buttons. |
| Ability B | ++mouse-side-down++ | Change it if your mouse has no side buttons. |
| Ability C | ++mouse-side-up++ + ++block++ | No key of its own by default. Give it one to cast it without blocking. |
| Ability D | ++mouse-side-down++ + ++block++ | No key of its own by default. Give it one to cast it without blocking. |
| Teleport | ++p++ | See [Teleport](../abilities/teleport.md). |
| Ignore special attack | ++left-alt++ + ++mouse-middle++ | Hold it to use your weapon's normal special attack. |

++block++ means "hold your block key" (Valheim's default: right mouse button).

## Special attacks

Valheim's special attack (secondary attack, default ++mouse-middle++) becomes an ability when you hold one of your
demigod's favorite weapons.

- Some demigods have more special attacks: one while blocking (++block++ + ++mouse-middle++) and one while
  airborne (++mouse-middle++ in the air).
- Which weapons trigger them differs per demigod: each demigod page lists them on its ability cards.
- Hold ++left-alt++ while using the special attack to get your weapon's normal special attack instead.

Your compendium page **ND: Abilities** lists every key and combination for your demigod. See
[First Steps](first-steps.md#the-compendium).

## Changing keys

- **In-game (easiest):** install a configuration manager (see
  [Recommended Mods](recommended-mods.md#configurationmanager)), open the Norse Demigods settings and set the
  keys under `(Hotkeys)`. Changes apply right away.
- **In the settings file:** edit the `[(Hotkeys)]` section of `BepInEx/config/NorseDemigods.cfg` while the game is
  closed.

| Command | Setting |
| --- | --- |
| Ability A | `[(Hotkeys)] Hotkey Ability A` |
| Ability B | `[(Hotkeys)] Hotkey Ability B` |
| Ability C | `[(Hotkeys)] Hotkey Ability C` |
| Ability D | `[(Hotkeys)] Hotkey Ability D` |
| Teleport | `[(Hotkeys)] Hotkey Ability Teleport` |
| Ignore special attack | `[(Hotkeys)] Hotkey Ignore Special Attack` |

- Hotkeys are your own settings: a server does not change them.
- To turn Teleport off, a server admin sets `[Teleportation] Enable Teleport Ability` = `false`. Unbinding the key
  is not needed.

## Interface settings

The `[User Interface]` section controls the mod's meters (energy and companions). These are your own
settings too.

| Setting | Default | What it does |
| --- | --- | --- |
| `Enable Meters` | On | Shows the mod's meters. Turn it off if another interface mod clashes with them. |
| `Show Current Experience` | Off | Shows your progress toward the next demigod skill level, as a percentage, in the energy meter. |
| `Energy Meter Anchor`, `Position`, `Scale`, `Text Color` | Lower left | Moves, resizes and recolors the energy meter. |
| `Pet Health Meter Anchor`, `Position`, `Scale`, `Text Color` | Lower left | The same for the companion meter (minions, necks or wolf). |

## Related pages

- [First Steps](first-steps.md)
- [Abilities](../abilities/index.md)
- [Recommended Mods](recommended-mods.md)

<!-- Verified against NorseDemigods 1.9.1 -->
