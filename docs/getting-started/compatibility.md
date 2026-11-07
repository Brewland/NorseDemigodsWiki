# Compatibility

Most mods work alongside Norse Demigods. This page lists the mods known to cause problems, the mods Norse
Demigods has built-in support for, and third-party mods that connect Norse Demigods to other mods.

<!-- IMAGE: the compatibility settings in a configuration manager -->

Entries in the first two tables are labelled:

- **Confirmed:** handled in the mod's code, or stated by the mod author.
- **User-reported:** reported by players (for example on Discord) and not verified.

## Known problems

| Mod | Severity | Problem | Source |
| --- | --- | --- | --- |
| BetterTames | High | Summoned companions become immortal, and you can summon again and again without limit. | User-reported |
| CombatincentivesREwrite | High | You cannot save or respawn while both mods are installed. | User-reported |
| FortifySkillsRedux | Medium | Your demigod skill level drops sharply when you die. | User-reported |
| Resurrection | Low | After being resurrected, your demigod's effects do not come back until you log out and in again. | User-reported |
| Shawesomes Divine Armaments | Medium | With its "ssj" feature active, your skills level up too quickly. | User-reported |

## Built-in support

| Mod | What Norse Demigods does | Source |
| --- | --- | --- |
| Agility (by blacks7ar) | Removes Agility's jump changes, so the double jump from [Hare Legs](../attributes/hare-legs.md) keeps working. Setting: `[(General)] Enhance Compatibility With Mod Agility` (on by default). | Confirmed |
| EpicLoot | Its attack speed bonuses add up with the mod's. | Confirmed |
| Environmental Awareness | [Restoration](../abilities/restoration.md) is only interrupted by hits that deal damage, so this mod's harmless hits do not stop it. | Confirmed |
| Jewelcrafting | Its attack speed bonuses add up with the mod's. Its gliding effects are removed while [Crush](../abilities/crush.md) is active, so Crush still dives to the ground. | Confirmed |
| PathOfValheiman | The demigod skill is exempt from its skill freeze, so it still gains experience and shows the right level. | Confirmed |
| Warfare (by Therzie) | Warfare's pike special attack deals 120% of the weapon's damage, so it does not outclass the demigods' area abilities. Setting: `[(General)] Enhance Compatibility With Mod Warfare` (on by default). | Confirmed |

## Bridge mods

Mods by other authors that connect Norse Demigods to another mod. Install one only if you also use that other mod.
They are not made or tested by the Norse Demigods author; descriptions come from their own pages.

| Mod | Author | For players of | What it does | Links |
| --- | --- | --- | --- | --- |
| NorseDemigodsPovBridge | OblitusEsMods | PathOfValheiman | Scales Norse Demigods' abilities, healing and summons with PathOfValheiman's passive tree, set separately for each element and spell. Also gives every claw weapon the claw swipe. | [Thunderstore](https://thunderstore.io/c/valheim/p/OblitusEsMods/NorseDemigodsPovBridge/) |

## If something breaks

- Turn off the matching setting above if Agility or Warfare causes problems.
- If another interface mod clashes with the mod's meters, turn them off: `[User Interface] Enable Meters`. You
  lose the energy and companion meters.
- Report problems on the [Norse Demigods Discord](https://discord.gg/gSQHmE3yap).

## Related pages

- [Installing the Mod](installing-the-mod.md)
- [Recommended Mods](recommended-mods.md)

<!-- Verified against NorseDemigods 1.9.3 -->
