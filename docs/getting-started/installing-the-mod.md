# Installing the Mod

Norse Demigods is a BepInEx mod for Valheim. Install it with a mod manager or by hand. On a multiplayer server,
every player needs the same mod version and data files as the server.

<!-- IMAGE: Norse Demigods in a mod manager's list of installed mods -->

Mod page:<br>
[Thunderstore](https://thunderstore.io/c/valheim/p/Alpus/NorseDemigods/) · [Hexium](https://valheim.hexium.gg/mods/Alpus/NorseDemigods)

## Requirements

| Mod | What it does | Links |
| --- | --- | --- |
| BepInExPack Valheim | Loads mods into the game | [Thunderstore](https://thunderstore.io/c/valheim/p/denikson/BepInExPack_Valheim/) · [Hexium](https://valheim.hexium.gg/mods/denikson/BepInExPack_Valheim) |
| Jotunn | Modding library the mod is built on | [Thunderstore](https://thunderstore.io/c/valheim/p/ValheimModding/Jotunn/) · [Hexium](https://valheim.hexium.gg/mods/ValheimModding/Jotunn) |
| YamlDotNet | Reads the demigod file (`Demigods.yaml`) | [Thunderstore](https://thunderstore.io/c/valheim/p/ValheimModding/YamlDotNet/) · [Hexium](https://valheim.hexium.gg/mods/ValheimModding/YamlDotNet) |

Mod managers install these automatically.

## With a mod manager

1. Open your mod manager (for example r2modman or the Thunderstore Mod Manager) and select Valheim.
2. Search for **NorseDemigods** by Alpus and install it. The required mods are installed with it.
3. Start the game from the mod manager.

## Manual install

1. Install the three required mods above, following their instructions.
2. Put the Norse Demigods files in their own folder inside `BepInEx/plugins`.
3. Keep every file and folder that comes with the mod next to `NorseDemigods.dll`, in the same folder structure.

- Do not rename `NorseDemigods.dll`.
- The mod may not work correctly if files are missing or moved.

## Video guide

A video walkthrough of the setup and the mod's basics:<br>
<https://www.youtube.com/watch?v=uaGUaIzbVR8>

!!! warning "Outdated video"
    The video was recorded while the mod was in early access. Demigods, abilities, numbers and settings have
    changed since; where they differ, this wiki is up to date.

## Multiplayer

- The server and every player need the mod, in **exactly the same version** (for example 1.9.3).
- Every player also needs the same `Demigods.yaml` and `Consumables.json` as the server. These files set each
  demigod's abilities and attributes, and the mod's recipes.
- A player with different files cannot join. In-game message: *"Norse Demigods: your Demigods.yaml differs from
  the server's. Install the same mod files as the server (for example, its modpack) and try again."*
- The easiest way to match the server is to install the server's modpack.

## Settings

The settings file is `BepInEx/config/NorseDemigods.cfg`. It is created the first time you start the game with the
mod.

- Edit it with a text editor while the game is closed, or in-game with a configuration manager (see
  [Recommended Mods](recommended-mods.md#configurationmanager)).
- On a server, most settings come from the server and are sent to players when they join. Only admins can change
  them.
- Your own settings stay yours: hotkeys (`[(Hotkeys)]`), the interface (`[User Interface]`), passive visual effects
  (`[(General)] Enable Passive Special Effects`) and the attack angle (`[(General)] Enhance Attack Angle`).
- To turn the mod off without uninstalling it, set `[(General)] Enable Mod` = `false` and restart the game.
- Server admins: see [Difficulty](difficulty.md) and [Optional Features](optional-features.md) next.

!!! warning "Updates reset the advanced settings"
    After every mod update, the advanced settings (abilities, attributes and demigods) go back to their new
    defaults, so the update's balance changes apply. To keep your own values, set
    `[(Configs)] Automatically Update Configs` = `false`. Other settings, such as Difficulty and hotkeys, are kept.

## Languages

The mod uses your game language when a translation exists, and English otherwise.

Included: Brazilian Portuguese, Chinese, English, French, German, Hungarian, Italian, Japanese, Korean, Polish,
Russian, Spanish, Turkish, Ukrainian and Vietnamese.

## Related pages

- [Recommended Mods](recommended-mods.md)
- [Compatibility](compatibility.md)
- [Difficulty](difficulty.md)

<!-- Verified against NorseDemigods 1.9.3 -->
