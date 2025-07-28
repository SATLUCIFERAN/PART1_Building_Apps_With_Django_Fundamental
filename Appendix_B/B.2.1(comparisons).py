
# Non-Pythonic: Separate comparisons
mana_level = 75
if mana_level > 50 and mana_level < 100:
    print("Mana level is optimal.")

# Mana level is optimal.

# Pythonic: Chained comparisons
mana_level = 75
if 50 < mana_level < 100:
    print("Mana level is optimal (Pythonic).")


# Mana level is optimal (Pythonic).