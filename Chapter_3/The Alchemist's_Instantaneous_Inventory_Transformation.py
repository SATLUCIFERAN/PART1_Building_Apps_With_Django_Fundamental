
raw_discoveries = [
    "Silver Coin", "Broken Wand", "Healing Potion (Minor)", "Gold Coin",
    "Mana Potion (Greater)", "Silver Coin", "Rusty Dagger", "Healing Potion (Minor)",
    "Scroll of Teleportation", "Gold Coin", "Mana Potion (Lesser)"
]

# --- Phase 1: Categorize and filter useful items ---
# Create a dictionary mapping item type to a list of its specific names,
# but only for potions and scrolls, and only if they are "Greater" or "Scroll"

categorized_inventory = {
    item.split(' (')[0]: item # Key: base name, Value: full name
    for item in raw_discoveries
    if ("Potion (Greater)" in item or "Scroll" in item)
}

# This will give us a dictionary like {'Mana Potion': 'Mana Potion (Greater)', 'Scroll of Teleportation': 'Scroll of Teleportation'}
# Note: If there were multiple "Greater" potions, only the last one would be kept as keys must be unique.
# For multiple items of the same type, a list comprehension would be better for the values, or a defaultdict.
# Let's refine this to group by type for a more realistic scenario:

# Refined approach for categorization:

from collections import defaultdict
grouped_inventory = defaultdict(list)
for item in raw_discoveries:
    if "Potion" in item:
        grouped_inventory["Potions"].append(item)
    elif "Scroll" in item:
        grouped_inventory["Scrolls"].append(item)
    elif "Coin" in item:
        grouped_inventory["Coins"].append(item)
    else:
        grouped_inventory["Misc"].append(item)

print("--- Grouped Inventory (Traditional Loop) ---")
print(dict(grouped_inventory)) # Convert defaultdict to dict for printing

# --- Phase 2: Extract all unique item types found ---
unique_item_types = {
    item.split(' (')[0] # Get just the base name
    for item in raw_discoveries
}
print(f"\n--- All Unique Item Types Discovered (Set Comprehension) ---")
print(unique_item_types)

# --- Phase 3: Create a list of only 'Potion' names, but only if they are 'Greater'
greater_potions_list = [
    item.split(' (')[0] # Extract just the name
    for item in raw_discoveries
    if "Potion" in item and "Greater" in item
]
print(f"\n--- List of Greater Potions (List Comprehension) ---")
print(greater_potions_list)
