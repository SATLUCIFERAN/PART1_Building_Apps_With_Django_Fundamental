
from typing import List, Tuple, Optional

class SpellComponent:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def __repr__(self) -> str: # A method to represent the object as a string
        return f"Component({self.name}, {self.quantity})"

class PotionRecipe:
    def __init__(self, name: str, components: List[SpellComponent], difficulty: int):
        self.name = name
        self.components = components
        self.difficulty = difficulty

    def calculate_total_ingredients(self) -> int:
        total = 0
        for comp in self.components:
            total += comp.quantity
        return total

    def is_complex_recipe(self) -> bool:
        return self.difficulty > 5

def find_recipe_by_component(component_name: str, recipes: List[PotionRecipe]) -> Optional[PotionRecipe]:
    """
    Finds a potion recipe that includes a specific component.
    Returns the recipe or None if not found.
    """
    for recipe in recipes:
        for component in recipe.components:
            if component.name == component_name:
                return recipe
    return None

# --- Define some components and recipes ---
herb: SpellComponent = SpellComponent("Moonpetal", 5)
water: SpellComponent = SpellComponent("Purified Water", 10)
fire_essence: SpellComponent = SpellComponent("Volatile Fire Essence", 2)
dragon_scale: SpellComponent = SpellComponent("Dragon Scale", 1)

healing_recipe: PotionRecipe = PotionRecipe(
    "Greater Healing Potion",
    [herb, water],
    4
)

fire_storm_recipe: PotionRecipe = PotionRecipe(
    "Firestorm Elixir",
    [fire_essence, dragon_scale, water],
    8
)

all_recipes: List[PotionRecipe] = [healing_recipe, fire_storm_recipe]

print("--- Recipe Analysis System ---")

# Find a recipe using 'Moonpetal'
found_healing = find_recipe_by_component("Moonpetal", all_recipes)
if found_healing:
    print(f"\nFound recipe for '{found_healing.name}' using Moonpetal.")
    print(f"  Total ingredients: {found_healing.calculate_total_ingredients()}")
    print(f"  Is complex: {found_healing.is_complex_recipe()}")

# Find a recipe using 'Dragon Scale'
found_firestorm = find_recipe_by_component("Dragon Scale", all_recipes)
if found_firestorm:
    print(f"\nFound recipe for '{found_firestorm.name}' using Dragon Scale.")
    print(f"  Total ingredients: {found_firestorm.calculate_total_ingredients()}")
    print(f"  Is complex: {found_firestorm.is_complex_recipe()}")

# What if we pass an incorrect type (mypy would warn us!)
# find_recipe_by_component(123, all_recipes) # mypy would flag this!