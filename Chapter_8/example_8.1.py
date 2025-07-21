
# First, ensure the file exists with some content
with open("ancient_wisdom.txt", "w") as f:
    f.write("Chapter 1: The First Incantation.\n")
    f.write("Chapter 2: The Art of Transmutation.\n")
    f.write("Chapter 3: Summoning Lesser Elementals.\n")

print("--- Reading Entire Ancient Wisdom Scroll ---")
with open("ancient_wisdom.txt", "r") as scroll:
    full_wisdom = scroll.read()
    print(full_wisdom)


'''
--- Reading Entire Ancient Wisdom Scroll ---
Chapter 1: The First Incantation.
Chapter 2: The Art of Transmutation.
Chapter 3: Summoning Lesser Elementals.

'''