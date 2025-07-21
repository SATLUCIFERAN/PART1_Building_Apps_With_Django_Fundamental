
def brew_forbidden_potion(ingredient_list):
    forbidden_ingredient = "Shadow Essence"
    print(f"\n--- Brewing Ritual with Ingredients: {ingredient_list} ---")
    for ingredient in ingredient_list:
        if ingredient == forbidden_ingredient:
            # We are explicitly raising a ValueError here
            raise ValueError(f"Forbidden ingredient '{forbidden_ingredient}' detected! Ritual aborted!")
        print(f"  Adding {ingredient} to cauldron...")
    print("  Potion brewed successfully!")

# Test scenarios
try:
    # No forbidden ingredient
    brew_forbidden_potion(["Moonpetal", "Dragon's Scale"]) 
except ValueError as e:
    print(f"Caught error: {e}")

'''
--- Brewing Ritual with Ingredients: ['Moonpetal', "Dragon's Scale"] ---
  Adding Moonpetal to cauldron...
  Adding Dragon's Scale to cauldron...
  Potion brewed successfully!

'''

# Test scenarios
try:
    # Forbidden ingredient
    brew_forbidden_potion(["Phoenix Feather", "Shadow Essence", "Unicorn Horn"]) 
except ValueError as e:
    print(f"Caught error: {e}")

'''
--- Brewing Ritual with Ingredients: 
    ['Phoenix Feather', 'Shadow Essence', 'Unicorn Horn'] ---
  Adding Phoenix Feather to cauldron...
Caught error: Forbidden ingredient 'Shadow Essence' detected! Ritual aborted!

'''