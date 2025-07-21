
# Import the entire module
import combat_spells 

# Import a specific spell directly
from combat_spells import cast_ice_shard 

# Avoid this in real projects!
from combat_spells import * 

# Using an alias for convenience
import combat_spells as cs


print("--- Adventurer's Journey Begins ---")

# Using the full module name
fire_result = combat_spells.cast_fireball("Bandit Leader", 40)
print(f"  Fire spell result: {fire_result} damage.")
# Output : *WHOOSH!* Fireball erupts on Bandit Leader, dealing 90 damage!
#          Fire spell result: 90 damage.

# Using the directly imported spell
ice_result = cast_ice_shard("Wolf Pack", 25)
print(f"  Ice spell result: {ice_result} damage.")
# *CRACKLE!* Ice Shard strikes Wolf Pack, dealing 20 damage and slowing!
#   Ice spell result: 20.0 damage.

# Using the alias
print(f"  Max damage boost from combat magic: {cs.MAX_DAMAGE_BOOST}")
# Ice spell result: 20.0 damage.
# Max damage boost from combat magic: 50

print("--- Journey Continues ---")


'''
--- Adventurer's Journey Begins ---
  *WHOOSH!* Fireball erupts on Bandit Leader, dealing 90 damage!
  Fire spell result: 90 damage.
  *CRACKLE!* Ice Shard strikes Wolf Pack, dealing 20 damage and slowing!
  Ice spell result: 20.0 damage.
  Max damage boost from combat magic: 50
--- Journey Continues ---

'''