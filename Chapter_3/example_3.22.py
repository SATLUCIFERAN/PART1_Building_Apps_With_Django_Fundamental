
ancient_text = "  The Whispering Woods holds ancient secrets.  "
print(f"Original Text: '{ancient_text}'")

# Clean up whitespace and convert to uppercase
cleaned_upper = ancient_text.strip().upper()
print(f"Cleaned & Uppercase: '{cleaned_upper}'") 
# Output: Cleaned & Uppercase: 'THE WHISPERING WOODS HOLDS ANCIENT SECRETS.'

# Split into individual words
words = cleaned_upper.split(" ")
print(f"Words: {words}") 
# Output: Words: ['THE', 'WHISPERING', 'WOODS', 'HOLDS', 'ANCIENT', 'SECRETS.']

# Join words back with a different separator
new_phrase = "-".join(words)
print(f"Joined with hyphens: {new_phrase}") 
# Output: Joined with hyphens: THE-WHISPERING-WOODS-HOLDS-ANCIENT-SECRETS.

# Find a specific word
secret_index = ancient_text.find("secrets")
print(f"Index of 'secrets': {secret_index}") 
# Output: Index of 'secrets': 37

# Replace a word
new_text = ancient_text.replace("ancient", "forgotten").strip()
print(f"After replacing 'ancient': '{new_text}'") 
# Output: After replacing 'ancient': 'The Whispering Woods holds forgotten secrets.'
