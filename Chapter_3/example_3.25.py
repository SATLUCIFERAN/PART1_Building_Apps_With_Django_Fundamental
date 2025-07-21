
spell_list = [
    {"name": "Fireball", "element": "fire"},
    {"name": "Aqua Blast", "element": "water"},
    {"name": "Stone Skin", "element": "earth"},
    {"name": "Wind Gust", "element": "air"},
    {"name": "Magma Burst", "element": "fire"} # Duplicate element
]


unique_affinities = {
    spell["element"] for spell in spell_list
}
print(f"Unique Elemental Affinities: {unique_affinities}")
# Output: Unique Elemental Affinities: {'earth', 'fire', 'air', 'water'} 
# (order may vary)
