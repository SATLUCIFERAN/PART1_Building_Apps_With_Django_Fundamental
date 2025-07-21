
alchemist_name = "Elara"
potion_name = "Elixir of Vitality"
potion_count = 3
is_rare = True
flask_size = 150.75 # ml

# Traditional way (less readable)
# message_old = "Alchemist " + alchemist_name + " has " + str(potion_count) + " " + potion_name + "s."

# Using f-strings (much more readable and powerful)
message_fstring = f"Alchemist {alchemist_name} has {potion_count} {potion_name}s."
print(message_fstring) # Output: Alchemist Elara has 3 Elixir of Vitalitys.

# You can include expressions and formatting directly
status_report = f"Inventory: {potion_name} (x{potion_count}), Rare: {is_rare}. Total volume: {flask_size:.2f} ml."
print(status_report) # Output: Inventory: Elixir of Vitality (x3), Rare: True. Total volume: 150.75 ml.
