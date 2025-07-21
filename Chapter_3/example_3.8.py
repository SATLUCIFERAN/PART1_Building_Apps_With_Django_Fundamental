
gem_collection = ["Ruby", "Emerald", "Sapphire", "Ruby", "Diamond", "Emerald"]
print(f"Original Collection: {gem_collection}")

# Count the number of gems
num_gems = len(gem_collection)
print(f"Total Gems: {num_gems}") # Output: Total Gems: 6

# Count occurrences of a specific gem
ruby_count = gem_collection.count("Ruby")
print(f"Number of Rubies: {ruby_count}") # Output: Number of Rubies: 2

# Sort the collection (in place)
gem_collection.sort()
print(f"Sorted Collection (in place): {gem_collection}") 
# Output: Sorted Collection (in place): ['Diamond', 'Emerald', 'Emerald', 'Ruby', 'Ruby', 'Sapphire']

# Create a new sorted list (original unchanged)
unsorted_scrolls = ["Dragon Lore", "Ancient History", "Celestial Maps"]
sorted_scrolls = sorted(unsorted_scrolls)
print(f"Original Scrolls: {unsorted_scrolls}") 
# Output: Original Scrolls: ['Dragon Lore', 'Ancient History', 'Celestial Maps']
print(f"New Sorted Scrolls: {sorted_scrolls}") 
# Output: New Sorted Scrolls: ['Ancient History', 'Celestial Maps', 'Dragon Lore']

# Find the index of an item
emerald_index = gem_collection.index("Emerald")
print(f"First Emerald is at index: {emerald_index}") # Output: First Emerald is at index: 1
