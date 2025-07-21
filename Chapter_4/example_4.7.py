
def brew_simple_potion():
    # 'potion_type' is a local variable to this function
    potion_type = "Minor Healing"
    print(f"Inside function: Brewing a {potion_type} potion.")
    # 'mana_cost' is also local
    mana_cost = 10
    print(f"Inside function: Cost is {mana_cost} mana.")

print("--- Initiating Brewing Process ---")
brew_simple_potion()
print("--- Brewing Process Complete ---")

# Attempting to access local variables outside the function will cause an error
# print(f"Outside function: Potion type was {potion_type}") # This line would cause a NameError!
# print(f"Outside function: Mana cost was {mana_cost}") # This line would cause a NameError!
