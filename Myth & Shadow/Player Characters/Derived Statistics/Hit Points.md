# Hit Points (HP)

## Max HP

Your *Max HP* is equal to 5 x ([Level](../Progression/Level.md) + [Health](../Attributes/Health.md))

If any of these values are less than 1, treat them as a 1 instead.

Hit Points represent a mix of your combat skill, endurance, and physical health.

## Current HP

Your current HP, referred to as just HP, ranges from 0 to your *Max HP*.

Your current HP is changed by [Damage](Hit%20Points.md#Damage) or [Healing](Hit%20Points.md#Healing).

## Damage

Whenever you take damage:

- You subtract it from your HP.
- If the damage meets or exceeds [Half](../../Game%20Procedures/Core%20Procedures/Half.md) your Max HP, you become [Wounded](../../Game%20Procedures/Conditions/Wounded.md).
- If your HP is reduced to 0, you start [Dying](../../Game%20Procedures/Conditions/Dying.md).

*Creatures can be [Resistant](../../Game%20Procedures/Conditions/Resistant.md), [Vulnerable](../../Game%20Procedures/Conditions/Vulnerable.md), or [Immune](../../Game%20Procedures/Conditions/Immune.md) to certain [Damage Types](../../Game%20Procedures/Combat/Damage/Damage%20Types/{Damage%20Types}.md) and [Damage Tiers](../../Game%20Procedures/Combat/Damage/Damage%20Tiers/{Damage%20Tiers}.md).*

## Healing

You can take a [Break](../../Game%20Procedures/Core%20Procedures/Break.md) to restore a [Quarter](../../Game%20Procedures/Core%20Procedures/Half.md) of your [Max HP](Hit%20Points.md#Max%20HP).

[Spells](../../Magic/Spells.md) and magic can heal HP more quickly.

## Miscellaneous

If multiple effects would increase a creature's [Max HP](Hit%20Points.md#Max%20HP), only the stronger effect is used.

Objects may be given HP to represent how tough they are.
