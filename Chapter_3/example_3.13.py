
magical_artifacts = {
    "Amulet of Ages": "Grants wearer wisdom of past eras.",
    "Sword of Whispers": "Can communicate with ancient spirits.",
}

orb_description = magical_artifacts.get("Orb of Foresight", 
                                        "Description not found in this encyclopedia.")
print(f"Orb Description: {orb_description}") 
# Output: Orb Description: Description not found in this encyclopedia.

sword_description = magical_artifacts.get("Sword of Whispers") # Default is None if not found
print(f"Sword Description: {sword_description}") 
# Output: Sword Description: Can communicate with ancient spirits.






