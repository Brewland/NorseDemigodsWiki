# Demigod Runestone

The Demigod Runestone is the item you use to choose your demigod, or to switch to another one later. You get one
for free when you start, and it is not used up when you choose.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Type** | Misc (reusable) |
| **Crafting station** | None (craft from your inventory) |
| **Recipe** | 1 Stone<br>1 Resin |
| **Restricted to** | Anyone |
| **Stack size** | 1 |
| **Config ID** | `DemigodRunestone` |
| **Config section** | `[Runestone]` |

</div>

<!-- IMAGE: the Demigod Runestone menu with a demigod page open -->

## Effect

1. Use the runestone from your inventory: a menu opens.
2. Pick a demigod from the list to read its description.
3. Press *"I choose you!"* to become that demigod.

- You keep the runestone: it can be used again at any time.
- **If enabled:** the runestone is used up when you choose a demigod. Setting: `[Runestone] Runestone Consumable`
  (off by default).
- A demigod the server has disabled cannot be chosen; players who already are that demigod keep it. Setting:
  `[(General)] Disabled Demigods List`.

## Getting one

- **Free runestone:** every time you spawn while you are not a demigod and have no runestone, one is put in your
  inventory. Setting: `[Runestone] Runestone Spawn At Start` (on by default).
- **Crafting:** from 1 Stone and 1 Resin, without a crafting station. Servers can change the recipe:
  `[Runestone] Runestone Crafting Recipe` (default `Stone:1,Resin:1`). If the setting cannot be read, the default
  recipe is used.

## Switching demigods

Choosing a different demigod while you already are one asks for confirmation first. If you confirm:

| What happens | Default |
| --- | --- |
| Demigod skill levels lost | 5, and your progress toward the next level (never below level 0) |
| Abilities | Replaced by the new demigod's abilities |
| [Ability infusion](infusion-items.md) | Lost; the new demigod must be infused on its own |
| [Permanent consumables](permanent-consumables.md) | Kept |

- The level loss is a setting: `[Skills] Levels Lost When Switching Demigod`.
- Choosing the demigod you already are does nothing.

## Related pages

- [Demigods](../demigods/index.md)
- [Infusion Items](infusion-items.md)
- [Permanent Consumables](permanent-consumables.md)

<!-- Verified against NorseDemigods 1.9.1 -->
