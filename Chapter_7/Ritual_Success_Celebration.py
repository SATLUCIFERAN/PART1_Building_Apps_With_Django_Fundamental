
import random # Make sure random is imported

def perform_risky_ritual(success_chance):
    try:
        print(f"\n--- Performing Risky Ritual \
               (Success Chance: {success_chance}) ---")
        # random.random() gives a float between 0.0 and 1.0
        if random.random() < success_chance: 
            print("  Ritual succeeded without a hitch!")
        else:
            # Deliberately raise an error
            raise ValueError("Ritual failed due to unstable energies!") 
        
    except ValueError as e:
        print(f"  Ritual encountered a specific issue: {e}")
    except Exception as e:
        print(f"  An unexpected magical anomaly occurred: {e}")
    else:
        print("  Ritual completed perfectly! Initiating success celebration!")
        # This block only runs if NO exception was raised in the 'try'
        print("  *Fireworks of magic burst forth!*")
    finally:
        print("  Ritual chamber cleanup initiated.") # This always runs


# High chance of success
perform_risky_ritual(0.8) 

'''
--- Performing Risky Ritual (Success Chance: 0.8) ---
  Ritual succeeded without a hitch!
  Ritual completed perfectly! Initiating success celebration!
  *Fireworks of magic burst forth!*
  Ritual chamber cleanup initiated.

'''

# Low chance of success (likely to fail)
perform_risky_ritual(0.2) 

'''
--- Performing Risky Ritual (Success Chance: 0.2) ---
  Ritual encountered a specific issue: Ritual failed due to unstable energies!
  Ritual chamber cleanup initiated.

'''