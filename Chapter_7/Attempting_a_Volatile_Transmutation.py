
def attempt_volatile_transmutation(raw_material_qty, conversion_rate):
    """
    Attempts a transmutation. Volatile if conversion_rate is zero.
    """
    try:
        print(f"\n--- Attempting Transmutation Ritual (Qty: {raw_material_qty}, Rate: {conversion_rate}) ---")
        # This line might cause a ZeroDivisionError
        gold_produced = raw_material_qty / conversion_rate
        print(f"  Transmutation successful! Produced {gold_produced:.2f} gold.")
        return gold_produced
    except ZeroDivisionError:
        print("  WARNING: Transmutation rate cannot be zero! Spell fizzled.")
        return 0
    except TypeError:
        print("  ERROR: Invalid material quantity or conversion rate type. Must be numbers!")
        return -1
    except Exception as e: # Catch any other unexpected error
        print(f"  An unexpected magical anomaly occurred: {e}")
        return -2

# Scenario 1: Successful transmutation
attempt_volatile_transmutation(100, 0.5)

'''
--- Attempting Transmutation Ritual (Qty: 100, Rate: 0.5) ---
  Transmutation successful! Produced 200.00 gold.

'''

# Scenario 2: Zero conversion rate (ZeroDivisionError)
attempt_volatile_transmutation(50, 0)

'''
--- Attempting Transmutation Ritual (Qty: 50, Rate: 0) ---
  WARNING: Transmutation rate cannot be zero! Spell fizzled.

'''

# Scenario 3: Invalid types (TypeError)
attempt_volatile_transmutation("fifty", 0.2)

'''
--- Attempting Transmutation Ritual (Qty: fifty, Rate: 0.2) ---
  ERROR: Invalid material quantity or conversion rate type. Must be numbers!

'''

# # Scenario 4: Another unexpected error (e.g., if we forced a NameError)
# try:
#     print(undefined_variable)
# except Exception as e:
#     print(f"Caught general error: {e}")

# '''
# Caught general error: name 'undefined_variable' is not defined

# '''