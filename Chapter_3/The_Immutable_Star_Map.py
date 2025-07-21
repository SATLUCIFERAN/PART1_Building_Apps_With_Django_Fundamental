

# A star map where each star's data is an immutable tuple 
# (Name, (RA, Dec, Magnitude))
star_map = [
    ("Sirius", (6.75, -16.71, -1.46)),
    ("Vega", (18.62, 38.78, 0.03)),
    ("Polaris", (2.52, 89.26, 1.98))
]

print("--- Ancient Star Map ---")
for star_data in star_map:
    star_name = star_data[0]
    coordinates = star_data[1] # This is itself a tuple!
    ra = coordinates[0]
    dec = coordinates[1]
    # Accessing magnitude from the nested coordinates tuple
    magnitude = coordinates[2] 
    print(f"Star: {star_name}, \
    Coordinates (RA, Dec): ({ra}, {dec}), Magnitude: {magnitude}")

'''
--- Ancient Star Map ---
Star: Sirius, Coordinates (RA, Dec): (6.75, -16.71), Magnitude: -1.46
Star: Vega, Coordinates (RA, Dec): (18.62, 38.78), Magnitude: 0.03
Star: Polaris, Coordinates (RA, Dec): (2.52, 89.26), Magnitude: 1.98

'''

# Attempt to change a star's coordinate (will fail if you try to modify the tuple directly)
# star_map[0][1] = (7.0, -17.0, -1.40) # This would cause a TypeError!
# You can, however, replace an entire star entry (if star_map itself is a list)

print("\n--- Correcting a Star's Magnitude (by replacing the whole entry) ---")
# Find Sirius's entry
sirius_entry_index = -1
for i, entry in enumerate(star_map): # enumerate gives both index and item
    if entry[0] == "Sirius":
        sirius_entry_index = i
        break

if sirius_entry_index != -1:
    old_sirius_data = star_map[sirius_entry_index]
    # Create a NEW tuple with the updated magnitude
    # Only magnitude changed
    new_sirius_coordinates = (old_sirius_data[1][0], 
                              old_sirius_data[1][1], -1.42)     
    # Reconstruct the main tuple with the original name 
    # and the new coordinates tuple
    new_sirius_data = (old_sirius_data[0], new_sirius_coordinates)
    # Replace the old tuple with the new one
    star_map[sirius_entry_index] = new_sirius_data 
    print(f"Updated Sirius entry: {star_map[sirius_entry_index]}")
    # Output : Updated Sirius entry: ('Sirius', (6.75, -16.71, -1.42))

print("\n--- Final Star Map (after potential update) ---")
for star_data in star_map:
    # CORRECTED LINE: 
    # Access magnitude from the nested coordinates tuple (star_data[1][2])
    print(f"Star: {star_data[0]}, Coords: {star_data[1]}, Mag: {star_data[1][2]}")

'''
--- Final Star Map (after potential update) ---
Star: Sirius, Coords: (6.75, -16.71, -1.42), Mag: -1.42
Star: Vega, Coords: (18.62, 38.78, 0.03), Mag: 0.03
Star: Polaris, Coords: (2.52, 89.26, 1.98), Mag: 1.98

'''