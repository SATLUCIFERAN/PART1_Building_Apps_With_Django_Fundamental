
print("--- Writing Prophecy with Enchanted Doorway ---")
with open("prophecy_scroll.txt", "w") as scroll:
    scroll.write("The stars shall align, and new magic will awaken.\n")
    scroll.write("Seek the ancient texts in the Whispering Caves.\n")
    # No need to call scroll.close() here, 'with' handles it!
print("Prophecy written and scroll safely closed.")

'''
--- Writing Prophecy with Enchanted Doorway ---
Prophecy written and scroll safely closed.

'''


print("\n--- Reading Prophecy with Enchanted Doorway ---")
try:
    with open("prophecy_scroll.txt", "r") as scroll:
        content = scroll.read() # Read the entire content
        print("Content of Prophecy:")
        print(content)
    print("Prophecy read and scroll safely closed.")
except FileNotFoundError:
    print("Error: Prophecy scroll vanished!")

'''
--- Reading Prophecy with Enchanted Doorway ---
Content of Prophecy:
The stars shall align, and new magic will awaken.
Seek the ancient texts in the Whispering Caves.

Prophecy read and scroll safely closed.

'''