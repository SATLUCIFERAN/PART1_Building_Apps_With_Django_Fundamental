print("\n--- Final Star Map (after potential update) ---")
for star_data in star_map:
    # CORRECTED LINE: 
    # Access magnitude from the nested coordinates tuple (star_data[1][2])
    print(f"Star: {star_data[0]}, Coords: {star_data[1]}, Mag: {star_data[1][2]}")
