# Converting Shadowdark and BX Monsters
## Shadowdark
Converting monsters from Shadowdark is relatively simple, it can more or less be used as is.
- [Attack](../../Game%20Procedures/Attack.md) = Same.
	- We don't add attack to damage because monster's have their own unique damage scaling usually built in (multiattack). We have PCs start with more effective HP (basically level 2ish) so that they don't just die in one hit, but their HP grows much slower, and technically has a lower cap than a high roller, so we don't want to increase damage to keep the math roughly equivalent across systems.
- [Ability Scores](../../Player%20Characters/Chosen%20Statistics/Ability%20Scores.md) = Same.
	- If a stat is +4 or more, treat it as equal to the creature's level for non [Attack](../../Game%20Procedures/Attack.md) [Checks](../../Game%20Procedures/Check.md).
- [AC](../../Player%20Characters/Derived%20Statistics/Armor%20Class.md) = Same
	- *Optional*
		- If they are listed with a shield, give them the [Shield Block](../../Items/Individual%20Item%20Cards/Armors/Armor%20Properties/Shield%20X%20Property.md#Shield%20Block) [Reaction](../../Game%20Procedures/Reaction.md).
		- If you do, also reduce their AC by 1 or 2 depending on the tier of enemy.
- [HP](../../Player%20Characters/Derived%20Statistics/Health%20Points.md) = Same
	- Use 5HP instead of 4HP for the minimum
- Special Abilities = Same, see if an appropriate [Condition](../../Conditions/!Conditions.md) applies, or make a ruling.
	- Stat Damage = Same, 
		- it'll be more punishing, but that's fine, PCs have more options and it heals easy.
- [DCs](../../Game%20Procedures/DC.md) = Same
- [Movement](../../Game%20Procedures/Movement.md) = near means 30'
	- *Optional, use if using variable [Movement](../../Game%20Procedures/Movement.md).*
	- If the creature is unarmored and has positive [Dexterity](../../Player%20Characters/Chosen%20Statistics/Dexterity.md), add (5' x [Dexterity](../../Player%20Characters/Chosen%20Statistics/Dexterity.md)) to this.

That being said, I have converted monsters to this system for better reference and compatibility.

### Why did you change AC to be half damage? Does this break the math?
*Missing is a null result and it is very challenging to make it interesting and not just have players check out. I take cues from Pokemon for turn based combat. If a move has less than 100% accuracy, I am significantly less likely to use it. 95% is acceptable but not ideal. Moves with less than 90% accuracy are expected to have a big payoff. In this system, ranged is a big payoff.*

*Reducing damage is much more fun for players. Mathematical progress is almost always happening rather than just a straight miss. Even if that damage is reduced to 0, that still has a very different feeling to the player, and it isn't too likely to happen. This leads to an interesting narrative too, "You go to pierce the dragon's hide, but it's scales deflect the blade".* 

*You can have this same explanation with normal AC, but it will happen roughly 30-50% of the time against goblins and bandits too. It doesn't feel special when you miss the dragon, missing a lot is just part of the game. I feel like the severe feeling of helplessness that comes from missing and effectively losing your turn should be reserved for powerful foes, like dragons, or poor decisions, like wielding a weapon you aren't experienced with. This also helps speed up routine encounters, the same amount of damage will still be dealt to both sides, just over fewer rounds. This also makes winning initiative much more important, which is why we make it predictable so players can plan around this. When players lose initiative, they should realize the danger and usually run. This also gives players extra incentive to scheme to get surprise, and not to be reckless so they avoid being surprised.*

*Just because it's old doesn't mean it's good. This was a great system when it was originally invented, where a hit = death, and so you could roll a bunch of d20s and count all the hits for your wargaming minis and see how many you killed vs. the other side killed. Once you add the ability to take multiple hits, the miss rate being this high makes combat a slog compared to halving the damage.*

*I ran a bunch of combat simulations. This system primarily just increases the variance of outcome depending on which side goes first. It doesn't impact the mean outcome much at all. I think initiative mattering is good, as players should always be trying to get the jump if they are willingly engaging in a combat. A fair fight is a lost fight.*

*Additionally, this let's referees be less concerned about bonuses to AC. In most d20 systems, increasing AC to a certain point will make that creature basically unkillable. And if you don't know where the math starts to get out of hand for that system it is really easy to accidentally set an AC to high and create a really swingy combat. This reduces the impact of each AC point dramatically, and brings it much closer in line with a percent damage reduction armor system. Percent damage reduction is ideal in my opinion, but it is too hard to do without computers. AC is effectively percent damage reduction, but it scales from 0% to 95% in a linear way, which means that survivability in turns will scale geometrically (1/x). When you get to 95% damage reduction and only get hit on a crit you have roughly double the percent reduction, but it takes roughly 10x the number of turns to kill you compared to 50% damage reduction. Difficulty of obtaining this damage reduction would need to scale exponentially to have the effective turns scale more or less linearly. Unfortunately, humans tend to undervalue just how quick this grows, and hence you get +2 plate armors breaking the game from inexperienced GMs.* 

*However, this new system changes that to be 0% to ~50%. This reduces that top end armor has in normal d20 systems, while still retaining the same trappings, ease of conversion, geometric scaling, and dependency on attack bonus for interesting tactical decisions, without introducing game breaking potential for absurdly high ACs that might as well read as a special ability: immortal.*