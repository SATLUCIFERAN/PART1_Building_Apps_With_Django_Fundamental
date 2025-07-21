
alchemist_inventory = {
    "potions": 10,
    "scrolls": 5,
    "gems": 20,
    "elixirs": 3
}
print(f"Initial Inventory: {alchemist_inventory}")

# Consume some potions (delete the entry)
del alchemist_inventory["potions"]
print(f"After consuming potions: {alchemist_inventory}") 
# Output: After consuming potions: {'scrolls': 5, 'gems': 20, 'elixirs': 3}

# Sell some gems (pop the value)
sold_gems = alchemist_inventory.pop("gems")
print(f"Sold {sold_gems} gems.") 
# Output: Sold 20 gems.
print(f"After selling gems: {alchemist_inventory}") 
# Output: After selling gems: {'scrolls': 5, 'elixirs': 3}

# Try to pop a non-existent item safely
non_existent_item = alchemist_inventory.pop("runes", "Item not found in inventory.")
print(f"Tried to pop runes: {non_existent_item}") 
# Output: Tried to pop runes: Item not found in inventory.
