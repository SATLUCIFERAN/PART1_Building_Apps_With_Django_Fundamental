
class MagicalCreature:
    """A general blueprint for all magical creatures."""
    def __init__(self, name, health, mana):
        self.name = name
        self.health = health
        self.mana = mana
        print(f"Creature '{self.name}' (Health: {self.health}, Mana: {self.mana}) emerges.")

    def attack(self, target):
        if self.mana >= 10:
            self.mana -= 10
            print(f"  {self.name} attacks {target}!")
            return True
        else:
            print(f"  {self.name} is too tired to attack.")
            return False

    def display_status(self):
        print(f"  {self.name} Status: Health={self.health}, Mana={self.mana}")

class Dragon(MagicalCreature):
    """A specialized blueprint for Dragons, inheriting from MagicalCreature."""
    def __init__(self, name, health, mana, fire_breath_strength):
        # Call the parent's constructor to set up basic creature attributes
        super().__init__(name, health, mana)
        self.fire_breath_strength = fire_breath_strength # New attribute specific to Dragon
        print(f"  Dragon '{self.name}' breathes fire with strength {self.fire_breath_strength}.")

    def breathe_fire(self, target):
        """Dragon's unique fire breath attack."""
        if self.mana >= 25:
            self.mana -= 25
            print(f"  *ROAR!* {self.name} unleashes a torrent of fire on {target}, dealing {self.fire_breath_strength} fire damage!")
            return True
        else:
            print(f"  {self.name} doesn't have enough mana for fire breath.")
            return False

    # Dragons can override the generic attack method to be more powerful
    def attack(self, target):
        print(f"  {self.name} lunges with claws and teeth!")
        return super().attack(target) # Call the parent's attack method too, if desired

class Unicorn(MagicalCreature):
    """A specialized blueprint for Unicorns, inheriting from MagicalCreature."""
    def __init__(self, name, health, mana, horn_healing_power):
        super().__init__(name, health, mana)
        self.horn_healing_power = horn_healing_power # New attribute specific to Unicorn
        print(f"  Unicorn '{self.name}' radiates healing energy with power {self.horn_healing_power}.")

    def heal_with_horn(self, target):
        """Unicorn's unique healing ability."""
        if self.mana >= 15:
            self.mana -= 15
            print(f"  {self.name}'s horn glows, healing {target} for {self.horn_healing_power} health!")
            return True
        else:
            print(f"  {self.name} is too drained to heal.")
            return False

print("--- Conjuring Creatures ---")
smaug = Dragon("Smaug", 500, 200, 150)
sparkle = Unicorn("Sparkle", 100, 80, 40)

print("\n--- Creatures in Action ---")
smaug.display_status()
smaug.breathe_fire("Adventurer Party")
smaug.attack("Stone Wall") # Uses Dragon's overridden attack
smaug.display_status()

sparkle.display_status()
sparkle.heal_with_horn("Injured Squirrel")
sparkle.attack("Dark Shadow") # Uses inherited attack
sparkle.display_status()
