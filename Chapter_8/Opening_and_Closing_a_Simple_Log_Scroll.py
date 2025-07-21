

# # --- Writing to a new log scroll ('w' mode) ---
# print("--- Creating a New Ritual Log ---")

# # Open in write mode (erases existing content)
# log_scroll = open("ritual_log.txt", "w") 
# log_scroll.write("Ritual started: Dawn of the First Day.\n")
# log_scroll.write("Mana conduit activated.\n")
# log_scroll.close() # Crucial: Close the scroll to save changes!
# print("Log scroll created and closed.")

# '''
# --- Creating a New Ritual Log ---
# Log scroll created and closed.

# '''

# # --- Appending to the log scroll ('a' mode) ---
# print("\n--- Appending to the Ritual Log ---")

# # Open in append mode (adds to end)
# log_scroll = open("ritual_log.txt", "a") 
# log_scroll.write("Apprentice John arrived.\n")
# log_scroll.write("First spell cast: Light Orb.\n")
# log_scroll.close()
# print("Log scroll appended and closed.")

# '''
# --- Appending to the Ritual Log ---
# Log scroll appended and closed.

# '''

# --- Attempting exclusive creation ('x' mode) ---
print("\n--- Attempting Exclusive Creation (will error if file exists) ---")
try:
    # This will fail because ritual_log.txt already exists
    exclusive_scroll = open("ritual_log.txt", "x") 
    exclusive_scroll.write("This line should not be written.\n")
    exclusive_scroll.close()
except FileExistsError:
    print("Error: 'ritual_log.txt' already exists.\
           Exclusive creation failed as expected.")

'''
--- Attempting Exclusive Creation (will error if file exists) ---
Error: 'ritual_log.txt' already exists. 
       Exclusive creation failed as expected.

'''