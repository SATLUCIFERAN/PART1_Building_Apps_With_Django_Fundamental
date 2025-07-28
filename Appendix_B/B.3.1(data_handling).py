
# Non-Pythonic: Accessing elements by index
artifact_data = ("Phoenix Feather", "Rare", 95)
name = artifact_data[0]
rarity = artifact_data[1]
power = artifact_data[2]
print(f"Artifact: {name}, Rarity: {rarity}, Power: {power}")


'''
Artifact: Phoenix Feather, Rarity: Rare, Power: 95
Artifact (Pythonic): Phoenix Feather, Rarity: Rare, Power: 95

'''



# Pythonic: Unpacking a tuple/list
artifact_data = ("Phoenix Feather", "Rare", 95)
name, rarity, power = artifact_data
print(f"Artifact (Pythonic): {name}, Rarity: {rarity}, Power: {power}")

# You can also unpack in loops!
spell_details = [("Ignis Bolt", 15), ("Healing Aura", 25)]
print("\n--- Pythonic Spell Unpacking in Loop ---")
for spell_name, mana_cost in spell_details:
    print(f"Spell: {spell_name}, Cost: {mana_cost}")


'''
--- Pythonic Spell Unpacking in Loop ---
Spell: Ignis Bolt, Cost: 15
Spell: Healing Aura, Cost: 25

'''