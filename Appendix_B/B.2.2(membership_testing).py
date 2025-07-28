
# Non-Pythonic: Looping to check for membership
forbidden_ingredients = ["Dragon's Scale", "Shadow Essence"]
current_ingredient = "Shadow Essence"
found = False
for item in forbidden_ingredients:
    if item == current_ingredient:
        found = True
        break
if found:
    print("Forbidden ingredient detected!")


# Forbidden ingredient detected!




# Pythonic: Using the 'in' operator
# Sets are even faster for 'in' checks!
forbidden_ingredients = {"Dragon's Scale", "Shadow Essence"} 
current_ingredient = "Shadow Essence"
print("\n--- Pythonic Forbidden Ingredient Check ---")
if current_ingredient in forbidden_ingredients:
    print("Forbidden ingredient detected (Pythonic)!")



# --- Pythonic Forbidden Ingredient Check ---
# Forbidden ingredient detected (Pythonic)!