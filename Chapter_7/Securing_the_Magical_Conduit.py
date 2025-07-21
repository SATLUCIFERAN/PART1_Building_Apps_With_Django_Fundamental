
def activate_conduit(power_level, unstable_factor):
    conduit_open = False
    try:
        print(f"\n--- Activating Conduit (Power: {power_level}, Unstable: {unstable_factor}) ---")
        conduit_open = True # Assume conduit is now open
        if unstable_factor > 0.5:
            # Simulate an overload
            raise ValueError("Conduit overload detected!")
        final_output = power_level / unstable_factor
        print(f"  Conduit stable. Final output: {final_output:.2f} units.")

    except ValueError as e:
        print(f"  Conduit activation failed: {e}")
    except ZeroDivisionError:
        print("  Unstable factor cannot be zero!")
    finally:
        # This code ALWAYS runs, ensuring the conduit is closed
        if conduit_open:
            print("  [CLEANUP] Securing and closing the magical conduit.")
        else:
            print("  [CLEANUP] No conduit was opened, no need to close.")
        print("  [CLEANUP] Lab workspace reset.")


# Stable activation
activate_conduit(100, 0.2) 

'''
--- Activating Conduit (Power: 100, Unstable: 0.2) ---
  Conduit stable. Final output: 500.00 units.
  [CLEANUP] Securing and closing the magical conduit.
  [CLEANUP] Lab workspace reset.

'''

# Unstable activation (ValueError)
activate_conduit(50, 0.8)

'''
--- Activating Conduit (Power: 50, Unstable: 0.8) ---
  Conduit activation failed: Conduit overload detected!
  [CLEANUP] Securing and closing the magical conduit.
  [CLEANUP] Lab workspace reset.

'''


# Zero unstable factor (ZeroDivisionError)
activate_conduit(75, 0)   

'''
--- Activating Conduit (Power: 75, Unstable: 0) ---
  Unstable factor cannot be zero!
  [CLEANUP] Securing and closing the magical conduit.
  [CLEANUP] Lab workspace reset.

'''