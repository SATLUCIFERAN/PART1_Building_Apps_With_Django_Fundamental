
import functools # Used to preserve original function metadata

def spell_logger(func):
    """
    A decorator that logs when a spell is cast and its arguments.
    """
    @functools.wraps(func) # Preserves original function's name, docstring, etc.
    def wrapper(*args, **kwargs):
        print(f"\n--- LOG: Casting spell '{func.__name__}' ---")
        print(f"LOG: With arguments: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs) # Execute the original function
        print(f"LOG: Spell '{func.__name__}' completed. Result: {result}")
        return result
    return wrapper

# Now, let's decorate our spells
@spell_logger # This is the decorator syntax!
def cast_fireball(target, power):
    print(f"  *WHOOSH!* Fireball unleashed on {target} with {power} power!")
    return f"Fireball hit {target}"

@spell_logger
def brew_healing_potion(herbs_count):
    print(f"  Brewing a healing potion with {herbs_count} herbs...")
    return "Healing Potion Brewed"

# Casting the decorated spells
cast_fireball("Dark Sorcerer", 100)

'''
--- LOG: Casting spell 'cast_fireball' ---
LOG: With arguments: args=('Dark Sorcerer', 100), kwargs={}
  *WHOOSH!* Fireball unleashed on Dark Sorcerer with 100 power!
LOG: Spell 'cast_fireball' completed. Result: Fireball hit Dark Sorcerer
'''

# Casting the decorated spells
brew_healing_potion(herbs_count=5)

'''
--- LOG: Casting spell 'brew_healing_potion' ---
LOG: With arguments: args=(), kwargs={'herbs_count': 5}
  Brewing a healing potion with 5 herbs...
LOG: Spell 'brew_healing_potion' completed. Result: Healing Potion Brewed

'''