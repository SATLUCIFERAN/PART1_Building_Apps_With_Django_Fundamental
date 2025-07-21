
quest_log = ["Defeat Goblins"]
print(f"Initial Quest Log: {quest_log}")

# Add a new quest to the end
quest_log.append("Find Lost Relic")
print(f"After Append: {quest_log}") 

# Output: After Append: ['Defeat Goblins', 'Find Lost Relic']

# Insert a high-priority quest at the beginning
quest_log.insert(0, "Rescue Captured Alchemist")
print(f"After Insert: {quest_log}")

# Output: After Insert: ['Rescue Captured Alchemist', 'Defeat Goblins', 'Find Lost Relic']



