
# Create a multi-line prophecy file
prophecy_content = """
The ancient prophecy speaks:
  A hero shall rise from the ashes,
  Bearing the mark of the Dragon.
  Only then shall the darkness recede,
  And the true light return.
  Beware the whispers of the forgotten king.
"""

with open("ancient_prophecy.txt", "w") as f:
    f.write(prophecy_content)

print("--- Deciphering Ancient Prophecy ---")
key_phrases = []
with open("ancient_prophecy.txt", "r") as prophecy_scroll:
    for line_num, line in enumerate(prophecy_scroll):
        # Remove leading/trailing whitespace and newlines
        cleaned_line = line.strip() 

        if not cleaned_line: # Skip empty lines
            continue

        print(f"  Deciphering Line {line_num + 1}: '{cleaned_line}'")

        # Extract key phrases (e.g., lines containing "hero",
        # "dragon", "darkness", "light")
        if "hero" in cleaned_line.lower() or \
           "dragon" in cleaned_line.lower() or \
           "darkness" in cleaned_line.lower() or \
           "light" in cleaned_line.lower():
            key_phrases.append(cleaned_line)

print("\n--- Key Prophetic Phrases Extracted ---")
for phrase in key_phrases:
    print(f"- {phrase}")

print("\nProphecy deciphering complete.")
