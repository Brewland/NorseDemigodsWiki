# Teleport

Teleport is shared by all demigods: it takes you to your bed, and a second use takes you back to where you left.
It costs no energy and is enabled by default.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Used by** | All demigods (e.g. [Thor](../demigods/thor.md)) |
| **Input** | ++p++ (Teleport) |
| **Energy cost** | None |
| **Cooldown** | 15 s |
| **Cast time** | 3 s |
| **Config ID** | `Teleport` |
| **Config section** | `[Ability Teleport]` |

</div>

<!-- IMAGE: in-game screenshot of the Teleport charge effect -->

## Effect

1. Press ++p++. You cheer and charge for 3 s, unable to move.
2. You teleport to your bed. Your current location is saved.
3. Use Teleport again within 300 s to return to the saved location.
4. After 300 s the saved location expires. A status effect shows the time left.

## Limits

- You must have claimed a bed. In-game message: *"You have not claimed a bed yet"*.
- You cannot teleport while carrying items that cannot be teleported, such as ore.

**If enabled:** `[Teleportation] Ignore Non Teleportable Items` = `true` allows them. This only matters if world
modifiers or other mods restrict teleportation.

## Settings

| Setting | Default | Config |
| --- | --- | --- |
| Teleport enabled for all demigods | On | `[Teleportation] Enable Teleport Ability` |
| Hotkey | ++p++ | `[(Hotkeys)] Hotkey Ability Teleport` |

## Related pages

- [Thor](../demigods/thor.md)

<!-- Verified against NorseDemigods 1.9.0 -->
