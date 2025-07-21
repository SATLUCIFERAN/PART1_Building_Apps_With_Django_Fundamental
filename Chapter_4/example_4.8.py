
# 'global_mana_pool', 'current_weather' is a global variable
global_mana_pool = 500
current_weather = "Sunny" 

def cast_weather_spell(new_weather):
    # We can READ 'global_mana_pool' here
    print(f"Inside function: Current global mana: {global_mana_pool}")
    print(f"Inside function: Changing weather to {new_weather}.")
   

print(f"Outside function (before spell): Global Mana: {global_mana_pool}, Weather: {current_weather}")
cast_weather_spell("Rainy")
print(f"Outside function (after spell): Global Mana: {global_mana_pool}, Weather: {current_weather}")

'''
Outside function (before spell): Global Mana: 500, Weather: Sunny
Inside function: Current global mana: 500
Inside function: Changing weather to Rainy.
Outside function (after spell): Global Mana: 500, Weather: Sunny

'''



# Output (without 'global' keyword for current_weather):
# Outside function (before spell): Global Mana: 500, Weather: Sunny
# Inside function: Current global mana: 500
# Inside function: Changing weather to Rainy.
# Outside function (after spell): Global Mana: 500, Weather: Sunny (Weather remains Sunny because 'current_weather' inside the function was a NEW local variable unless 'global' was used)
