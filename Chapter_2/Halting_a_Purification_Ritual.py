
items_to_purify = ["Blessed Relic", "Ancient Tome",
                   "Corrupted Orb", "Sacred Chalice"]

print("--- Beginning Purification Ritual ---")
for item in items_to_purify:
    print(f"  Purifying '{item}'...")
    if item == "Corrupted Orb":
        print("  !!! WARNING: HIGH CORRUPTION DETECTED\
               IN ORB! RITUAL HALTED FOR SAFETY !!!")
        break # Emergency stop!
    print(f"  '{item}' cleansed.")
print("--- Purification Ritual Concluded ---")

'''
--- Beginning Purification Ritual ---
  Purifying 'Blessed Relic'...
  'Blessed Relic' cleansed.
  Purifying 'Ancient Tome'...
  'Ancient Tome' cleansed.
  Purifying 'Corrupted Orb'...
  !!! WARNING: HIGH CORRUPTION DETECTED IN ORB! RITUAL HALTED FOR SAFETY !!!
--- Purification Ritual Concluded ---

'''