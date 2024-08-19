# Zone Based Maps

*Optional*
Zone based maps are the recommended way to implement abstract [Geometry](Geometry.md).

## Zone Based Map Procedure

1. Grab a reference image that roughly represents the environment of your map.
2. If the environment is large than a 30 foot cube, break it up into zones that are roughly 30 foot cubes in size.
	1. Label each of these zones with a memorable name.
	2. Denote which zones are adjacent to each other in a clear way. Some ideas:
		1. *Write them down on index cards an a dry erase battle map and draw lines that connect them to one another*.
		2. *Create touching transparent text boxes on a VTT*.
3. Each zone has two sub-zones:
	1. **Melee**: Creatures in melee are at the center of the zone.
		1. A creature in melee is [Threatened](../Conditions/Threatened.md) if there is a hostile creature also in melee
		2. *Tip: Place their minis on the index card*.
	2. **Range:** Creatures at range are at the edges of the zone.
		1. A creature at range is [Threatened](../Conditions/Threatened.md) only by creatures that moved to [Melee Attack](../Combat/Melee%20Attack.md) it.
		2. *Tip: Place their minis around the index card*.
4. Creatures can move a number of zones equal to their [Movement](../Combat/Movement.md) divided by 30.
	1. *Round to the nearest whole number.*
5. A creature can use 1 zone of movement to move anywhere within their current zone or an adjacent zone. *This means that movement is no longer discontinuous*.
	1. *Note: Creatures at range can move away from [Threaten](../Conditions/Threatened.md) and stay at range in that zone.*
6. [Ranged Attacks](../Combat/Ranged%20Attack.md) can hit anyone within the same zone or a number of zones away according to the range of the weapon divided by 30, rounded down.
7. Areas of Effect can affect multiple creatures in the same zone. They can either:
	1. Affect all creatures in **Melee**, or
	2. Use the [Abstract](../../Magic/Spells/Areas%20of%20Effect/{AOE}%20Area%20of%20Effect.md#Abstract) AOE table to determine the number of creatures affected.

## GM Motivation

Zone based maps require more rules text to accurately define, but they tend to prove much faster and easier to run in both VTTs and at a physical table, particularly for the GM. This is an example of the phenomena in Mathematics, and problem solving more generally, that problems that are easy to specify can require incredibly complicated solutions. See [Collatz Conjecture](https://www.youtube.com/watch?v=094y1Z2wpJg)

A Measurement system is the easiest to specify, and so it is the assumed method throughout Myth & Shadow for adjudicating ranges and distances, but when you think about it, it is a very hard method to get right.

The method is essentially:

> *Create a scale model of the fictional game world. Using the scale for this world, convert the distances given in feet to measurements for your scale model.*

The phrase "*Create a scale model*" is doing a lot of heavy lifting for the simplicity of a measurement system's rules text. That heavy lifting gets passed down to the GM, who now needs to spend significant time creating that scale model, digital or physical.

Instead, you as the GM can opt to use the rules for Zone Based Maps. By enduring a little bit more rules text upfront, you can save yourself lots of time spent making maps.

See [this article by Slyflourish](https://slyflourish.com/fate_style_zones_in_5e.html) for another take on how to do zone based maps.
