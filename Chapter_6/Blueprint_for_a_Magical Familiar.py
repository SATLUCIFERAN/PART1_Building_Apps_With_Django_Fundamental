
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
