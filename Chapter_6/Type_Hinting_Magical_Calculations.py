
# To use List, Dict, etc. for type hints, import from 'typing'
from typing import List, Dict, Union, Tuple

def calculate_spell_damage(base_damage: int, multiplier: float) -> float:
    """
    Calculates the final spell damage.
    :param base_damage: The base integer damage.
    :param multiplier: The float multiplier for damage.
    :return: The final damage as a float.
    """
    final_damage = base_damage * multiplier
    return final_damage

def get_artifact_details(artifact_id: int, artifact_catalog: 
                         Dict[int, Dict[str, Union[str, int]]])-> Union[Dict[str, Union[str, int]], None]:
    """
    Retrieves details of an artifact from a catalog.
    :param artifact_id: The ID of the artifact.
    :param artifact_catalog: A dictionary mapping artifact IDs to their details.
    :return: A dictionary of artifact details, or None if not found.
    """
    return artifact_catalog.get(artifact_id)

# Using the functions with type hints
print("--- Spell Damage Calculation ---")
damage_output = calculate_spell_damage(50, 1.75)
print(f"Calculated damage: {damage_output}")

'''
--- Spell Damage Calculation ---
Calculated damage: 87.5

'''

# Catalog of artifacts (ID -> {name, power})
my_artifact_catalog: Dict[int, Dict[str, Union[str, int]]] = {
    101: {"name": "Amulet of Ages", "power": 90},
    102: {"name": "Sword of Whispers", "power": 75}
}

print("\n--- Artifact Details Retrieval ---")
amulet_details = get_artifact_details(101, my_artifact_catalog)
print(f"Amulet Details: {amulet_details}")

'''
--- Artifact Details Retrieval ---
Amulet Details: {'name': 'Amulet of Ages', 'power': 90}

'''


non_existent_artifact = get_artifact_details(999, my_artifact_catalog)
print(f"Non-existent Artifact: {non_existent_artifact}")
# Output: Non-existent Artifact: None




