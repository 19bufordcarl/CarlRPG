# Morale

Morale is the system to handle when NPCs will attempt to flee or surrender.

## Breaking Points

Breaking points are situations in [Combat](../Combat/Combat.md) that trigger a morale [Check](../Core%20Procedures/Check.md). The defaults are:

- A solo monster (or NPC) going below [Half](../Core%20Procedures/Half.md) HP
- A group losing [Half](../Core%20Procedures/Half.md) their members
- A group losing their leader ([Unconscious](../Conditions/Unconscious.md) or [Dying](../Conditions/Dying.md) counts as losing too)

## Enemy Morale

When a breaking point occurs, the GM makes a [DC](../Core%20Procedures/DC.md) 15 [Wisdom](../../Player%20Characters/Chosen%20Statistics/Wisdom.md) check for the creature or the leader if there is a group. On a failure, the *whole group's* morale is broken.

On a failed morale check, the enemies will go into life preservation mode. They should first try to flee, if they deem that impossible or unlikely then they may attempt surrender.

- *See [On Advanced Interrogation](../../Resources%20for%20GMs/Foreword/Author's%20Notes/On%20Advanced%20Interrogation.md)*

## Ally Morale ([NPC Hirelings](Stronghold%20Rules/NPC%20Hirelings.md))

When the party undergoes a breaking point, if any [NPC Hirelings](Stronghold%20Rules/NPC%20Hirelings.md) are present, a PC must make a [Charisma](../../Player%20Characters/Chosen%20Statistics/Charisma.md) check with a [DC](../Core%20Procedures/DC.md) equal to 10 + (2 x [Level](../../Player%20Characters/Derived%20Statistics/Level.md) of the enemy creature / leader). On a failure, all the NPCs with the party have their morale broken. These NPCs will cease fighting and attempt to flee or surrender.
