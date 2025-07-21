def transmute_lead_to_gold(lead_quantity):
    """
    Transmutes lead into gold.
    Returns the quantity of gold produced.
    """
    if lead_quantity <= 0:
        print("No lead to transmute!")
        return 0 # Return 0 gold if no lead

    gold_produced = lead_quantity * 0.5 # 0.5 units of gold per unit of lead
    print(f"Transmuting {lead_quantity} units of lead...")
    print(f"Successfully produced {gold_produced} units of gold!")
    return gold_produced # The function sends this value back
    # Any code after return in the function will NOT execute

# Casting the spell and capturing the result
print("--- First Transmutation Attempt ---")
my_gold = transmute_lead_to_gold(10) # The returned value (5.0) is stored in my_gold
print(f"I now have {my_gold} units of gold.")

print("\n--- Second Transmutation Attempt ---")
another_gold_batch = transmute_lead_to_gold(0)
print(f"I received {another_gold_batch} units of gold from the second attempt.")
