# Corruption

Corruption is Kvasir's own attribute: his wards are cheaper to build, and while he stands inside one, it slowly
duplicates wood, seeds and other materials in a chest next to it and makes him more comfortable.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Demigod** | [Kvasir](../demigods/kvasir.md) |
| **Condition** | While you are inside the area of an active ward |
| **Config ID** | `Corruption` |
| **Config section** | `[Attribute Corruption]` |

</div>

<!-- IMAGE: in-game screenshot of a corrupted ward next to a chest -->

## Cheaper wards

Your ward recipe changes to:

| Material | Amount |
| --- | --- |
| Wood | 5 |
| Honey | 1 |

- The materials are not returned when you deconstruct the ward.

## Duplication

While you stand inside the area of an active ward:

1. The chest closest to the ward, within 3 m of it, is corrupted.
2. The first duplicable item in that chest is copied once after a short time, then the next copy starts.

| Material | Time per copy |
| --- | ---: |
| Coal | 3 s |
| Wood, Finewood, Corewood, Ancient bark, Yggdrasil wood, Ashwood | 5 s |
| Tar, Charcoal resin | 10 s |
| Carrot, turnip, onion, vineberry and ivy seeds; beech seeds, birch seeds, pine cones | 15 s |

- Each copy adds 1 item to the stack already in the chest. Nothing is copied while the chest is open or full.
- Only one item is copied at a time: the first duplicable item in the chest's inventory.
- If you are inside several wards, the closest one counts.
- Servers can change the lists: `[Attribute Corruption] Wood List`, `[Attribute Corruption] Seed List`.

## Comfort

| Effect | Value |
| --- | --- |
| Comfort level inside an active ward | +3 |

## Notes

- The in-game tooltip only mentions wood and seeds; coal, tar and charcoal resin are copied too.

## Related pages

- [Kvasir](../demigods/kvasir.md)

<!-- Verified against NorseDemigods 1.9.1 -->
