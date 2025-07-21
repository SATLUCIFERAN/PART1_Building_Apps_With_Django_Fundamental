
print("\n--- Reading All Lines into a List ---")
with open("ancient_wisdom.txt", "r") as scroll:
    all_chapters = scroll.readlines()
    print(f"Type of result: {type(all_chapters)}") # Output: <class 'list'>
    for chapter in all_chapters:
        print(f"  - {chapter.strip()}")


'''
--- Reading All Lines into a List ---
Type of result: <class 'list'>
  - Chapter 1: The First Incantation.
  - Chapter 2: The Art of Transmutation.
  - Chapter 3: Summoning Lesser Elementals.

'''