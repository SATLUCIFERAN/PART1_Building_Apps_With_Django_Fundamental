
full_recipe = ["Water", "Moonpetal", "Dragon's Scale",
               "Sunstone Dust", "Phoenix Feather", "Elixir Base"]

# Get ingredients from index 1 up to (but not including) index 4
core_ingredients = full_recipe[1:4]
print(f"Core Ingredients: {core_ingredients}") 
# Output: Core Ingredients: ['Moonpetal', 'Dragon\'s Scale', 'Sunstone Dust']

# Get all ingredients from the third one to the end
remaining_steps = full_recipe[2:]
print(f"Remaining Steps: {remaining_steps}") 
# Output: Remaining Steps: ['Dragon\'s Scale', 
#         'Sunstone Dust', 'Phoenix Feather', 'Elixir Base']

# Get a copy of the entire list
copy_of_recipe = full_recipe[:]
print(f"Copy of Recipe: {copy_of_recipe}") 
# Output: Copy of Recipe: ['Water', 'Moonpetal', 'Dragon\'s Scale',
#         'Sunstone Dust', 'Phoenix Feather', 'Elixir Base']

# Get every other ingredient
alternate_ingredients = full_recipe[::2]
print(f"Alternate Ingredients: {alternate_ingredients}") 
# Output: Alternate Ingredients: ['Water', 'Dragon\'s Scale', 'Phoenix Feather']
