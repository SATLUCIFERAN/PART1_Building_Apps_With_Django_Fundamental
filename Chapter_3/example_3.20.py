
my_components = {"Moonpetal", "Dragon's Scale", "Phoenix Feather", "Glimmering Dewdrop"}
friend_components = {"Dragon's Scale", "Unicorn Horn", "Glimmering Dewdrop",
                     "Sunstone Dust"}

print(f"My Components: {my_components}")
# My Components: {'Moonpetal', 'Phoenix Feather', 'Glimmering Dewdrop', "Dragon's Scale"}
print(f"Friend's Components: {friend_components}")
# Friend's Components: {'Sunstone Dust', 'Glimmering Dewdrop',
#                        "Dragon's Scale", 'Unicorn Horn'}

# Add a new component to my collection
my_components.add("Star Dust")
print(f"\nMy Components after adding Star Dust: {my_components}")
# My Components after adding Star Dust: {'Star Dust', "Dragon's Scale", 'Moonpetal',
#                                        'Phoenix Feather', 'Glimmering Dewdrop'}

# Remove a component (safely)
my_components.discard("Phoenix Feather")
print(f"My Components after discarding Phoenix Feather: {my_components}")
#My Components after discarding Phoenix Feather: {'Star Dust', "Dragon's Scale",
#                                                 'Moonpetal', 'Glimmering Dewdrop'}

# Find all unique components we collectively have (Union)
all_unique_components = my_components.union(friend_components)
print(f"\nAll Unique Components (Union): {all_unique_components}")
# All Unique Components (Union): {'Unicorn Horn', 'Sunstone Dust', 'Star Dust',
#                                  "Dragon's Scale", 'Moonpetal', 'Glimmering Dewdrop'}

# Find components we both possess (Intersection)
common_components = my_components.intersection(friend_components)
print(f"Common Components (Intersection): {common_components}")
# Common Components (Intersection): {'Glimmering Dewdrop', "Dragon's Scale"}

# Find components I have that my friend doesn't (Difference)
my_unique_components = my_components.difference(friend_components)
print(f"My Unique Components (Difference): {my_unique_components}")
# My Unique Components (Difference): {'Star Dust', 'Moonpetal'}

# Check if my components are a subset of all unique components
is_subset = my_components.issubset(all_unique_components)
print(f"Are my components a subset of all unique component? {is_subset}") 
# Are my components a subset of all unique conponent? True


