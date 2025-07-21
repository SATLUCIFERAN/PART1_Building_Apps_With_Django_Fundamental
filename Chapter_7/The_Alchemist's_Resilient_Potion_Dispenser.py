
import random

def dispense_potion(potion_name, quantity):
    """
    Attempts to dispense a potion. Handles various errors gracefully.
    Always logs the outcome.
    """
    dispenser_status = "Unknown"
    try:
        print(f"\n--- Attempting to dispense {quantity} x '{potion_name}' ---")
        if quantity <= 0:
            raise ValueError("Quantity must be positive!")

        if potion_name not in ["Healing Potion", "Mana Elixir", "Invisibility Brew"]:
            raise KeyError(f"Potion '{potion_name}' not found in dispenser's inventory!")

        # Simulate various dispense outcomes
        if random.random() < 0.1: # 10% chance of a critical failure
            raise RuntimeError("Critical Dispenser Malfunction! Emergency Shutdown!")
        elif random.random() < 0.3: # 30% chance of insufficient ingredients
            raise IndexError("Insufficient ingredients in dispenser reservoir.")
        else:
            # Successful dispense
            print(f"  Dispensing {quantity} x '{potion_name}'... *GLUG GLUG*")
            dispenser_status = "Success"

    except ValueError as e:
        print(f"  Dispense Error: Invalid Request - {e}")
        dispenser_status = "Invalid Request"
    except KeyError as e:
        print(f"  Dispense Error: Inventory Issue - {e}")
        dispenser_status = "Potion Not Found"
    except IndexError as e:
        print(f"  Dispense Error: Resource Depletion - {e}")
        dispenser_status = "Out of Stock"
    except RuntimeError as e:
        print(f"  Dispense Error: SYSTEM CRITICAL - {e}")
        dispenser_status = "Critical Failure"
    except Exception as e: # Catch any other unforeseen magical anomaly
        print(f"  An unexpected cosmic anomaly occurred during dispense: {e}")
        dispenser_status = "Unhandled Anomaly"
    else:
        # This block runs ONLY if no exception occurred in the 'try' block
        print(f"  Dispense operation completed perfectly. Customer satisfied!")
    finally:
        # This block ALWAYS runs, for final logging/cleanup
        print(f"  [DISPENSER LOG] Final Dispenser State: {dispenser_status}")
        print("  [DISPENSER LOG] Dispenser ready for next order.")

# Test various scenarios
dispense_potion("Healing Potion", 2) # Likely success
dispense_potion("Mana Elixir", 0)    # ValueError
dispense_potion("Strength Potion", 1) # KeyError
dispense_potion("Invisibility Brew", 3) # May hit IndexError or RuntimeError
dispense_potion("Healing Potion", 1) # Another attempt