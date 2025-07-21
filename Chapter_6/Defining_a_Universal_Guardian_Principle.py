
from abc import ABC, abstractmethod

class Guardian(ABC): # Inherit from ABC to make it an abstract class
    """
    An abstract blueprint for all magical guardians.
    Defines methods that ALL guardians MUST implement.
    """
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    @abstractmethod # This method MUST be implemented by subclasses
    def defend(self, threat):
        """Abstract method: How the guardian defends against a threat."""
        pass # No implementation here, just a placeholder

    @abstractmethod # This method MUST be implemented by subclasses
    def alert(self, message):
        """Abstract method: How the guardian alerts others."""
        pass

    def report_status(self):
        """Concrete method: Can be implemented in abstract class and inherited."""
        print(f"{self.name} (Strength: {self.strength}) reporting for duty.")

# --- Concrete Guardian Implementations ---

class StoneGuardian(Guardian):
    """A guardian crafted from stone."""
    def __init__(self, name, strength, material):
        super().__init__(name, strength)
        self.material = material
        print(f"  {self.name} (Stone Guardian) stands ready.")

    def defend(self, threat):
        """Stone Guardian's specific defense."""
        print(f"  {self.name} solidifies its {self.material} form against {threat}!")

    def alert(self, message):
        """Stone Guardian's specific alert."""
        print(f"  {self.name} emits a low, rumbling alert: '{message}'")

class SpiritGuardian(Guardian):
    """A guardian formed from pure spirit."""
    def __init__(self, name, strength, ethereal_form):
        super().__init__(name, strength)
        self.ethereal_form = ethereal_form
        print(f"  {self.name} (Spirit Guardian) shimmers into existence.")

    def defend(self, threat):
        """Spirit Guardian's specific defense."""
        print(f"  {self.name} phases through {threat}, dissipating its energy!")

    def alert(self, message):
        """Spirit Guardian's specific alert."""
        print(f"  {self.name} sends a telepathic warning: '{message}'")


# This would cause an error (TypeError: Can't instantiate abstract class Guardian)
# generic_guardian = Guardian("Generic Sentinel", 50)

print("--- Attempting to Conjure Guardians ---")
stone_guard = StoneGuardian("Gargoyle Sentinel", 80, "Granite")
spirit_guard = SpiritGuardian("Whispering Watcher", 70, "Mist")

'''
--- Attempting to Conjure Guardians ---
  Gargoyle Sentinel (Stone Guardian) stands ready.
  Whispering Watcher (Spirit Guardian) shimmers into existence.

'''

print("\n--- Guardians in Action ---")
stone_guard.report_status()
stone_guard.defend("Goblin Ambush")
stone_guard.alert("Perimeter Breach!")

'''
--- Guardians in Action ---
Gargoyle Sentinel (Strength: 80) reporting for duty.
Gargoyle Sentinel solidifies its Granite form against Goblin Ambush!
Gargoyle Sentinel emits a low, rumbling alert: 'Perimeter Breach!'

'''





print("\n--- Guardians in Status ---")
spirit_guard.report_status()
spirit_guard.defend("Shadow Beast")
spirit_guard.alert("Intruder in the West Wing!")

'''
--- Guardians in Status ---
Whispering Watcher (Strength: 70) reporting for duty.
Whispering Watcher phases through Shadow Beast, dissipating its energy!
Whispering Watcher sends a telepathic warning: 'Intruder in the West Wing!'

'''