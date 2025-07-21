
all_potions = [
    {"name": "Healing Potion", "purity": 95},
    {"name": "Poison Vial", "purity": 10},
    {"name": "Mana Elixir", "purity": 88},
    {"name": "Weak Antidote", "purity": 60}
]

# Traditional way (using a for loop)
pure_potions_traditional = []
for potion in all_potions:
    if potion["purity"] >= 80:
        pure_potions_traditional.append(potion["name"])
print(f"Pure Potions (Traditional): {pure_potions_traditional}")
# Pure Potions (Traditional): ['Healing Potion', 'Mana Elixir']

# Using List Comprehension (more concise!)
pure_potions_comprehension = [
    potion["name"] for potion in all_potions if potion["purity"] >= 80
]
print(f"Pure Potions (Comprehension): {pure_potions_comprehension}")
# Output: Pure Potions (Comprehension): ['Healing Potion', 'Mana Elixir']

# Example: Doubling the power of all spells
initial_powers = [10, 25, 40, 55]
doubled_powers = [power * 2 for power in initial_powers]
print(f"Doubled Powers: {doubled_powers}") 
# Output: Doubled Powers: [20, 50, 80, 110]
