
# Non-Pythonic: Risking KeyError
spell_book = {"Fireball": 100, "Healing Aura": 75}
try:
    power = spell_book["Teleport"]
except KeyError:
    power = 0
print(f"Teleport power (Non-Pythonic): {power}")

# Teleport power (Non-Pythonic): 0



# Pythonic: Using .get() with a default value
spell_book = {"Fireball": 100, "Healing Aura": 75}
print("\n--- Pythonic Spell Power Lookup ---")
power = spell_book.get("Teleport", 0) # Default to 0 if "Teleport" not found
print(f"Teleport power (Pythonic): {power}")

power_fireball = spell_book.get("Fireball", 0)
print(f"Fireball power (Pythonic): {power_fireball}")

'''
--- Pythonic Spell Power Lookup ---
Teleport power (Pythonic): 0
Fireball power (Pythonic): 100

'''