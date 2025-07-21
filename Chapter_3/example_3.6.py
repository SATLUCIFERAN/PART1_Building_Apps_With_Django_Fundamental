

spell_repertoire = ["Fireball", "Ice Shard", "Teleport", "Fireball", "Healing Wave"]
print(f"Initial Spells: {spell_repertoire}")

# Remove the first "Fireball" spell found
spell_repertoire.remove("Fireball")
print(f"After remove('Fireball'): {spell_repertoire}") 
# Output: After remove('Fireball'): ['Ice Shard', 'Teleport', 'Fireball', 'Healing Wave']

# Pop the last spell (Healing Wave)
last_learned_spell = spell_repertoire.pop()
print(f"Popped Spell: {last_learned_spell}") 
# Output: Popped Spell: Healing Wave
print(f"After pop(): {spell_repertoire}") 
# Output: After pop(): ['Ice Shard', 'Teleport', 'Fireball']

# Pop the spell at index 1 (Teleport)
mid_spell = spell_repertoire.pop(1)
print(f"Popped Mid Spell: {mid_spell}") 
# Output: Popped Mid Spell: Teleport
print(f"After pop(1): {spell_repertoire}") 
# Output: After pop(1): ['Ice Shard', 'Fireball']

# Delete the spell at index 0 (Ice Shard)
del spell_repertoire[0]
print(f"After del list[0]: {spell_repertoire}") 
# Output: After del list[0]: ['Fireball']