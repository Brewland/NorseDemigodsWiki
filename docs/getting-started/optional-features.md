# Optional Features

Server settings that make the materials for the mod's recipes easier to get, plus other features a server can
turn on or off. Most are off by default.

<!-- IMAGE: map with the closest merchants and bosses pinned -->

All settings on this page are for server admins (or for you, in single player).

## Easier materials

| Feature | Default | What it does | Setting |
| --- | --- | --- | --- |
| Harpoon fishing | On | Catch fish with the [Abyssal Harpoon](../items/abyssal-harpoon.md). | `[Harpoon Fishing] Enable Harpoon Fishing` |
| Merchant map pins | Off | When you spawn, pins Haldor, Hildir and the Bog Witch on your map: for each, the location closest to the world center. | `[(General)] Find Closest Merchants` |
| Boss map pins | Off | When you spawn, pins every boss on your map, from Eikthyr to Fader: for each, the location closest to the world center. The Queen's pin marks the infested mine entrance, like the vanilla vegvisir. | `[(General)] Find Closest Bosses` |
| Haldor's extra items | Off | Haldor also sells a Queen bee (150 coins) and an [Abyssal Harpoon](../items/abyssal-harpoon.md) (350 coins). | `[Merchant] Enable Custom Merchant Items` |
| Queen bees from beehives | Off (0%) | Taking honey from a beehive can drop a Queen bee. The chance is the setting's value for each honey in the hive: at 10%, a hive with 4 honey gives a 40% chance. | `[Honey] Queen Bee Spawn Chance (%)` |
| Beehives without space | Off | Beehives no longer need free space around them to produce honey. | `[Honey] Ignore Beehive Proximity Check` |
| Honey per beehive | 4 (vanilla) | How much honey a beehive holds before it is full (up to 50). | `[Honey] Max Honey Produced By Beehive` |
| More feathers | ×1 | Birds (seagulls, crows and ash crows) drop up to ×3 feathers. | `[(Difficulty)] Feather Drop Multiplier` |

- Honey goes into [sweet fish foods](../items/sweet-fish-foods.md); queen bees let you build more beehives.
- Haldor's prices are settings too: `[Merchant] Queen Bee Price` and `[Merchant] Abyssal Harpoon Price` (`0`
  removes the item from his shop).
- Bosses matter for your [demigod skill](how-the-mod-works.md#demigod-skill): its level cap rises with each boss
  trophy.

## Other features

| Feature | Default | What it does | Setting |
| --- | --- | --- | --- |
| Experimental features | Off | Features not fully tested yet. Today: [Holy Sun](../abilities/holy-sun.md) burns tar (not in multiplayer). | `[(General)] Enable Experimental Features` |
| Teleport | On | Every demigod can [teleport](../abilities/teleport.md) to their bed and back. | `[Teleportation] Enable Teleport Ability` |
| Teleport with any item | Off | Teleport also works while you carry items that cannot be teleported. See [Teleport](../abilities/teleport.md#limits). | `[Teleportation] Ignore Non Teleportable Items` |
| Abilities in PvP | On | Offensive abilities also hit other players in PvP. | `[Combat] Enable Pvp For Abilities` |
| Ward protection | Off | Players cannot damage buildings inside an active player ward. | `[(General)] Protect Pieces Covered By Ward` |
| Single-use runestone | Off | The [Demigod Runestone](../items/demigod-runestone.md) is used up when you choose a demigod. | `[Runestone] Runestone Consumable` |
| Skill loss on death | Off | You lose 5 demigod skill levels when you die. | `[Skills] Enable Skill Loss On Death`, `[Skills] Levels Lost On Death` |
| Disabled demigods | None | Demigods on this list cannot be chosen, e.g. `Fenrir,Thor`. | `[(General)] Disabled Demigods List` |

## Related pages

- [Difficulty](difficulty.md)
- [Installing the Mod](installing-the-mod.md#settings)

<!-- Verified against NorseDemigods 1.9.1 -->
