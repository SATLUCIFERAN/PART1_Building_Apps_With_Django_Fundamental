
new_prophecies = [
    "The Veil between realms shall thin.\n",
    "A new hero, yet unknown, will emerge.\n",
    "The ancient dragons will stir from their slumber.\n"
]

print("--- Inscribing New Prophecies ---")
with open("new_prophecies.txt", "w") as scroll:
    scroll.writelines(new_prophecies)
print("New prophecies inscribed.")

'''
--- Inscribing New Prophecies ---
New prophecies inscribed.

'''

# Verify by reading
print("\n--- Verifying New Prophecies ---")
with open("new_prophecies.txt", "r") as scroll:
    print(scroll.read())

'''
--- Verifying New Prophecies ---
The Veil between realms shall thin.
A new hero, yet unknown, will emerge.
The ancient dragons will stir from their slumber.

'''