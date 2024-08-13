# Area of Effect (AOE)

Spells with a designated AOE apply some portion of their spell text to all creatures in the affected area. There are three types of area of effect. [Auras]({AOE}%20Area%20of%20Effect.md#Auras), [Lines]({AOE}%20Area%20of%20Effect.md#Lines), and Areas. Any creature inside an aura or line is referred to as an *Affected Target, Affected Creature, or Affected Object*. A target refers to both creatures and objects.

## Auras

An aura is the default term for an area of effect. The term is specifically non-geometrical so that it can apply to whatever method you use to represent the geometry of your game.

All examples will use a 15 foot aura effect.

### Measurement (Default)

In a measurement system, a spell that "creates a 15 foot aura on a point you can see within range" creates a sphere with a 15 foot radius whose origin is the chosen point. Creatures and objects within 15 feet are effected.

### Gridded

In a gridded system, a spell that "creates a 15 foot aura on a point you can see within range" creates a cube whose sides lengths are twice the aura size (30 feet long in this case).
*Yes this gives you an extra 4 affected squares, the corners are affected now.*

### Abstract

If using abstract distance, reference the following table.

| Aura Size | Maximum Number of Normal Size Creatures Affected |
| --------: | -----------------------------------------------: |
|    5 feet |                                              1d4 |
|   10 feet |                                              2d4 |
|   15 feet |                                             2d12 |
|  20+ feet |                                              +10 |

## Lines

A line is a rectangular area of effect. A line has a specified length. The line itself has negligible width typically, but any creature within 5 feet of the line's path is considered affected.

If playing on a square grid then you draw any straight line with a 5 foot width. Any squares that have at least 25% of their area covered by the line are considered affected.

## Areas

Areas are rectangular prisms that denote an area of effect. They are seldom used. They are expressed as:

Create an area that is $length$ long, $width$ wide, and $height$ tall. Any creature in that area is considered affected.

# On Geometry

Any AOE that has square as the epicenter would correlated to an cube size ending in 5 (5', 15', 25', etc.) A 5' cube is equivalent to just your square, and so isn't used. If a spell states, "within 15 feet of (a point)", that point is taken to be the intersection point of 4 squares. This equates to a 30 foot (30') cube centered on that intersection. If the spell states "within 30 feet of (caster)", then this equates to a 65 foot cube centered on the caster. For ease of language and compatibility with other measurement systems, within X feet is always the specification. It make measurement much easier and less finicky to decide which creatures can and can't be affected.

## Diagonal Movement

If playing on a square grid, it is recommended to use chess king movement as opposed to Euclidean geometry. Since a diagonal is the same distance as a non-diagonal in this system, that means that spheres are abstracted to be cubes, hence why everything is cube when gridded.

## Abstract Geometry

If playing with abstract distances, it is recommended to use zones of 30 feet (roughly 6 inches in real space if using minis, roughly the length of a pen). A spell with a 5 foot radius should affect all creatures in melee range of the target. A spell with a 30 foot radius should affect all creatures within movement range of the target. If it is a 15 foot radius, it can affect [Half](../../../Foreword/Rule%20for%20rules.md#Halving) the creatures within movement range of the target.
