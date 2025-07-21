

grimoire_of_fire_spells = {"Fireball", "Flame Shield", "Inferno Blast", "Scorch"}
grimoire_of_ice_spells = {"Ice Shard", "Frost Nova", "Blizzard", "Ice Wall"}
grimoire_of_universal_spells = {"Teleport", "Healing Aura", "Fireball", "Frost Nova"}

print("--- Spell Conflict Resolver ---")

# 1. Spells that exist in BOTH Fire and Universal Grimoires (overlap)
shared_fire_universal = grimoire_of_fire_spells.intersection(grimoire_of_universal_spells)
print(f"\nSpells common to Fire and Universal Grimoires: {shared_fire_universal}") 

# 2. Spells that exist in Fire Grimoire BUT NOT in Ice Grimoire (no direct conflict)
fire_only_spells = grimoire_of_fire_spells.difference(grimoire_of_ice_spells)
print(f"Spells unique to Fire Grimoire (vs. Ice): {fire_only_spells}") 

# 3. All unique spells across ALL grimoires (total known spells)
all_known_spells = grimoire_of_fire_spells.union(grimoire_of_ice_spells)\
                   .union(grimoire_of_universal_spells)
print(f"All unique spells known: {all_known_spells}")

# 4. Check if the Ice Grimoire is a subset of all known spells
is_ice_subset = grimoire_of_ice_spells.issubset(all_known_spells)
print(f"Is Ice Grimoire a subset of all known spells? {is_ice_subset}") 

# 5. Identify spells that are in Fire OR Ice, but NOT universal
#    (elemental-specific, not general)
elemental_specific_spells = (grimoire_of_fire_spells.union(grimoire_of_ice_spells))\
                             .difference(grimoire_of_universal_spells)
print(f"Elemental-specific spells (not universal): {elemental_specific_spells}") 