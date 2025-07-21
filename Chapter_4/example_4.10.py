
# Imagine 'ancient_scroll.txt' contains:
# "The first star falls."
# "The second moon rises."

# First, let's create a dummy file for this example
with open("ancient_scroll.txt", "w") as f:
    f.write("The first star falls.\n")
    f.write("The second moon rises.\n")

print("--- Reading Ancient Scroll (Safely) ---")
try:
    with open("ancient_scroll.txt", "r") as scroll: # 'scroll' is the file object
        for line_num, line in enumerate(scroll):
            print(f"  Line {line_num + 1}: {line.strip()}")
       
    print("Scroll reading complete. Door closed.")
except FileNotFoundError:
    print("Error: Ancient scroll not found!")


