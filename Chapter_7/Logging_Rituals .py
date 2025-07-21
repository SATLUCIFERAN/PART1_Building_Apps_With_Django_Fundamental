import logging

# Create a logger instance
ritual_logger = logging.getLogger('ritual_events')
ritual_logger.setLevel(logging.DEBUG) # Set this logger to capture all levels

# Create a file handler
file_handler = logging.FileHandler('ritual_log.txt')
file_handler.setLevel(logging.DEBUG) # File handler also captures all levels

# Create a formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the handler to the logger
ritual_logger.addHandler(file_handler)

# Optionally, also send to console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO) # Console only shows INFO and above
console_handler.setFormatter(formatter)
ritual_logger.addHandler(console_handler)

def perform_ancient_ritual(ritual_name, participants):
    ritual_logger.debug(f"Initiating '{ritual_name}' ritual with {participants} participants.")
    try:
        print(f"\n--- Performing '{ritual_name}' ritual ---")
        if not participants:
            raise ValueError("Ritual requires participants!")
        if len(participants) < 2:
            ritual_logger.warning("Ritual with few participants. May be less effective.")

        # Simulate ritual steps
        print("  Chanting incantations...")
        print("  Gathering energies...")
        # Simulate a random success/failure
        if random.random() > 0.8: # 20% chance of failure
            raise RuntimeError("Ritual energies became unstable!")

        print("  Ritual completed successfully!")
        ritual_logger.info(f"Ritual '{ritual_name}' completed successfully.")
    except ValueError as e:
        ritual_logger.error(f"Ritual '{ritual_name}' failed due to invalid setup: {e}")
    except RuntimeError as e:
        ritual_logger.critical(f"Ritual '{ritual_name}' CRITICAL FAILURE: {e}")
    except Exception as e:
        ritual_logger.exception(f"An unexpected error occurred during '{ritual_name}'.") # logging.exception includes traceback!

import random # Ensure random is imported

perform_ancient_ritual("Binding of Shadows", ["Elara", "Kael"])
perform_ancient_ritual("Summoning Lesser Imp", []) # No participants
perform_ancient_ritual("Grand Transmutation", ["Master Alchemist", "Journeyman"]) # May fail randomly
