# Evoker

## Core Evoker Traits

| **Primary Ability**            | Wisdom |
| ------------------------------ | ------ |
| **Hit Points**                 | 1d6 |
| **Saving Throw Proficiencies** | Wisdom, Charisma |
| **Skill Proficiencies**        | Choose 2 skills |
| **Weapon Proficiencies**       | Choose 1 category |
| **Starting Equipment**         | Padded Jacket, Sabre, Dagger, Grimoire |

## Evoker Features

| Level | Proficiency | Mana | Class Features                 |
| ----- | ----------- | ---- | ------------------------------ |
| 1     | +2          | 2    | Evocation, Elemental Specialty |
| 2     | +2          | 3    | —                              |
| 3     | +2          | 4    | Ability Score Improvement      |
| 4     | +2          | 5    | Specialty Power                |
| 5     | +3          | 6    | —                              |
| 6     | +3          | 7    | —                              |
| 7     | +3          | 8    | Ability Score Improvement      |
| 8     | +3          | 9    | —                              |
| 9     | +4          | 10   | Specialty Power                |
| 10    | +4          | 12   | Evoker's Mastery               |

## Level 1: Evocation

You channel raw elemental power. Wisdom is your spellcasting ability for evoker features. Your spell attack bonus is your Wisdom modifier + proficiency bonus. Your spell save DC is 8 + your Wisdom modifier + your proficiency bonus.

**Mana Points.** Your magic is powered by mana, as shown in the Evoker Features table. You can spend a number of mana points equal to your proficiency bonus on any single turn. You regain up to 3 mana points when you finish a short rest, and all expended mana points when you finish a long rest.

**Arcane Bolt.** As a magic attack action, make a ranged attack against a target within 120 feet. On a hit, the target takes 1d10 + your Wisdom modifier damage. The damage type is fire, cold, or lightning, matching your Elemental Specialty.

Before rolling the attack, you can spend 1 or more mana points to increase the damage by 1d10 per point spent. If you spend at least 1 mana point, the target takes half damage on a miss.

At 5th level, the base damage increases to 2d10. At 9th level, it increases to 3d10.

## Level 1: Elemental Specialty

Choose Pyromancy, Cryomancy, or Electromancy. You gain a passive ability now, a signature spell at 4th level, and an upgrade to that spell at 9th level.

## Level 3: Ability Score Improvement

You gain a +1 bonus to two abilities of your choice.

## Level 4: Specialty Power

You gain your specialty's signature spell.

## Level 7: Ability Score Improvement

You gain a +1 bonus to two abilities of your choice.

## Level 9: Specialty Power

Your signature spell improves.

## Level 10: Evoker's Mastery

You gain resistance to your specialty's damage type (fire, cold, or lightning). Once per long rest, you can use your Greater signature spell without spending mana.

---

# Elemental Specialties

## Pyromancy

You are trained in the ways of magical fire. Fire is wild, ambitious, and alive.

### Level 1: Burning Flames

Whenever you roll fire damage, if any die shows its maximum result, roll an additional die of that type and add it to the damage. Repeat this for each additional maximum roll.

### Level 5: Fireball

As a magic action, spend 1 or more mana points and choose a point within 120 feet. Each creature within a 20-foot-radius sphere centered on that point must make a Dexterity saving throw, taking 2d6 fire damage per mana point spent on a failed save, or half as much on a success.

**Greater Fireball (Level 9).** Your Fireball's radius increases to 30 feet, and creatures that fail their save catch fire. A burning creature takes 1d6 fire damage at the start of each of its turns until it uses an action to extinguish the flames.

## Cryomancy

You are trained in the ways of magical frost. Frost is patient, silent, and inevitable.

**Freezing Magic (Level 1).** Whenever you deal cold damage to a creature, you can force it to make a Constitution saving throw. On a failure, its speed is reduced to 0 until the end of its next turn.

**Cone of Cold (Level 4).** As a magic action, spend 1 or more mana points. A 60-foot cone erupts from you. Each creature in the area must make a Constitution saving throw, taking 1d8 cold damage per mana point spent on a failed save, or half as much on a success.

**Greater Cone of Cold (Level 9).** Your Cone of Cold's damage dice become 2d8 per mana point spent. The area also becomes difficult terrain until the end of your next turn, and any water in the area freezes solid.

## Electromancy

You channel lightning — fast, precise, and unpredictable.

**Mage Bane (Level 1).** Whenever you deal lightning damage to a creature, you can force it to make a Constitution saving throw. On a failure, it has disadvantage on any spellcasting-related checks until the end of its next turn.

**Lightning Bolt (Level 4).** As a magic action, spend 1 or more mana points. A line 100 feet long and 5 feet wide blasts out from you in a direction you choose. Each creature in the line must make a Dexterity saving throw, taking 1d12 lightning damage per mana point spent on a failed save, or half as much on a success.

**Greater Lightning Bolt (Level 9).** Your Lightning Bolt's damage dice become 2d12 per mana point spent. Creatures that fail their save are dazed until the end of their next turn.

---

## What Changed and Why

**Cut Evocation Technique entirely.** This was the single biggest complexity source: 4 feat selections at levels 2, 5, 8, and 10, drawn from a pool of **11 feats**. That's effectively a mini-subsystem. Lore Mystic has no feat subsystem. Gone.

**Cut all feats (11 → 0).** Since Evocation Technique is gone, the feats go with it. Every feat is either redundant with something else (Arcane Sense ≈ Detect Magic), combat power-creep (Flaming Weapon, Ice Shield), or mobility the class doesn't need (Fire Jump, Thunderstep).

**Cut Unfettered Arcana as a separate feature.** Original had a big flashy ability at level 5 on top of the power-3 AoE. Now level 9's "Greater" signature does the job of the level-9 capstone, and Unfettered Arcana is folded into the level-9 upgrade.

**Cut Power 4 and Power 5 entirely.** Atronach conjuring (both types), Ice Sphere, Fiery Form, Storm Crowned — all gone. This is the "don't go beyond level 5-6 power" rule in practice.

**Cut the "Power" column.** Power was doing four jobs at once: per-turn mana cap, Arcane Bolt damage tier, ability gating ("Power 2: Cinder Cloud"), and conditional thresholds (Cryomancy paralysis). Every one of those is now level-based or proficiency-based. The column is gone.

**Cut specialty abilities from 6+ to 3.** Each specialty now has exactly:
1. **One passive** at level 1
2. **One signature AoE** at level 4
3. **One Greater upgrade** at level 9

That's 3 abilities per specialty across the full class, matching the pace of a class like Sun Mystic (which gives you one signature feature that upgrades).

**Cut secondary specialty abilities.** Flickering Flame, Icy Touch, Static Charge, Gout of Flame, Hail of Shards, Chain Lightning, Cinder Cloud, Frozen Fog, Thunder Blast — all gone. Arcane Bolt is the basic attack; each specialty's signature AoE is the "big spell." No need for a redundant in-between.

**Result:** 2 features at level 1, 2 more ability-score bumps, 2 specialty powers, 1 capstone. Total = **6 feature entries across 10 levels**, same count as Lore Mystic. No feats, no branches, no scaling tiers, no per-power resource tracking.
