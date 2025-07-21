
shield_integrity = 100 # Initial shield strength
incoming_damage = 15 # Damage per magical attack

print("--- Activating Protective Shield ---")
while shield_integrity > 0:
    print(f"  Shield active! Integrity: {shield_integrity}%.")
    print("  *WHOOSH!* Incoming magical attack!")
    shield_integrity -= incoming_damage # Reduce integrity with each attack

    if shield_integrity <= 0:
        print("  Shield integrity critically low! It shatters!")
        break # We'll learn about 'break' next, but it stops the loop here!
    else:
        print("  Shield holds, for now...")

print("--- Protective Shield Deactivated ---")