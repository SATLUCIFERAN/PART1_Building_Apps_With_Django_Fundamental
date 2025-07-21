
def brew_potion(ingredient1, ingredient2, catalyst, duration_minutes):
    print(f"Brewing with {ingredient1}, {ingredient2}, and {catalyst} for {duration_minutes} minutes.")

# Using keyword arguments for clarity
brew_potion(ingredient1="Moonpetal", ingredient2="Dragon's Scale", 
            catalyst="Sunstone Dust", duration_minutes=30)
# Output: Brewing with Moonpetal, Dragon's Scale, and Sunstone Dust for 30 minutes.

# Order doesn't matter with keyword arguments
brew_potion(duration_minutes=45, catalyst="Phoenix Tear",
            ingredient1="Star Dust", ingredient2="Crystal Shard")
# Output: Brewing with Star Dust, Crystal Shard, and Phoenix Tear for 45 minutes.
