# Converting Shadowdark and BX Monsters
## Shadowdark
Converting monsters from Shadowdark is relatively simple, but takes a bit of math.
- [AC](../../Player%20Characters/Derived%20Statistics/Armor%20Class.md) = Creature's Dexterity x 2
- [Ability Scores](../../Player%20Characters/Chosen%20Statistics/Ability%20Scores.md) = The higher of the listed ability score or their Level 
	- (Only for abilities with positive modifiers)
- [HP](../../Player%20Characters/Derived%20Statistics/Health%20Points.md) = HP + Level (They'll take more hits with lower AC)
- Attacks = Same, but add it's calculated ability score (often just level) to all damage rolls.
- Special Abilities = Same, see if an appropriate [Condition](../../Conditions/!Conditions.md) applies, or make a ruling.
	- Stat Damage = Same, 
		- it'll be more punishing, but that's fine, PCs have more effective HP in MnS.
- [DC](../../Game%20Procedures/DC.md) = round up to the next one of 10, 15, 20.
- [Movement](../../Game%20Procedures/Movement.md) = near means 30'
- [Armor X Value](../../Items/Equipment/Individual%20Item%20Cards/Armors/Armor%20Properties/Armor%20X%20Property.md) = Treat this as a 5e modifier with the Creature's AC as the ability score but round up instead of down.
	- The Math for this is (AC - 10) / 2 round up. Minimum of 0.
	- If they are listed with a shield you can either just give them the higher AC for simplicity, or decrease the AC by 1 and give them the [Shield Block](../../Items/Equipment/Individual%20Item%20Cards/Armors/Armor%20Properties/Shield%20Property.md#Shield%20Block) [Reaction](../../Game%20Procedures/Reaction.md).
#### Shadowdark / BX AC to Armor X Value

| Shadowdark AC | Myth & Shadow Armor X Value |
| ------------: | --------------------------: |
|         <= 10 |                           0 |
|         11-12 |                           1 |
|         13-14 |                           2 |
|         15-16 |                           3 |
|         17-18 |                           4 |
|         19-20 |                           5 |
|          etc. |                        etc. |
### Why did you change AC? It's what everyone uses!
*Missing is a null result and it is very challenging to make it interesting and not just have players check out. I take cues from Pokemon for turn based combat. If a move has less than 100% accuracy, I am significantly less likely to use it. 95% is acceptable but not ideal. Moves with less than 90% accuracy are expected to have a big payoff.*

*Reducing damage is much more fun for players. Mathematical progress is almost always happening rather than just a straight miss. Even if that damage is reduced to 0, that still has a very different feeling to the player, and it is only likely to happen on a high level monster. This leads to an interesting narrative too, "You go to pierce the dragon's hide, but it's scales deflect the blade".* 

*You can have this same explanation with AC, but it will happen roughly 30-50% of the time against goblins and bandits too. It doesn't feel special when you miss the dragon, missing a lot is just part of the game. I feel like the severe feeling of helplessness that comes from missing and effectively losing your turn should be reserved for powerful foes, like dragons. This also helps speed up routine encounters, the same amount of damage will still be dealt to both sides, just over fewer rounds. This also makes winning initiative much more important and gives players extra incentive to scheme to get surprise, and not to be reckless so they avoid being surprised.*

*Just because it's old doesn't mean it's good. This was a great system when it was originally invented, where a hit = death, and so you could roll a bunch of d20s and count all the hits for your wargaming minis and see how many you killed vs. the other side killed. Once you add the ability to take multiple hits, the miss rate being this high makes combat a slog compared to minor damage reduction.*