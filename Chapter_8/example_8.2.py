
# (Using 'ancient_wisdom.txt' from previous example)

print("\n--- Reading Ancient Wisdom Scroll Line by Line (using .readline()) ---")
with open("ancient_wisdom.txt", "r") as scroll:
    line1 = scroll.readline()
    line2 = scroll.readline()
    line3 = scroll.readline()

    # .strip() removes leading/trailing whitespace, including '\n'
    print(f"Line 1: {line1.strip()}") 
    print(f"Line 2: {line2.strip()}")
    print(f"Line 3: {line3.strip()}")

'''
--- Reading Ancient Wisdom Scroll Line by Line (using .readline()) ---
Line 1: Chapter 1: The First Incantation.
Line 2: Chapter 2: The Art of Transmutation.
Line 3: Chapter 3: Summoning Lesser Elementals.

'''

print("\n--- Reading Ancient Wisdom Scroll Line by Line (Pythonic Iteration) ---")
with open("ancient_wisdom.txt", "r") as scroll:
    # enumerate gives index and item
    for line_num, line in enumerate(scroll): 
        print(f"Line {line_num + 1}: {line.strip()}")

'''
--- Reading Ancient Wisdom Scroll Line by Line (Pythonic Iteration) ---
Line 1: Chapter 1: The First Incantation.
Line 2: Chapter 2: The Art of Transmutation.
Line 3: Chapter 3: Summoning Lesser Elementals.

'''