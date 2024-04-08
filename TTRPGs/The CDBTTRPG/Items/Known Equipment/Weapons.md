# Weapons

These are mundane weapons. A martial PC is likely to end up using a special weapon for their character. These are a starting point for a character, and provide context for the baseline in this world. They can be reskinned as appropriate for the character and setting.

## Weapon Properties
A weapons properties determine how exactly a weapon can be used.

- #Melee means the weapon can [Melee Attack](../../Game%20Structure/Melee%20Attack.md) targets adjacent to you.  
- #Ranged means the weapon can make [Ranged Attacks](../../Game%20Structure/Ranged%20Attack.md) with the specified range.
- #Reach means the weapon can [Melee Attack](../../Game%20Structure/Melee%20Attack.md) a target that is up to 10 feet away from you.
	- Ex. Your square (5 foot gap square) Target square
- #Edged means that the weapon can be used for [Slashing](../../Damage%20Types/Slashing.md) or [Piercing](../../Damage%20Types/Piercing.md) damage.
	- The pommel can still be used for 1 + [Strength](../../Player%20Character%20Components/Chosen%20Statistics/Strength.md) [Bludgeoning](../../Damage%20Types/Bludgeoning.md) damage.
- #Blunt means the weapon can be used for [Bludgeoning](../../Damage%20Types/Bludgeoning.md) or [Piercing](../../Damage%20Types/Piercing.md) damage.
- #Versatile means the weapon can be wielded with one or two hands. 
	- If wielded with two hands, you make attack [Checks](../../Game%20Structure/Check.md) with [Advantage](../../Dice%20Rolls/Advantage.md).
- #TwoHanded means that you must use 2 hands to wield the weapon.
	- When you succeed on an attack [Check](../../Game%20Structure/Check.md), roll two damage dice and use the higher result.
		- The heavy weight of these weapons decreases the variability of their damage. 
	- Weapons are assumed to be one handed unless specified.
- #Thrown means that you can throw the weapon to make a ranged attack with [Strength](../../Player%20Character%20Components/Chosen%20Statistics/Strength.md).
- #ExpertiseX means that you attack with [Disadvantage](../../Dice%20Rolls/Disadvantage.md) unless you have X [Dexterity](../../Player%20Character%20Components/Chosen%20Statistics/Dexterity.md).
- #Loading means you must take an [Action](../../Game%20Structure/Action.md) to reload this weapon.
- #DualWield means that you can wield this weapon in your off hand. 
	- When you succeed on an attack [Check](../../Game%20Structure/Check.md), roll both damage dice and use the higher result.
- #Finesse means that you can choose to use [Dexterity](../../Player%20Character%20Components/Chosen%20Statistics/Dexterity.md) for all weapon attacks and damage.

## Melee Weapons

All these weapons have the #Melee property, omitted for brevity.

| Weapons                  | Damage | Slots | Price | Properties                               |
| ------------------------ | ------ | ----- | ----- | ---------------------------------------- |
| Club, Hammer, Torch      | d4     | 1     | 5     | #Blunt #DualWield                        |
| Wooden Staff, Whip       | d4     | 1     | 5     | #Blunt #Reach #DualWield #Versatile      |
| Dagger, Gladius, Hatchet | d4     | 1     | 10    | #Edged #DualWield #Finesse #Thrown       |
| Pitchfork, Javelin       | d4     | 1     | 10    | #Edged #Reach #Versatile #Thrown         |
| Mace, Flail              | d6     | 1     | 50    | #Blunt #Versatile                        |
| Metal Staff, Pole        | d6     | 1     | 50    | #Blunt #Versatile #Reach                 |
| Longsword, War Axe       | d6     | 1     | 50    | #Edged #Versatile #DualWield #Expertise1 |
| Spear, Glaive            | d6     | 1     | 50    | #Edged #Versatile #Reach #Expertise1     |
| Warhammer, Maul          | d8     | 2     | 100   | #Blunt #TwoHanded                        |
| Greatsword, Greataxe     | d8     | 2     | 100   | #Edged #TwoHanded #Expertise1            |
| Halberd, Pike            | d8     | 3     | 100   | #Edged #TwoHanded #Reach #Expertise1     |
## Ranged Weapons

All these weapons have the #Ranged property, omitted for brevity.

| Weapon         | Range | Damage | Slots | Price | Properties                       |
| -------------- | ----- | ------ | ----- | ----- | -------------------------------- |
| Sling          | 120'  | d4     | 1     | 5     | #Expertise1                      |
| Shortbow       | 120'  | d6     | 1     | 50    | #Expertise2  #TwoHanded          |
| Light crossbow | 60'   | d6     | 1     | 100   | #Expertise0  #TwoHanded #Loading |
| Longbow        | 240'  | d8     | 1     | 100   | #Expertise3 #TwoHanded           |
| Heavy crossbow | 120'  | d8     | 2     | 500   | #Expertise0  #TwoHanded #Loading |
## Ammo

| Ammo Type         | Slots | Price |
| ----------------- | ----- | ----- |
| 20 arrows / bolts | 1     | 50    |
| 20 sling stones   | 1     | 10    |
