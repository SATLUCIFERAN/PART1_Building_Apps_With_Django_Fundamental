
import json

# Python dictionary representing a magical artifact
artifact_data = {
    "name": "Orb of Foresight",
    "type": "Divination",
    "power_level": 85,
    "enchantments": ["Scrying", "Precognition"],
    "is_cursed": False,
    "origin": {
        "realm": "Ethereal Plane",
        "era": "Ancient"
    }
}

print("--- Converting Python Data to JSON (Serialization) ---")
# Convert Python dictionary to a JSON string
# indent=4 makes the JSON output human-readable with indentation
json_string = json.dumps(artifact_data, indent=4)
print(json_string)

'''
--- Converting Python Data to JSON (Serialization) ---
{
    "name": "Orb of Foresight",
    "type": "Divination",
    "power_level": 85,
    "enchantments": [
        "Scrying",
        "Precognition"
    ],
    "is_cursed": false,
    "origin": {
        "realm": "Ethereal Plane",
        "era": "Ancient"
    }
}

'''

# Save the JSON string to a file
with open("orb_of_foresight.json", "w") as json_file:
    json_file.write(json_string)
print("\nArtifact data saved to 'orb_of_foresight.json'")


print("\n--- Reading JSON from File and Converting to Python (Deserialization) ---")
# Read JSON string from the file
with open("orb_of_foresight.json", "r") as json_file:
    loaded_json_string = json_file.read()
    print(loaded_json_string)

'''
{
    "name": "Orb of Foresight",
    "type": "Divination",
    "power_level": 85,
    "enchantments": [
        "Scrying",
        "Precognition"
    ],
    "is_cursed": false,
    "origin": {
        "realm": "Ethereal Plane",
        "era": "Ancient"
    }
}

'''


# Convert JSON string back to a Python dictionary
loaded_artifact_data = json.loads(loaded_json_string)
print(f"Loaded Artifact Name: {loaded_artifact_data['name']}")
print(f"Loaded Artifact Enchantments: {loaded_artifact_data['enchantments']}")
print(f"Loaded Artifact Origin Realm: {loaded_artifact_data['origin']['realm']}")

'''
Loaded Artifact Name: Orb of Foresight
Loaded Artifact Enchantments: ['Scrying', 'Precognition']
Loaded Artifact Origin Realm: Ethereal Plane

'''



