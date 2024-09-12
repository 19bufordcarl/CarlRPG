# Zone Based Maps

*Optional*
Zone based maps are the recommended way to implement abstract [Geometry](Geometry.md).

## Zone Based Map Procedure

1. Grab a reference image that roughly represents the environment of your map.
2. If the environment is large than a 30 foot cube, break it up into zones that are roughly 30 foot cubes in size.
	1. Label each of these zones with a memorable name.
	2. Denote which zones are adjacent to each other in a clear way.

Some ways to manage zones at the table:

1. Write the names down on index cards and place them on a dry erase battle map. Then draw lines that show how they connect to one another.
2. Create touching transparent text boxes on a VTT.
3. Write them out in a markdown style list.

## Rules for Zones

1. While in a zone, a creature can be in two states:
	1. **Melee**: Creatures are *in melee* as long as they are adjacent to a hostile creature.
		1. Creatures *in melee* can [Melee Attack](../Combat/Melee%20Attack.md) each other.
		2. A creature *in melee* is [Engaged](../Conditions/Engaged.md).
		3. *Tip: Place their minis together on the index card*.
	2. **Range:** Creatures are *at range* as long as they are not adjacent to a hostile creature.
		1. *Tip: Place their minis around the index card*.
2. A creature can use 1 zone of movement to move anywhere within their current zone or an adjacent zone. *This means that movement is no longer discontinuous*.
3. A creature can move a number of zones equal to their [Movement](../Combat/Movement.md) divided by 30.
	1. *Round this to the nearest whole number.*
4. A [Ranged Attack](../Combat/Ranged%20Attack.md) can hit anyone within the same zone or a number of zones away according to the range of the weapon.
5. Areas of Effect can affect multiple creatures. Reference the [Abstract](../../Magic/Spells/Areas%20of%20Effect/{AOE}%20Area%20of%20Effect.md#Abstract) AOE table.

Whenever a measurement is referenced, divide by 30 to get the number of zones it represents.

Whenever 5 feet is referenced, treat it as meaning *in melee*.

## GM Motivation

Zone based maps require more rules text to accurately define, but they tend to prove much faster and easier to run in both VTTs and at a physical table, particularly for the GM. This is an example of the interesting phenomena that problems which are easy to specify can often be incredibly difficult to solve. See [Collatz Conjecture](https://www.youtube.com/watch?v=094y1Z2wpJg)

A measurement system is the easiest to specify for TTRPGs, and so the vast majority use it, including Myth & Shadow. But when you think about it, this is a very hard system to implement.

The method is essentially:

> *Create a scale model of the fictional game world and characters. Using the scale for this world, convert the distances given in feet to measurements for your scale model.*

The phrase "*Create a scale model*" is doing a lot of heavy lifting here. That heavy lifting gets passed down to the GM, who now needs to spend significant time creating that scale model, whether it is digital VTT maps or physical maps.

Instead, you as the GM can opt to use the rules for Zone Based Maps. By enduring a little bit more rules text upfront, you can save yourself lots of time spent making scale models.

See [this article by Sly Flourish](https://slyflourish.com/fate_style_zones_in_5e.html) for another take on how to do zone based maps.
