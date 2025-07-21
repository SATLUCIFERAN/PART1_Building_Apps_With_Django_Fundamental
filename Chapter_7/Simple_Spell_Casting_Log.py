
import logging

# Configure basic logging: messages will go to the console
# Default level is WARNING, so DEBUG and INFO messages won't show unless you change it.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def cast_light_spell(target):
    logging.debug(f"Attempting to cast light spell on {target}...") # This won't show with INFO level
    print(f"  *SHIMMER!* Light spell cast on {target}.")
    logging.info(f"Successfully cast light spell on {target}.")

def cast_dark_curse(target):
    logging.warning(f"Casting a dark curse on {target}. This is a dangerous spell.")
    print(f"  *SHADOWS GATHER!* Dark curse unleashed on {target}.")
    # Simulate a potential error
    try:
        result = 10 / 0 # This will cause a ZeroDivisionError
    except ZeroDivisionError:
        logging.error(f"Failed to calculate curse effect for {target} due to division by zero!")
        print("  Curse fizzled due to internal error.")

# print("--- Alchemist's Daily Log ---")
# cast_light_spell("Apprentice John")

cast_dark_curse("Goblin King")

'''
2025-07-20 16:41:36,629 - WARNING 
- Casting a dark curse on Goblin King. This is a dangerous spell.
  *SHADOWS GATHER!* Dark curse unleashed on Goblin King.
2025-07-20 16:41:36,630 - ERROR 
- Failed to calculate curse effect for Goblin King due to division by zero!
  Curse fizzled due to internal error.
'''