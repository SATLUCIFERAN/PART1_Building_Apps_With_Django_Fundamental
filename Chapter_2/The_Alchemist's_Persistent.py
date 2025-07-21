
import random
import time # To simulate time passing

rare_ingredient_found = False
search_attempts = 0
max_search_attempts = 10

print("--- Alchemist Begins Search for 'Glimmering Dewdrop' ---")

while not rare_ingredient_found and search_attempts < max_search_attempts:
    search_attempts += 1
    print(f"\nSearch attempt #{search_attempts}...")
    # Simulate the chance of finding the ingredient
    if random.randint(1, 3) == 1: # 1 in 3 chance
        rare_ingredient_found = True
        print("  *GASP!* A 'Glimmering Dewdrop' has been found!")
    else:
        print("  No 'Glimmering Dewdrop' here. Continuing search...")
        time.sleep(0.5) # Simulate a brief pause (0.5 seconds)

if rare_ingredient_found:
    print("\n--- Success! The rare ingredient is secured! ---")
else:
    print(f"\n--- Search concluded after {max_search_attempts}\
           attempts. 'Glimmering Dewdrop' remains elusive. ---")

'''
--- Alchemist Begins Search for 'Glimmering Dewdrop' ---

Search attempt #1...
  No 'Glimmering Dewdrop' here. Continuing search...

Search attempt #2...
  No 'Glimmering Dewdrop' here. Continuing search...

Search attempt #3...
  *GASP!* A 'Glimmering Dewdrop' has been found!

--- Success! The rare ingredient is secured! ---

'''