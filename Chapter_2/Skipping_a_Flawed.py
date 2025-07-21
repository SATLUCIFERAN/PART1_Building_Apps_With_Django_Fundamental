
runes_to_chant = ["Rune of Power", "Flawed Rune",
                  "Rune of Protection", "Rune of Wisdom"]

print("--- Chanting Ancient Runes ---")
for rune in runes_to_chant:
    if rune == "Flawed Rune":
        print(f"  Encountered '{rune}'. It's unstable. Skipping this rune.")
        continue # Skip the rest of this iteration and go to the next rune
    print(f"  Chanting the '{rune}'...")
    # Imagine complex magical effect of chanting here
print("--- Ancient Chants Complete ---")

'''
--- Chanting Ancient Runes ---
  Chanting the 'Rune of Power'...
  Encountered 'Flawed Rune'. It's unstable. Skipping this rune.
  Chanting the 'Rune of Protection'...
  Chanting the 'Rune of Wisdom'...
--- Ancient Chants Complete ---

'''