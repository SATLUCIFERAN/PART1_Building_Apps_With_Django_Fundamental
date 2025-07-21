
spellbook = {
    "Fireball": 
    {"power": 75, "mana_cost": 20, "element": "fire", "mastery_level": "Apprentice"},
    "Healing Aura": 
    {"power": 50, "mana_cost": 15, "element": "light", "mastery_level": "Novice"},
    "Teleportation": 
    {"power": 100, "mana_cost": 50, "element": "space", "mastery_level": "Master"}
}

print("--- Initial Spellbook ---")
for spell_name, details in spellbook.items():
    print(f"Spell: {spell_name}, Power: {details['power']}, Cost: {details['mana_cost']}")



# Day 1: Alchemist discovers a new, more powerful Fireball variant
print("\n--- Day 1: Discovering a New Fireball Variant ---")
spellbook["Fireball"] = {"power": 90, "mana_cost": 25,
                         "element": "fire", "mastery_level": "Journeyman"}
print(f"Updated Fireball Power: {spellbook['Fireball']['power']}")



# Day 2: A new spell is added to the spellbook
print("\n--- Day 2: Adding a New Spell ---")
spellbook["Ice Shard"] = {"power": 60, "mana_cost": 18,
                          "element": "ice", "mastery_level": "Apprentice"}
print(f"New Spell Added: {spellbook['Ice Shard']}")



# Day 3: Master Alchemist reviews spells and suggests improvements
print("\n--- Day 3: Master Review ---")
for spell_name, details in spellbook.items():
    if details["mastery_level"] == "Apprentice":
        # Apprentice spells get a small power boost
        details["power"] += 5
        print(f"  Boosting '{spell_name}' (Apprentice spell) power to {details['power']}")
    elif details["mastery_level"] == "Master" and details["mana_cost"] > 40:
        # Master spells with high cost get a mana efficiency improvement
        details["mana_cost"] -= 5
        print(f"  Improving '{spell_name}' (Master spell) mana cost to {details['mana_cost']}")

print("\n--- Final Spellbook After Master Review ---")
for spell_name, details in spellbook.items():
    print(f"Spell: {spell_name}, Power: {details['power']},\
             Cost: {details['mana_cost']}, Mastery: {details['mastery_level']}")

# Quickly check if a spell exists
if "Teleportation" in spellbook:
    print("\nTeleportation spell is available!")