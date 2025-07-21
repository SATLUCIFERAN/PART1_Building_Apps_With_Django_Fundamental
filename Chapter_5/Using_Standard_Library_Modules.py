
import math
import random
import datetime
import os # For interacting with the operating system
import sys # For system-specific parameters and functions

print("--- Consulting the Grand Library ---")

# Math module: Calculating spell range (square root)
base_range_power = 144
spell_range = math.sqrt(base_range_power)
print(f"Calculated Spell Range: {spell_range:.0f} units (using math.sqrt)")
# Output: Calculated Spell Range: 12 units (using math.sqrt)

# Random module: Rolling a magical die
dice_roll = random.randint(1, 20) # Roll a 20-sided die
print(f"Magical Die Roll: {dice_roll}")
# Output: Magical Die Roll: 20

# Datetime module: Timestamping a ritual
current_ritual_time = datetime.datetime.now()
print(f"Current Ritual Timestamp: {current_ritual_time}")
# Output: Current Ritual Timestamp: 2025-07-19 18:21:38.171795

formatted_time = current_ritual_time.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted Timestamp: {formatted_time}")
# Output: Formatted Timestamp: 2025-07-19 18:21:38

# OS module: Checking current working directory
current_location = os.getcwd()
print(f"Current Alchemist Location (Directory): {current_location}")
# Output: Current Alchemist Location (Directory): 
#         C:\Users\ASUS\Desktop\Python_book4\Chapter_5

# Sys module: Checking Python version
python_version = sys.version
print(f"Python Interpreter Version: {python_version.split(' ')[0]}")
# Output: Python Interpreter Version: 3.12.5
