
# 1. Daily Ritual Sequence (Order matters, can change)
daily_ritual_steps = ["Prepare Altar", "Gather Elements", "Chant Incantation", "Infuse Essence", "Seal Ritual"]
# Why List? Order is crucial, and steps might be added/removed.
print(f"Daily Ritual Steps (List): {daily_ritual_steps}")

# 2. Celestial Constellation Data (Fixed coordinates, immutable)
# (Constellation Name, (RA, Dec))
constellation_coordinates = ("Orion", (5.57, -6.20))
# Why Tuple? Coordinates are fixed, and we want to ensure their integrity.
print(f"Orion Coordinates (Tuple): {constellation_coordinates}")

# 3. Alchemist's Known Spells (Spell Name: Spell Details)
known_spells_details = {
    "Fireball": {"element": "fire", "mana_cost": 20},
    "Healing Aura": {"element": "light", "mana_cost": 15},
    "Invisibility": {"element": "shadow", "mana_cost": 30}
}
# Why Dictionary? Quick lookup of spell details by name.
print(f"Known Spells Details (Dictionary): {known_spells_details}")

# 4. Unique Discovered Creatures (No duplicates, order doesn't matter)
discovered_creatures = {"Griffin", "Basilisk", "Unicorn", "Griffin", "Dragon"}
# Why Set? Automatically handles uniqueness, perfect for a list of distinct species.
print(f"Unique Discovered Creatures (Set): {discovered_creatures}")

# 5. Combining strategies: A list of tuples for fixed quest details
quest_details = [
    ("The Lost Amulet", "Forest of Whispers", 3), # Name, Location, Difficulty
    ("Dragon's Hoard", "Volcano Peak", 5),
    ("Rescue Villagers", "Haunted Village", 2)
]
# Why List of Tuples? The overall list of quests can change, but each quest's details (tuple) are fixed.
print(f"Quest Details (List of Tuples): {quest_details}")

# 6. A dictionary mapping quest names to their full details (using a tuple as a key if needed)
quest_lookup = {
    quest[0]: {"location": quest[1], "difficulty": quest[2]}
    for quest in quest_details
}
print(f"Quest Lookup (Dictionary): {quest_lookup}")