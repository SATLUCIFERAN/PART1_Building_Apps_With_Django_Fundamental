
class MagicalOrb:
    """
    An Orb with encapsulated internal workings.
    """
    def __init__(self, name, initial_charge):
        # Public attribute
        self.name = name
        # Protected attribute (by convention)
        self._internal_energy_conduit = initial_charge
        # "Private" attribute (name mangled) 
        self.__secret_calibration_factor = 1.2 

    def _recalibrate_conduit(self): # Protected method
        """Internal method to recalibrate energy conduit."""
        print(f"  [Internal Process] Recalibrating {self.name}'s energy conduit.")
        self._internal_energy_conduit *= self.__secret_calibration_factor
        print(f"  [Internal Process] Conduit now at {self._internal_energy_conduit:.2f} charge.")

    def activate_orb(self): # Public method
        """Activates the orb, triggering internal processes."""
        print(f"\nActivating {self.name}...")
        # Public method can call protected/private methods
        self._recalibrate_conduit() 
        print(f"  {self.name} glows brightly! Current charge:{self._internal_energy_conduit:.2f}")

    def get_charge(self): # Public method (getter)
        """Public method to safely get the orb's charge."""
        return self._internal_energy_conduit

# Create an orb
my_orb = MagicalOrb("Power Orb", 100)

# Accessing public attribute is fine
print(f"Orb Name: {my_orb.name}")
# Output: Orb Name: Power Orb

# Accessing protected attribute (possible, but discouraged directly)
print(f"Direct access to protected conduit (discouraged):{my_orb._internal_energy_conduit}")
# Output: Direct access to protected conduit (discouraged): 100

# Attempting to access "private" attribute (will likely fail directly)
# print(my_orb.__secret_calibration_factor) 
#AttributeError: 'MagicalOrb' object has no attribute '__secret_calibration_factor'
#Python renames it to _MagicalOrb__secret_calibration_factor internally

# Interact with the orb through its public methods
my_orb.activate_orb()
print(f"Orb's charge via getter: {my_orb.get_charge()}")

'''
Activating Power Orb...
  [Internal Process] Recalibrating Power Orb's energy conduit.
  [Internal Process] Conduit now at 120.00 charge.
  Power Orb glows brightly! Current charge:120.00
Orb's charge via getter: 120.0

'''

# Attempting to call protected method directly (possible, but discouraged)
my_orb._recalibrate_conduit()

'''
 [Internal Process] Recalibrating Power Orb's energy conduit.
 [Internal Process] Conduit now at 120.00 charge.

'''