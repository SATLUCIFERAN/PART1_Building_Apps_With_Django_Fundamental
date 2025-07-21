
def craft_healing_potion(herbs_qty, water_qty):
    """Crafts a healing potion from herbs and water."""
    if herbs_qty >= 2 and water_qty >= 1:
        print(f"  Brewing Healing Potion with {herbs_qty} herbs and {water_qty} water...")
        return "Healing Potion (Standard)"
    else:
        print("  Insufficient ingredients for Healing Potion.")
        return None

def craft_mana_crystal(raw_crystal_qty, arcane_dust_qty):
    """Crafts a mana crystal from raw crystals and arcane dust."""
    if raw_crystal_qty >= 1 and arcane_dust_qty >= 5:
        print(f"  Forging Mana Crystal with {raw_crystal_qty} crystal and {arcane_dust_qty} dust...")
        return "Mana Crystal (Charged)"
    else:
        print("  Insufficient ingredients for Mana Crystal.")
        return None

def craft_invisibility_cloak(shadow_silk_qty, illusion_essence_qty):
    """Crafts an invisibility cloak."""
    if shadow_silk_qty >= 10 and illusion_essence_qty >= 3:
        print(f"  Weaving Invisibility Cloak with {shadow_silk_qty} silk and {illusion_essence_qty} essence...")
        return "Invisibility Cloak (Perfect)"
    else:
        print("  Insufficient ingredients for Invisibility Cloak.")
        return None
    

# --- Alchemist's Daily Crafting Schedule ---
print("--- Alchemist's Crafting Station Active ---")

# Attempt 1: Craft Healing Potions
print("\nAttempting to craft Healing Potions:")
potion1 = craft_healing_potion(herbs_qty=3, water_qty=2)
if potion1:
    print(f"  Successfully crafted: {potion1}")
potion2 = craft_healing_potion(herbs_qty=1, water_qty=1) # Insufficient herbs
if potion2:
    print(f"  Successfully crafted: {potion2}")

'''
--- Alchemist's Crafting Station Active ---

Attempting to craft Healing Potions:
  Brewing Healing Potion with 3 herbs and 2 water...
  Successfully crafted: Healing Potion (Standard)
  Insufficient ingredients for Healing Potion.

'''

# Attempt 2: Craft Mana Crystals
print("\nAttempting to craft Mana Crystals:")
crystal1 = craft_mana_crystal(raw_crystal_qty=2, arcane_dust_qty=10)
if crystal1:
    print(f"  Successfully crafted: {crystal1}")

'''
--- Alchemist's Crafting Station Active ---

Attempting to craft Mana Crystals:
  Forging Mana Crystal with 2 crystal and 10 dust...
  Successfully crafted: Mana Crystal (Charged)

'''

# Attempt 3: Craft Invisibility Cloak
print("\nAttempting to craft Invisibility Cloak:")
cloak1 = craft_invisibility_cloak(shadow_silk_qty=12, illusion_essence_qty=4)
if cloak1:
    print(f"  Successfully crafted: {cloak1}")

print("\n--- Crafting Schedule Complete ---")

'''
--- Alchemist's Crafting Station Active ---

Attempting to craft Invisibility Cloak:
  Weaving Invisibility Cloak with 12 silk and 4 essence...
  Successfully crafted: Invisibility Cloak (Perfect)

'''