# A variable representing a global combat constant
MAX_DAMAGE_BOOST = 50

def cast_fireball(target, base_damage):
    """Casts a fireball spell, dealing damage to a target."""
    final_damage = base_damage + MAX_DAMAGE_BOOST
    print(f"  *WHOOSH!* Fireball erupts on {target}, dealing {final_damage} damage!")
    return final_damage

def cast_ice_shard(target, base_damage):
    """Casts an ice shard spell, dealing damage and potentially slowing."""
    final_damage = base_damage * 0.8 # Ice shards might be less direct damage
    print(f"  *CRACKLE!* Ice Shard strikes {target}, dealing {final_damage:.0f} damage and slowing!")
    return final_damage

# This code only runs if combat_spells.py is executed directly, not imported
if __name__ == "__main__":
    print("--- Testing Combat Spells Module ---")
    cast_fireball("Goblin", 30)
    cast_ice_shard("Ogre", 40)
    print(f"Max damage boost available: {MAX_DAMAGE_BOOST}")
