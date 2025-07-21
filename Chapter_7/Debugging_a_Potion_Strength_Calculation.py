
# If using pdb.set_trace()
import pdb 
# Alternative for breakpoint() if needed
import sys; sys.breakpointhook = pdb.set_trace 

def calculate_potion_strength(base_ingredient_power,
                              magical_aura_modifier, dilution_factor):
    # breakpoint() # Python 3.7+ way to set a breakpoint  

    # Potential bug line
    intermediate_strength = base_ingredient_power + magical_aura_modifier 
    final_strength = intermediate_strength * dilution_factor

    return final_strength

print("--- Debugging Potion Strength ---")
strength1 = calculate_potion_strength(base_ingredient_power=10,
                                      magical_aura_modifier=5, 
                                      dilution_factor=2.0)
print(f"Potion Strength 1: {strength1}") 
# Expected: 30.0 (10+5)*2.0. If bug, 30.0. Corrected: 10*5*2.0 = 100.0


strength2 = calculate_potion_strength(base_ingredient_power=20,
                                      magical_aura_modifier=10, 
                                      dilution_factor=0.5)
print(f"Potion Strength 2: {strength2}") 
# Expected: 15.0 (20+10)*0.5. If bug, 15.0. Corrected: 20*10*0.5 = 100.0
