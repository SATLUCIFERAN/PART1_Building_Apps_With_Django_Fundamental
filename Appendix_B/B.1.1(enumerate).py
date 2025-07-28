
# Non-Pythonic: Manually managing an index
artifact_names = ["Amulet of Aethel", "Orb of Whispers", "Ever-Burning Lamp"]
index = 0
for name in artifact_names:
    print(f"Artifact {index}: {name}")
    index += 1

'''
Artifact 0: Amulet of Aethel
Artifact 1: Orb of Whispers
Artifact 2: Ever-Burning Lamp

'''





# Pythonic: enumerate() provides index and value directly
artifact_names = ["Amulet of Aethel", "Orb of Whispers", "Ever-Burning Lamp"]
print("--- Pythonic Artifact Listing ---")
for index, name in enumerate(artifact_names):
    print(f"Artifact {index}: {name}")

'''
--- Pythonic Artifact Listing ---
Artifact 0: Amulet of Aethel
Artifact 1: Orb of Whispers
Artifact 2: Ever-Burning Lamp

'''