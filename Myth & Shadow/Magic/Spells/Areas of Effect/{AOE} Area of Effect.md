# Area of Effect (AOE)

Spells with a designated AOE apply some portion of their spell text to all creatures in the affected area. There are three types of area of effect. [Auras]({AOE}%20Area%20of%20Effect.md#Auras), [Lines]({AOE}%20Area%20of%20Effect.md#Lines), and Areas. Any creature inside an aura or line is referred to as an *Affected Target, Affected Creature, or Affected Object*. A target refers to both creatures and objects.

## Auras

An aura is a spherical area of effect. The term is specifically non-geometrical so that it can apply to whatever method you use to represent the geometry of your game. Creatures and objects inside an aura are affected unless the effect specifies only creatures instead of targets.

All examples will use a 15 foot aura effect.

### Measurement

*Default*
On a measurement map, a spell that "creates a 15 foot aura on a point you can see within range" creates a sphere with a 15 foot radius whose origin is the chosen point. Creatures and objects within 15 feet are affected.

### Gridded

On a gridded map, a spell that "creates a 15 foot aura on a point you can see within range" creates a cube whose sides lengths are twice the aura size (30 feet long in this case).
*Yes this gives you an extra 4 affected squares, the corners are affected now.*

### Abstract

On an abstract map, reference the following table.

| Descriptor | Aura Size | # Affected | # Affected If All Are In Melee |
| ---------- | --------: | ---------: | -----------------------------: |
| Small      |    5 feet |          2 |                      At most 4 |
| Medium     |   10 feet |          3 |                     At most 16 |
| Large      |   15 feet |          5 |                     At most 32 |
| Huge       |  20+ feet |         8+ |                            64+ |

## Lines

A line is a rectangular area of effect. A line has a specified length. The line itself has negligible width typically, but any creature within 5 feet of the line's path is considered affected.

If playing on a square grid then you draw any straight line with a 5 foot width. Any squares that have at least 25% of their area covered by the line are considered affected.

Lines are seldom used because of their particularly difficulty in abstract maps.

## Areas

Areas are rectangular prisms that denote an area of effect. They are expressed as:

Create an area that is $length$ long, $width$ wide, and $height$ tall. Any creature in that area is considered affected.
