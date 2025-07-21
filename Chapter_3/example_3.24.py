
artifacts_data = [
    {"name": "Amulet of Ages", "power": 90, "rarity": "Legendary"},
    {"name": "Lesser Healing Orb", "power": 30, "rarity": "Common"},
    {"name": "Sword of Whispers", "power": 75, "rarity": "Rare"},
    {"name": "Broken Shield", "power": 5, "rarity": "Common"}
]

# Create a dictionary of powerful artifacts (name: power) : only for 'Rare' or 'Legendary'

powerful_artifacts_catalog = { 
    artifact["name"]: artifact["power"]
    for artifact in artifacts_data
    if artifact["rarity"] in ["Rare", "Legendary"]
}
print(f"Powerful Artifacts Catalog: {powerful_artifacts_catalog}")
# Output: Powerful Artifacts Catalog: {'Amulet of Ages': 90, 'Sword of Whispers': 75}
