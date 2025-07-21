# A lambda function to quickly calculate potion power
# It takes 'base_power' and 'multiplier' and returns their product
calculate_potion_power = lambda base_power, multiplier: base_power * multiplier

print("--- Quick Potion Power Calculations ---")
potion_a_power = calculate_potion_power(20, 1.5)
print(f"Potion A Power: {potion_a_power}") # Output: Potion A Power: 30.0

potion_b_power = calculate_potion_power(50, 0.8)
print(f"Potion B Power: {potion_b_power}") # Output: Potion B Power: 40.0

# Lambda functions are often used directly where a function is expected
# Example: Sorting a list of magical artifacts by their power
artifacts = [
    {"name": "Amulet of Ages", "power": 90},
    {"name": "Lesser Healing Orb", "power": 30},
    {"name": "Sword of Whispers", "power": 75}
]

# Sort artifacts by their 'power' value using a lambda as the key
# 'key=lambda artifact: artifact["power"]' tells sort() to use the 'power' value for comparison
artifacts.sort(key=lambda artifact: artifact["power"])
print("\n--- Artifacts Sorted by Power ---")
for artifact in artifacts:
    print(f"{artifact['name']}: {artifact['power']} power")
# Output:
# Lesser Healing Orb: 30 power
# Sword of Whispers: 75 power
# Amulet of Ages: 90 power
