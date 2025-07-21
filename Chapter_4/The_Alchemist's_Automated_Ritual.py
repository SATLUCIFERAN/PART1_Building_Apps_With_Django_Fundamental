
import time
import functools

# --- Decorator: The Ritual Timer Sigil ---
def ritual_timer(func):
    """A decorator that times how long a ritual (function) takes."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        print(f"\n--- Ritual '{func.__name__}' begins... ---")
        result = func(*args, **kwargs) # Execute the original ritual
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"--- Ritual '{func.__name__}' completed in {duration:.4f} seconds. ---")
        return result
    return wrapper

# --- Context Manager: The Sacred Altar Chamber ---
class SacredAltar:
    """A context manager to ensure the altar is prepared and cleaned."""
    def __init__(self, altar_name):
        self.altar_name = altar_name

    def __enter__(self):
        print(f"\n[ALTAR LOG] Preparing the '{self.altar_name}' altar chamber...")
        print("[ALTAR LOG] Sacred energies are flowing. Chamber is ready.")
        return self # You can return self, or any object to be used with 'as'

    def __exit__(self, exc_type, exc_val, exc_tb):
        # exc_type, exc_val, exc_tb are for error handling (we'll cover errors later)
        if exc_type:
            print(f"[ALTAR LOG] Ritual in '{self.altar_name}' ended with an error: {exc_val}")
        print(f"[ALTAR LOG] Cleaning the '{self.altar_name}' altar chamber...")
        print("[ALTAR LOG] Sacred energies dispersed. Chamber is sealed.")
        return False # False means propagate exception, True means suppress it

# --- Rituals using both ---

@ritual_timer # Decorate the function with the timer
def perform_complex_transmutation(item_name, target_element):
    """A complex transmutation ritual."""
    with SacredAltar("Transmutation Altar") as altar: # Use the context manager
        print(f"  Transmuting '{item_name}' into '{target_element}'...")
        time.sleep(1.2) # Simulate long magical process
        if "lead" in item_name.lower() and "gold" in target_element.lower():
            print("  *SHIMMER!* Lead successfully transmuted into gleaming gold!")
            return f"Gleaming {target_element} from {item_name}"
        else:
            print("  Transmutation failed. Unsuitable materials.")
            return "Failed Transmutation"

@ritual_timer
def invoke_ancient_spirit(spirit_name):
    """Ritual to invoke an ancient spirit."""
    with SacredAltar("Invocation Circle") as circle:
        print(f"  Chanting ancient words to invoke '{spirit_name}'...")
        time.sleep(0.8)
        print(f"  '{spirit_name}' appears! (Briefly).")
        return f"Spirit '{spirit_name}' invoked"

# --- Execute the rituals ---
perform_complex_transmutation("Chunk of Lead", "Gold")
invoke_ancient_spirit("Whispering Shade")
