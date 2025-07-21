
artifact_status = {
    "Amulet of Ages": "Active",
    "Sword of Whispers": "Sheathed"
}
print(f"Initial Status: {artifact_status}")

# Update status of an existing artifact
artifact_status["Sword of Whispers"] = "Drawn (in Combat!)"
print(f"Updated Status: {artifact_status}") 
# Output: Updated Status: {'Amulet of Ages': 'Active',
#                          'Sword of Whispers': 'Drawn (in Combat!)'}

# Add a new artifact
artifact_status["Healing Orb"] = "Charging"
print(f"After Adding: {artifact_status}") 
# Output: After Adding: {'Amulet of Ages': 'Active',
#                        'Sword of Whispers': 'Drawn (in Combat!)',
#                        'Healing Orb': 'Charging'}
