
# Non-Pythonic: Explicitly checking for empty or None
quest_list = []
if len(quest_list) == 0:
    print("No quests available.")

active_spell = None
if active_spell is None:
    print("No active spell.")

'''
No quests available.
No active spell.

'''



# Pythonic: Leveraging truthiness/falsiness
quest_list = []
print("\n--- Pythonic Quest Check ---")
if not quest_list: # Checks if the list is empty (Falsy)
    print("No quests available (Pythonic).")

active_spell = None
if not active_spell: # Checks if active_spell is None (Falsy)
    print("No active spell (Pythonic).")

# For checking if something IS NOT None, prefer 'is not None' for clarity
item_found = "Ancient Relic"
if item_found is not None:
    print(f"Found: {item_found}")
    

'''
--- Pythonic Quest Check ---
No quests available (Pythonic).
No active spell (Pythonic).
Found: Ancient Relic

'''