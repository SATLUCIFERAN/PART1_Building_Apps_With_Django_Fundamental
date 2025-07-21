
def cast_healing_spell(target_name, heal_amount):
    """
    Casts a healing spell on a target for a specified amount.
    """
    print(f"Casting 'Mend Wounds' on {target_name}...")
    print(f"{target_name} regains {heal_amount} health!")


print("--- Healing the Adventurer ---")
cast_healing_spell("Brave Knight", 30)

'''
--- Healing the Adventurer ---
Casting 'Mend Wounds' on Brave Knight...
Brave Knight regains 30 health!

'''

print("\n--- Healing the Dragon ---")
cast_healing_spell("Injured Dragon", 150) 

'''
--- Healing the Dragon ---
Casting 'Mend Wounds' on Injured Dragon...
Injured Dragon regains 150 health!

'''