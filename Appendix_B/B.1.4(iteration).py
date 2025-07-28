

# Non-Pythonic: Iterating by index when not needed
creature_types = ["Forest Sprite", "Stone Golem"]
for i in range(len(creature_types)):
    print(f"Encountering a {creature_types[i]}")


'''
Encountering a Forest Sprite
Encountering a Stone Golem

'''



# Pythonic: Direct iteration over the list
creature_types = ["Forest Sprite", "Stone Golem"]
print("\n--- Pythonic Creature Encounters ---")
for creature in creature_types:
    print(f"Encountering a {creature}")
    

'''
--- Pythonic Creature Encounters ---
Encountering a Forest Sprite
Encountering a Stone Golem

'''