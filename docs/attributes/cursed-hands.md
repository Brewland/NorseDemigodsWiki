# Cursed Hands

Cursed Hands is Hel's own attribute: a tree or log she hits in melee becomes cursed and keeps taking damage on its own
for up to 15 seconds.

<div class="nd-infobox" markdown>

| | |
| --- | --- |
| **Demigod** | [Hel](../demigods/hel.md) |
| **Condition** | Melee hits that chop a tree or log; one curse at a time |
| **Config ID** | `CursedHands` |
| **Config section** | `[Attribute Cursed Hands]` |

</div>

<!-- IMAGE: a cursed tree with the dark Cursed Hands orb -->

## Effect

1. Hit a standing tree or a log with a melee attack that deals chop damage (an axe, for example) and is strong enough to
   damage it ([tool tier](../getting-started/glossary.md#tool-tier)).
2. The tree or log is cursed: every 0.5 s, it takes **35%** of that hit's damage again.
3. The curse lasts 15 s, or until the tree or log is destroyed.

- A full curse adds up to 30 extra hits: ×10.5 (1050%) of the cursing hit's damage.
- One curse at a time: while a tree is cursed, hitting other trees curses nothing.
- Ranged attacks do not curse.

## Related pages

- [Hel](../demigods/hel.md)
- [Glossary](../getting-started/glossary.md)

<!-- Verified against NorseDemigods 1.9.1 -->
