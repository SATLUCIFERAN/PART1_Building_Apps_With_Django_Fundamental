

print("--- Inscribing New Discoveries ---")
with open("discovery_log.txt", "w") as log:
    log.write("Discovery 1: Found a new species of glowing moss.\n")
    log.write("Discovery 2: Uncovered ruins of an ancient civilization.\n")
    log.write("Discovery 3: Deciphered a fragment of the Celestial Map.")
    # No newline after Discovery 3, so next write would be on same line
print("Discoveries inscribed.")

'''
--- Inscribing New Discoveries ---
Discoveries inscribed.

'''

# Now, let's append to it
print("\n--- Appending More Discoveries ---")
with open("discovery_log.txt", "a") as log:
    log.write("\nDiscovery 4: Identified the source of the magical anomaly.")
    log.write("\nDiscovery 5: Successfully stabilized the elemental orb.")
print("More discoveries appended.")

'''
--- Appending More Discoveries ---
More discoveries appended.

'''