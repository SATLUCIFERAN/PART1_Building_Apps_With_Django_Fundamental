
class MagicalArtifact:
    """A general blueprint for all magical artifacts."""
    def __init__(self, name):
        self.name = name

    def activate(self):
        """Generic activation method."""
        print(f"{self.name} hums softly. (Generic activation)")

class HealingOrb(MagicalArtifact):
    """A Healing Orb artifact."""
    def __init__(self, name, healing_power):
        super().__init__(name)
        self.healing_power = healing_power

    def activate(self):
        """Healing Orb's specific activation."""
        print(f"  {self.name} glows with warm light, radiating {self.healing_power} healing energy!")

class WarGolem(MagicalArtifact):
    """A War Golem artifact."""
    def __init__(self, name, attack_strength):
        super().__init__(name)
        self.attack_strength = attack_strength

    def activate(self):
        """War Golem's specific activation."""
        print(f"  {self.name} rumbles to life, ready to unleash {self.attack_strength} attack power!")

# Create different artifacts
orb = HealingOrb("Aura of Life", 50)
golem = WarGolem("Iron Sentinel", 120)
basic_artifact = MagicalArtifact("Ancient Relic")

# Put them in a list (treating them all as MagicalArtifacts)
artifacts_to_activate = [orb, golem, basic_artifact]
print("--- Activating All Artifacts ---")
for artifact in artifacts_to_activate:
    artifact.activate() # The SAME method call, but different behaviors!

'''
--- Activating All Artifacts ---
  Aura of Life glows with warm light, radiating 50 healing energy!
  Iron Sentinel rumbles to life, ready to unleash 120 attack power!
Ancient Relic hums softly. (Generic activation)

'''