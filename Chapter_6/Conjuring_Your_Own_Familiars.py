

class MagicalFamiliar:
    """
    A blueprint for creating magical familiar companions.
    """

    def __init__(self, name, species, magical_affinity, initial_energy):
        """
        The constructor spell to imbue the familiar with initial characteristics.
        """
        self.name = name                 # Attribute: The familiar's name
        self.species = species           # Attribute: The familiar's species (e.g., 'Sprite', 'Imp')
        self.magical_affinity = magical_affinity # Attribute: Its primary magical element
        self.energy = initial_energy     # Attribute: Its current energy level
        self.is_loyal = True             # Attribute: Default state

        print(f"Familiar '{self.name}' ({self.species}) has been conjured!")

    def display_familiar_info(self):
        """Method to display the familiar's current information."""
        print(f"\n--- Familiar Profile: {self.name} ---")
        print(f"  Species: {self.species}")
        print(f"  Affinity: {self.magical_affinity}")
        print(f"  Energy: {self.energy} units")
        print(f"  Loyalty: {'Loyal' if self.is_loyal else 'Questionable'}")

    def use_energy(self, amount):
        """Method to reduce familiar's energy."""
        if self.energy >= amount:
            self.energy -= amount
            print(f"  {self.name} used {amount} energy. Remaining: {self.energy}")
            return True
        else:
            print(f"  {self.name} is too tired to perform that action (needs {amount} energy, has {self.energy}).")
            return False

    def recharge_energy(self, amount):
        """Method to recharge familiar's energy."""
        self.energy += amount
        print(f"  {self.name} recharged {amount} energy. New energy: {self.energy}")



# Conjure a Fire Sprite familiar
sparky = MagicalFamiliar("Sparky", "Fire Sprite", "Fire", 80)
sparky.display_familiar_info()

'''
Familiar 'Sparky' (Fire Sprite) has been conjured!

--- Familiar Profile: Sparky ---
  Species: Fire Sprite
  Affinity: Fire
  Energy: 80 units
  Loyalty: Loyal

'''

# Conjure an Earth Imp familiar
rocky = MagicalFamiliar("Rocky", "Earth Imp", "Earth", 120)
rocky.display_familiar_info()

'''
Familiar 'Rocky' (Earth Imp) has been conjured!

--- Familiar Profile: Rocky ---
  Species: Earth Imp
  Affinity: Earth
  Energy: 120 units
  Loyalty: Loyal

'''

# Now, let your familiars perform actions (call their methods)

sparky.use_energy(30) # Sparky uses energy
# Output: Sparky used 30 energy. Remaining: 50

sparky.recharge_energy(10) # Sparky recharges
# Output: Sparky recharged 10 energy. New energy: 60  





rocky.use_energy(150) # Rocky tries to use more energy than it has
# Output : Rocky is too tired to perform 
#          that action (needs 150 energy, has 120).

rocky.display_familiar_info() # Check Rocky's energy

'''
--- Familiar Profile: Rocky ---
  Species: Earth Imp
  Affinity: Earth
  Energy: 120 units
  Loyalty: Loyal

'''