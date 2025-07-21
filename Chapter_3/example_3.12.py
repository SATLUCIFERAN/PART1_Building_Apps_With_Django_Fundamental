
magical_artifacts = {
    "Amulet of Ages": "Grants wearer wisdom of past eras.",
    "Sword of Whispers": "Can communicate with ancient spirits.",
}

amulet_description = magical_artifacts["Amulet of Ages"]
print(f"Amulet Description: {amulet_description}") 
# Output: Amulet Description: Grants wearer wisdom of past eras.

# This would cause a KeyError if you uncomment it:
# non_existent_artifact = magical_artifacts["Staff of Power"]


