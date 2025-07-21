
ingredient_list = [
    "Moonpetal (Fresh)",
    "Dragon's Scale (Good)",
    "Expired Phoenix Tear",
    "Gorgon's Eye (Dangerous!)",
    "Unicorn Horn Shavings"
]

print("--- Alchemist Begins Ingredient Sorting ---")
sorted_ingredients = []

for ingredient in ingredient_list:
    print(f"\nInspecting: '{ingredient}'")

    if "Dangerous!" in ingredient:
        print("  !!! CRITICAL WARNING: DANGEROUS INGREDIENT FOUND!\
              ABORTING SORTING PROCESS !!!")
        break # Stop the entire loop immediately

    if "Expired" in ingredient:
        print("  This ingredient is expired. Skipping to the next one.")
        continue # Skip the rest of the current iteration

    # If neither dangerous nor expired, process it
    processed_name = ingredient.split(' (')[0] # Get just the name before '('
    sorted_ingredients.append(processed_name)
    print(f"  '{processed_name}' added to sorted collection.")

print("\n--- Ingredient Sorting Concluded ---")
print(f"Sorted Ingredients: {sorted_ingredients}")


'''
--- Alchemist Begins Ingredient Sorting ---

Inspecting: 'Moonpetal (Fresh)'
  'Moonpetal' added to sorted collection.

Inspecting: 'Dragon's Scale (Good)'
  'Dragon's Scale' added to sorted collection.

Inspecting: 'Expired Phoenix Tear'
  This ingredient is expired. Skipping to the next one.

Inspecting: 'Gorgon's Eye (Dangerous!)'
  !!! CRITICAL WARNING: DANGEROUS INGREDIENT FOUND! ABORTING SORTING PROCESS !!!

--- Ingredient Sorting Concluded ---
Sorted Ingredients: ['Moonpetal', "Dragon's Scale"]

'''