# Overland Journeys (Hex Crawls)

## Point Crawl

If the party is traveling along a road or safe area, it is generally better to abstract the journey into the total days / rations it will take and generate 1 encounter at the halfway point.

- This encounter should not always be hostile

## Hex Crawl

While on a journey (hex crawl), days are divided into six [Watches](Watches.md):

- Three for day
- Three for night

*If there is very little to no danger or content in the average hex, this level of granularity provides little gameplay value. Use watches and hex crawl rules for overland travel only when traversing dangerous areas with lots of activity in each hex.*

## Overland Journey Danger Level

Roll the journey hazard die according to the danger level table below.

| Danger Level | When to roll hazard die   |
| ------------ | ------------------------- |
| Safe         | Never                     |
| Normal       | At dawn                   |
| Risky        | At dawn and at dusk       |
| Deadly       | Every [Watch](Watches.md) |

## Journey Hazard Die

At the start of each day (6 [Watches](Watches.md)), roll the Journey Hazard Die (d6).

| d6  | Result                                                            |
| --- | ----------------------------------------------------------------- |
| 1   | Encounter: The GM should have something prepared, or a table |
| 2-6 | Free: No effect                                                   |

### Overworld Encounter Tips

The nature of overworld encounters is intended to allow the GM to build out the world. The following is the encounter generation for the default setting. You can use it, or use it as a reference point for building your own.

#### Encounter Time of Day

In normal areas, roll 2d12 for the 24 hour time of the encounter. This makes nighttime ambushes more rare as they are the most punishing.

In risky areas, the dawn encounter happens at noon, the dusk encounter happens at midnight.

In deadly areas, the encounter happens at the beginning of the specified watch.

#### Encounter Random Table

There are numerous historic random tables for generating encounters based on the environment. Myth & Shadow does not specify any in particular, you are encouraged to use your favorites or build your own. It is assumed that the probability distribution of your encounters tables is roughly:

| d12 | Encounter                             |
| --- | ------------------------------------- |
| 1   | Extreme Danger: Far above party level |
| 2   | High Danger: Above party level        |
| 3   | High Danger: Above party level        |
| 4   | Moderate Danger: About party level    |
| 5   | Moderate Danger: About party level    |
| 6   | Moderate Danger: About party level    |
| 7   | Moderate Danger: About party level    |
| 8   | Moderate Danger: About party level    |
| 9   | Moderate Danger: About party level    |
| 10  | Low Danger: Below party level         |
| 11  | Low Danger: Below party level         |
| 12  | Mystical Encounter                    |

Not all encounters are assumed to be monsters. Some could be environmental, perhaps the onset of a blizzard, and some could even be helpful, perhaps a traveling merchant, or a mythical spirit animal. Remember to make [Creature Reactions](../Social%20Systems/Creature%20Reactions.md), or [Social Reactions](../Social%20Systems/Social%20Reactions.md), whichever is more appropriate. This helps keep the variety of the game high.

#### Creature Distance

Have each PC make a [Wisdom](../Player%20Characters/Chosen%20Statistics/Wisdom.md) check, with a [DC](DC.md) equal to 10 + (2 x the creature's [Level](../Player%20Characters/Derived%20Statistics/Level.md)).

- If any player succeeds, they spot the creature at a distance of about 200 feet.
	- (100 + 3d6 x 10 feet away if random is desired).
	- If any player succeeded by 5 or more, the creature is unaware of them.
		- Staying undetected for an extended time requires stealth ([Dexterity](../Player%20Characters/Chosen%20Statistics/Dexterity.md)) [Checks](Check.md) from each PC within sight range of the creature.
- If all players fail, they do not spot the creature until it is 30 feet away.
	- They are not surprised for [Initiative](Initiative.md) unless they were sleeping or otherwise occupied
	- Or , if the creature was aware of them and deliberately being stealthy.

#### Creature Details

Creature's should have ongoing behavior, complications, and a goal. This makes them dynamic when engaged if the reaction roll was such that they are not immediately hostile and gives you an idea of how to use them to progress the adventure.

| d12 | Activity                    | Complication    | Goal                                         |
| --: | --------------------------- | --------------- | -------------------------------------------- |
| 1-2 | Hunting something           | Hungry          | FOOD (in dire need of a meal)                |
| 3-4 | Hiding from something       | Being followed  | Coins (d10 x level x 100)                    |
|   5 | Guarding something          | Hates boss      | Magic items (equal to level)                 |
|   6 | Socializing (if in a group) | Injured         | Random item (for some reason)                |
|   7 | Digging for something       | Caught in trap  | Territory (get out of my swamp)              |
|   8 | Building or nesting         | Tending to ally | Information (rival faction / region)         |
|   9 | Carrying supplies           | Broken gear     | Blood (they need the PCs blood)              |
|  10 | Eating something            | Understaffed    | Trade (a random selection of goodies)        |
|  11 | Fighting off creatures      | Captured        | Mission (they are in service to another NPC) |
|  12 | Sleeping                    | Sickly / Young  | Directions (they are lost)                   |
