

potion_queue = ["Healing Potion", "Invisibility Brew", "Strength Elixir"]
print(f"Initial Potion Queue: {potion_queue}")

# Day 1: New urgent order arrives for a specific spot
potion_queue.insert(1, "Mana Restorative (Urgent)")
print(f"After urgent order: {potion_queue}")

# Day 2: Alchemist finishes the first potion
finished_potion = potion_queue.pop(0)
print(f"Finished brewing: {finished_potion}")
print(f"Queue after brewing: {potion_queue}")

# Day 3: A new, less urgent potion is added
potion_queue.append("Sleep Draught")
print(f"Queue after new order: {potion_queue}")

# Day 4: Check if a specific potion is still in queue and prioritize it
if "Strength Elixir" in potion_queue:
    print("\nStrength Elixir still in queue! Moving to front for immediate brewing.")
    strength_index = potion_queue.index("Strength Elixir")
    strength_elixir = potion_queue.pop(strength_index)
    potion_queue.insert(0, strength_elixir)
print(f"Queue after prioritizing Strength Elixir: {potion_queue}")

# Day 5: Sort the remaining queue alphabetically for easier management
print("\nSorting remaining potions alphabetically for next week's schedule...")
potion_queue.sort()
print(f"Sorted Queue: {potion_queue}")

print(f"\nTotal potions remaining in queue: {len(potion_queue)}")
