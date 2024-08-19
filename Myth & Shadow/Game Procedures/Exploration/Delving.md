# Delving

When in an especially hostile environment, like the [Shadowcurse](../Hazards/Shadowcurse.md), but not currently engaged in [Combat](../Combat/Combat.md) (i.e. a dungeon) the party is considered [Delving]().

While [Delving](), time is divided into 6-minute segments called [Delve Rounds](../Core%20Procedures/Round.md#Delve%20Round). There are 10 delve rounds per hour.

Whenever an [Action](../Core%20Procedures/Action.md) is mentioned on this page, it is referring to a [Delving Action](../Core%20Procedures/Action.md#Delving%20Action). Likewise, a [Turn](../Core%20Procedures/Turn.md) refers to a [Delve Turn](../Core%20Procedures/Turn.md#Delve%20Turn), and a [Round](../Core%20Procedures/Round.md) a [Delve Round](../Core%20Procedures/Round.md#Delve%20Round).

## Marching Order

When the Party starts [Delving](Delving.md), they should determine a marching order. This will determine who encounters dangerous obstacles like traps and monsters first.

## Tracking Delve Turns

### Party Turn

When [Delving](Delving.md), the GM divides the explorable area into zones. Each zone should be roughly the size the PCs can cover with their [Movement](../Combat/Movement.md) (usually a ~30 foot cube). In a dungeon, each room is usually it's own zone. Particularly large rooms may have multiple zones.

Each PC gets a [Turn](../Core%20Procedures/Turn.md), going in *Marching Order*. A PC can move to any adjacent zone, and perform one [Action](../Core%20Procedures/Action.md). They can use this action to move again. Once each PC has taken their turn, the GM takes the [Dungeon Turn](#Dungeon%20Turn) and then the [Round](../Core%20Procedures/Round.md) ends.

Generally speaking, a [Round](../Core%20Procedures/Round.md) should take 5-10 minutes of real time. It represents the passing of roughly 6 minutes in game time. The GM may enforce a timer if they think it would increase the tension and fun at the table.

### Dungeon Turn

The Dungeon Turn is effectively the GM's turn. It happens at the end of each [Round](../Core%20Procedures/Round.md).

The GM makes the [Delving Hazard Die](#Delving%20Hazard%20Die) roll, updates any relevant parts of the environment, and adjusts any ongoing timers.

#### Delving Hazard Die

According to the danger level, roll the delving hazard die at the end of a [Delve Round](../Core%20Procedures/Round.md#Delve%20Round). On a result of 1, there is a *Random Encounter*.

| Danger Level | Hazard Die Roll |
| ------------ | --------------- |
| Normal       | d20             |
| Risky        | d12             |
| Deadly       | d6              |

#### Random Encounter Distance and Reaction

The encounter monster(s) are placed at a random direction at the edge of the PCs vision. By default, a d12 determines their "[O'clock](https://en.wikipedia.org/wiki/Clock_position)". The [Monster Reactions](../Social%20Procedures/Monster%20Reactions.md) roll should be used unless the monster is an [Undead](../../Resources%20for%20GMs/Creatures/Creature%20Types/Undead.md), or otherwise clearly hostile.

## Primary Delve Actions

### Recover

PCs can use an [Action](../Core%20Procedures/Action.md) to *Recover*. They regain [FP](../../Player%20Characters/Derived%20Statistics/Fatigue%20Points.md) equal to d4 + [Constitution](../../Player%20Characters/The%20Ability%20Scores/Constitution.md). They also recover any reusable resources, such as [Ammo](../../Items%20and%20Gear/Weapon%20Properties/Ammo%20Property.md), that were not destroyed / lost.

PCs can recover multiple rounds in a row.

### Search

PCs can use an [Action](../Core%20Procedures/Action.md) to *Search* their current zone. The GM informs them of one hidden feature in the zone, or informs them if there are no hidden features remaining in the zone.

Hidden features are not obvious, but would reasonably be found by taking roughly 5 minutes to look around carefully. A PC may need to spend subsequent actions to search further details.
*A loose brick, a cracked tile, a suspicious ankle height wire, etc.*

#### Secret Features

Secret features like hidden doors, a letter inside a mattress, and the like are NOT outright revealed by a [Search](Delving.md#Search). The GM should give clues to these features, and the PCs can only find these by following the clues.

The GM may have the PCs roll an investigation [Check](../Core%20Procedures/Check.md) to determine what clue they get if they prepared many clues, there should always be at least one clue.

### Move

Each PC gets to move in addition to their [Action](../Core%20Procedures/Action.md) on their [Turn](../Core%20Procedures/Turn.md).

There are 3 movement speeds the Party can choose from while [Delving](Delving.md).

#### Delve Speed (Default)

The PCs normal [Movement](../Combat/Movement.md) per [Delve Round](../Core%20Procedures/Round.md#Delve%20Round). This allows them to move to an adjacent zone.

At this speed PCs spend most of their time standing still and listening, testing surfaces, and drawing maps. This allows them to automatically detect traps, map their environment, and avoid [Surprise](../Conditions/Surprised.md) in [Initiative](../Combat/Initiative.md).

A PC can spend their [Action](../Core%20Procedures/Action.md) to move a second time in a single [Turn](../Core%20Procedures/Turn.md).

#### Walk

A PC can use an [Action](../Core%20Procedures/Action.md) to walk. A walking PC has **20** zone moves. A walking PC is [Surprised](../Conditions/Surprised.md) by all encounters and springs all traps.

Distance Measurements: Roughly 500 feet, 100 squares at 5 feet, and 50 squares at 10 feet.

*The intent is to allow PCs to quickly backtrack in large dungeons.*

#### Run

A PC can use an [Action](../Core%20Procedures/Action.md) to run. A running PC has **100** zone moves. A running PC is [Surprised](../Conditions/Surprised.md) by all encounters, spring all traps, and cannot map their environment. A PC can run for a number of rounds equal to 1 + their [Constitution](../../Player%20Characters/The%20Ability%20Scores/Constitution.md) before becoming [Exhausted](../Conditions/Exhausted.md).

Distance Measurements: Roughly 3,000 feet, 600 squares at 5 feet, and 300 squares at 10 feet.

*The intent is to allow PCs to quickly flee large dungeons.*

## Real Timer

*Optional*
All effects with a duration of **1 hour** are tracked in real time while delving.
