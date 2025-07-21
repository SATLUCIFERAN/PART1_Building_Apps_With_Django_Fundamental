

# This represents the primary magical ingredient's energy signature
energy_signature = "volatile_fire" # Could be "calm_water", "stable_earth", "swift_air", "volatile_fire", or "unknown

print(f"Analyzing energy signature: '{energy_signature}'...")

if energy_signature == "volatile_fire":
    print("Potion gains a fiery affinity! Caution: May explode.")
    potion_affinity = "Fire"
elif energy_signature == "calm_water":
    print("Potion gains a watery affinity. Soothing and restorative.")
    potion_affinity = "Water"
elif energy_signature == "stable_earth":
    print("Potion gains an earthy affinity. Enhances defense.")
    potion_affinity = "Earth"
elif energy_signature == "swift_air":
    print("Potion gains an airy affinity. Grants agility.")
    potion_affinity = "Air"
else:
    print("Unknown energy signature. Potion's effect is unpredictable!")
    potion_affinity = "Unpredictable"

print(f"Final Potion Affinity: {potion_affinity}")

'''
Analyzing energy signature: 'volatile_fire'...
Potion gains a fiery affinity! Caution: May explode.
Final Potion Affinity: Fire

'''