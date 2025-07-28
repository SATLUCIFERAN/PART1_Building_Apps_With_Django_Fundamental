

# Non-Pythonic: Iterating by index, 
# prone to IndexError if lists are different lengths
spell_names = ["Ignis Bolt", "Healing Aura"]
mana_costs = [15, 25]
for i in range(len(spell_names)):
    print(f"Spell: {spell_names[i]}, Mana Cost: {mana_costs[i]}")


'''
Spell: Ignis Bolt, Mana Cost: 15
Spell: Healing Aura, Mana Cost: 25

'''


# Pythonic: zip() for elegant parallel iteration
spell_names = ["Ignis Bolt", "Healing Aura"]
mana_costs = [15, 25]
print("\n--- Pythonic Spell & Mana Pairing ---")
for name, cost in zip(spell_names, mana_costs):
    print(f"Spell: {name}, Mana Cost: {cost}")


'''
--- Pythonic Spell & Mana Pairing ---
Spell: Ignis Bolt, Mana Cost: 15
Spell: Healing Aura, Mana Cost: 25

'''