
# Import directly from a module within a sub-package
from spells.offensive.fireball import unleash_fireball

# Import a module from a sub-package
import spells.defensive.shield

# Import a module from a sub-package with an alias
# CORRECTED: Ensure teleport.py exists and has teleport_to_location
import spells.utility.teleport as teleport_charm

print("--- The Grand Quest Begins ---")

# Cast a spell from the 'offensive' sub-package
unleash_fireball("Ancient Lich", 90)
# Output:  *BOOM!* A searing fireball engulfs Ancient Lich with intensity 90!

# Cast a spell from the 'defensive' sub-package (using full path)
spells.defensive.shield.cast_protective_shield(60)
# Output:  *SHIMMER!* A shimmering shield forms, lasting 60 seconds.

# Cast a spell from the 'utility' sub-package (using alias)
# CORRECTED: Call the correct function name
teleport_charm.teleport_to_location("Mystic Glade")
# Output: *WHOOSH!* Teleporting to Mystic Glade with a burst of arcane energy!