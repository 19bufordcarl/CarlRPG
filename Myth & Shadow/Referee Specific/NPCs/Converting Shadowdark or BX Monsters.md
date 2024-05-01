# Converting Shadowdark and BX Monsters
## Shadowdark
Converting monsters from Shadowdark is relatively simple, but takes a bit of math.
- [Attack](../../Game%20Procedures/Attack.md) = Add double their attack bonus for attack rolls. Add their attack bonus for damage rolls, or half the attack bonus if it's a [Ranged Attack](../../Game%20Procedures/Ranged%20Attack.md).
	- Unless specified, attacks do [Mundane Damage](../../Damage%20Types/Mundane%20Damage.md).
- [Ability Scores](../../Player%20Characters/Chosen%20Statistics/Ability%20Scores.md) = Same.
	- If a stat is +4 or more, treat it as equal to the creature's level for non [Attack](../../Game%20Procedures/Attack.md) [Checks](../../Game%20Procedures/Check.md).
- [AC](../../Player%20Characters/Derived%20Statistics/Armor%20Class.md) = Creature's [Dexterity](../../Player%20Characters/Chosen%20Statistics/Dexterity.md) x 2
	- Remembering the last step, if it's a +4 or more just uses the creature's level
- [HP](../../Player%20Characters/Derived%20Statistics/Health%20Points.md) = Add 5 HP (I also round to 10 / 15 / 20 etc for ease of tracking)
	- You can add 1d8+1 if you want it to be a bit less predictable
	- PCs start with roughly 10 HP, so NPCs / monsters should too
		- This helps smooth out the math a bit so that everything doesn't die instantly since roll to hit is effectively turned into roll to crit.
	- If they are level 0, keep their HP as is, they can die in 1 hit, it's fine
	- You can treat it as 7 + d6 if you want some variability
	- If it has 1 HP, just keep it as 1 HP.
- Special Abilities = Same, see if an appropriate [Condition](../../Conditions/!Conditions.md) applies, or make a ruling.
	- Stat Damage = Same, 
		- it'll be more punishing, but that's fine, PCs have more options and it heals easy.
- [DC](../../Game%20Procedures/DC.md) = round up to 10, 15, 20. If you think 20 is too low, go 25.
- [Movement](../../Game%20Procedures/Movement.md) = near means 30'
- [Armor X Value](../../Items/Equipment/Individual%20Item%20Cards/Armors/Armor%20Properties/Armor%20X%20Property.md) = Treat this as a 5e modifier with the Creature's AC as the ability score
	- The Math for this is (AC - 10) / 2. Minimum of 0.
	- If they are listed with a shield, give them the [Shield Block](../../Items/Equipment/Individual%20Item%20Cards/Armors/Armor%20Properties/Shield%20Property.md#Shield%20Block) [Reaction](../../Game%20Procedures/Reaction.md).
	- If they state the armor type (leather, chain, plate) you can just use that (1, 2, 3).

I've also converted all the creatures in the starter set for you and 
#### Shadowdark / BX AC to Armor X Value

| Shadowdark AC (If unarmored) | Myth & Shadow Armor X Value |
| ---------------------------: | --------------------------: |
|                        <= 11 |                           0 |
|                        12-13 |                           1 |
|                        14-15 |                           2 |
|                        16-17 |                           3 |
|                        18-19 |                           4 |
|                        20-21 |                           5 |
|                         etc. |                        etc. |
### Why did you change AC? It's what everyone uses!
*Missing is a null result and it is very challenging to make it interesting and not just have players check out. I take cues from Pokemon for turn based combat. If a move has less than 100% accuracy, I am significantly less likely to use it. 95% is acceptable but not ideal. Moves with less than 90% accuracy are expected to have a big payoff.*

*Reducing damage is much more fun for players. Mathematical progress is almost always happening rather than just a straight miss. Even if that damage is reduced to 0, that still has a very different feeling to the player, and it is only likely to happen on a high level monster. This leads to an interesting narrative too, "You go to pierce the dragon's hide, but it's scales deflect the blade".* 

*You can have this same explanation with AC, but it will happen roughly 30-50% of the time against goblins and bandits too. It doesn't feel special when you miss the dragon, missing a lot is just part of the game. I feel like the severe feeling of helplessness that comes from missing and effectively losing your turn should be reserved for powerful foes, like dragons. This also helps speed up routine encounters, the same amount of damage will still be dealt to both sides, just over fewer rounds. This also makes winning initiative much more important and gives players extra incentive to scheme to get surprise, and not to be reckless so they avoid being surprised.*

*Just because it's old doesn't mean it's good. This was a great system when it was originally invented, where a hit = death, and so you could roll a bunch of d20s and count all the hits for your wargaming minis and see how many you killed vs. the other side killed. Once you add the ability to take multiple hits, the miss rate being this high makes combat a slog compared to minor damage reduction.*

*It also helps with the narrative in my opinion as players don't have such a massive power spike from levels 1-3. The biggest jump in Shadowdark is level 2. Characters will usually double their expected number of combat turns they can survive. A fighter with +2 CON who rolled poorly on their initial HP (say they got a 4) could go from 4 to 12 HP if they max roll their next HP. Yes this is a high roll, and yes the core mechanic of the game is rolling dice, I enjoy some randomness, but tripling your HP on a high roll I think is way beyond a fun level of variance for most games. If you wanna play this way, I think of that as more level 0 nowadays. Don't get me wrong, I've played a bunch of level 0 games in my time, their fun, but I think this kind of swingy-ness belongs at level 0, not level 1.*

*This also makes for very awkward narrative in my opinion. Going from levels 1 to 2 is usually the easiest level to gain. Level 0 sessions will often be a prologue to establish the PCs for a campaign, and might take places months or years before the actual campaign start. Or sometimes they'll involve the PCs surviving a funnel and getting some great reward / power that turns them into level 1 characters. Plenty of time / narrative to justify how they got so powerful. Level 1 to level 2 on the other hand is usually expected by players to be handled pretty easily and handwaved. Even in Shadowdark it doesn't specify even needing to rest, you just level up. Even if it is a rest it's just a long rest. I'm fine with the stated design goal of flattening the math across levels, but the HP math is anything but flattened here. It's very swingy and while some randomness is good, a player tripling their HP between levels I think is too much.*

*HP improvements should be more gradual, along with damage improvements. This keeps the math truly flattened. Combats between equally skilled opponents should last roughly the same length (always short) from levels 1-10. Combats between skill disparate opponents will also be short, provided they are fought "fairly". They might take longer if the PCs go through elaborate methods to gain a tactical advantage, which is the fun part!*

*To sum up, in base Shadowdark, low level fights can drag on for ages with both sides constantly missing, or be over in a single round because you get hit once and have 5 HP. It's too much swingy-ness for my taste. By increasing HP and hit chance, we make the number of rounds you can survive a little bit more predictable, while still having the randomness of the damage die. Your character won't get massively more healthy from levels 1-2. Everything will be a bit more gradual. The math will stay a bit flatter, and when designing monsters we can more easily predict how deadly they will be to the party if engaged in combat so we as referees can decide how to communicate the danger. No longer will your Minotaur do 0 damage because you didn't roll above an 8 against a party of fighters.*