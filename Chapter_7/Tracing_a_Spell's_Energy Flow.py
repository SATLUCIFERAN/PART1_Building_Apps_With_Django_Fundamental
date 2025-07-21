
class MagicalFocus:
    def __init__(self, name: str, initial_charge: int):
        self.name = name
        self.charge = initial_charge
        self.overcharge_limit = 200
        self.drain_rate = 10

    def infuse_energy(self, amount: int):
        # Set breakpoint here
        self.charge += amount
        if self.charge > self.overcharge_limit:
            print(f"  WARNING: {self.name} is overcharged! Reducing to limit.")
            self.charge = self.overcharge_limit
        print(f"  {self.name} infused with {amount} energy. New charge: {self.charge}")

    def cast_minor_spell(self):
        if self.charge >= self.drain_rate:
            self.charge -= self.drain_rate
            print(f"  {self.name} casts minor spell. Charge remaining: {self.charge}")
            return True
        else:
            print(f"  {self.name} has insufficient charge for minor spell.")
            return False

# --- Main simulation ---
print("--- Tracing Magical Focus Energy ---")
my_focus = MagicalFocus("Aura Amplifier", 50)

my_focus.infuse_energy(80) # Infuse some energy
my_focus.cast_minor_spell() # Cast a spell
my_focus.infuse_energy(100) # Infuse more energy (might overcharge)
my_focus.cast_minor_spell()
my_focus.cast_minor_spell()
my_focus.cast_minor_spell() # Try to drain it
