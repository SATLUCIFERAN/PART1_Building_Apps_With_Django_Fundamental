
# Creating an empty set
empty_pouch_for_charms = set()
print(f"Empty Charm Pouch: {empty_pouch_for_charms}") # Output: Empty Charm Pouch: set()

# A set of unique magical elements (duplicates are automatically removed)
elemental_types = {"Fire", "Water", "Earth", "Air", "Fire", "Water"}
print(f"Unique Elemental Types: {elemental_types}") 
# Output: Unique Elemental Types: {'Earth', 'Air', 'Fire', 'Water'} (order may vary)

# Creating a set from a list (useful for removing duplicates)
duplicate_runes = ["Rune of Power", "Rune of Speed", "Rune of Power", "Rune of Sight"]
unique_runes = set(duplicate_runes)
print(f"Unique Runes: {unique_runes}") 
# Output: Unique Runes: {'Rune of Speed', 'Rune of Power',
#                        'Rune of Sight'} (order may vary)
