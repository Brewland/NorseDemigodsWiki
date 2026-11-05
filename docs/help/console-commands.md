# Console Commands

Norse Demigods adds a few console commands. One lets any player stop being a demigod; the others are cheats for
server admins and testing.

<!-- IMAGE: the game console with a Norse Demigods command typed in -->

## Using the console

- The console opens with ++f5++, but only when the game was started with the `-console` launch option (vanilla).
- Cheat commands work only after you turn on cheats with `devcommands`. On a server, only admins can do that
  (vanilla).
- Type the command and press ++enter++.

## Commands

| Command | What it does | Cheat |
| --- | --- | --- |
| `RevokeDemigod` | Removes your demigod, your ability infusion and your permanent consumables, and resets your demigod skill to level 0. Cannot be undone. | No |
| `InfuseAbilities` | Infuses your current demigod's abilities. | Yes |
| `GiveDemigodExperience <amount>` | Gives your demigod skill the amount of experience, for example `GiveDemigodExperience 100`. It ignores the [skill cap](../getting-started/progression.md#skill-cap). | Yes |
| `NoAbilityCooldown` | Abilities have no cooldown. Run it again to turn it off. | Yes |
| `NoEnergyCost` | Abilities cost no energy. Run it again to turn it off. | Yes |
| `RestoreEnergy` | Fills your energy and gives you the Rested effect. | Yes |
| `ResetDemigodSettings` | Resets the advanced settings (abilities, attributes and demigods) to their defaults. No progress is lost. | Yes |

The commands that act on your demigod do nothing if you have not chosen one.

## Vanilla commands

| Command | What it does |
| --- | --- |
| `raiseskill Demigod <levels>` | Raises your demigod skill by that many levels (vanilla cheat command). |

## Related pages

- [First Steps](../getting-started/first-steps.md#changing-your-mind)
- [Progression](../getting-started/progression.md)
- [FAQ](faq.md)

<!-- Verified against NorseDemigods 1.9.1 -->
