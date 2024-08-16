# Area of Effect (AOE)

Spells with a designated AOE apply some portion of their spell text to all creatures in the affected area. There are three types of area of effect. [Auras]({AOE}%20Area%20of%20Effect.md#Auras), [Lines]({AOE}%20Area%20of%20Effect.md#Lines), and Areas. Any creature inside an aura or line is referred to as an *Affected Target, Affected Creature, or Affected Object*. A target refers to both creatures and objects.

## Auras

An aura is the default term for an area of effect. The term is specifically non-geometrical so that it can apply to whatever method you use to represent the geometry of your game. Creatures and objects inside an aura are affected unless the effect specifies only creatures instead of targets.

All examples will use a 15 foot aura effect.

### Measurement (Default)

In a measurement system, a spell that "creates a 15 foot aura on a point you can see within range" creates a sphere with a 15 foot radius whose origin is the chosen point. Creatures and objects within 15 feet are affected.

### Gridded

In a gridded system, a spell that "creates a 15 foot aura on a point you can see within range" creates a cube whose sides lengths are twice the aura size (30 feet long in this case).
*Yes this gives you an extra 4 affected squares, the corners are affected now.*

### Abstract

If using abstract distance, reference the following table.

| Aura Size | Maximum Number of Normal Size Creatures Affected | Average # |
| --------: | -----------------------------------------------: | --------: |
|    5 feet |                                                4 |         2 |
|   10 feet |                                                8 |         4 |
|   15 feet |                                               24 |         8 |
|  20+ feet |                                            A lot |        16 |

## Lines

A line is a rectangular area of effect. A line has a specified length. The line itself has negligible width typically, but any creature within 5 feet of the line's path is considered affected.

If playing on a square grid then you draw any straight line with a 5 foot width. Any squares that have at least 25% of their area covered by the line are considered affected.

## Areas

Areas are rectangular prisms that denote an area of effect. They are seldom used. They are expressed as:

Create an area that is $length$ long, $width$ wide, and $height$ tall. Any creature in that area is considered affected.

# On Geometry


