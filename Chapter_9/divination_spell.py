# # Example_9.1.py: Reading the Alchemist's Library HTML
# # This spell sends a messenger raven to retrieve the content of our local HTML scroll.

# # Import the 'os' module to help with path manipulation.
# # This makes our code work correctly whether you're on Windows, macOS, or Linux.
# import os

# # Define the path to our local HTML scroll.
# # We use os.path.join to safely combine folder names into a correct path for your operating system.
# # IMPORTANT: The HTML file is now located inside the 'web-alchemist-lab' subfolder.
# html_file_path = os.path.join("web-alchemist-lab", "alchemist_library.html")

# # The 'try...except' block is our Graceful Recovery protocol (Chapter 7).
# # It ensures our spell doesn't completely fail if the file isn't found or another disruption occurs.
# try:
#     # 'with open(...) as file:' is the safest way to open files (Chapter 8).
#     # 'r' means we are opening the file in 'read' mode.
#     # 'encoding="utf-8"' is crucial for web content, ensuring all characters (even magical symbols!) are read correctly.
#     with open(html_file_path, "r", encoding="utf-8") as file:
#         # 'file.read()' reads the entire content of the HTML file and stores it as a single, large string
#         # in our 'html_content' variable.
#         html_content = file.read()

#     # If we reach here, the file was read successfully!
#     print("Messenger Raven reports: HTML scroll successfully retrieved!")
#     print("\n--- A Glimpse into the Raw Scroll (First 500 characters) ---")
#     # We'll print only the first 500 characters to give us a quick peek without flooding the terminal.
#     # This is an example of string slicing, a powerful technique for manipulating text (Chapter 3).
#     print(html_content[:500])
#     print("\n-------------------------------------------------------------")

# except FileNotFoundError:
#     # If Python can't find the file at the specified path, this error is 'caught'.
#     print(f"Error: The scroll '{html_file_path}' was not found.")
#     print("Please ensure 'alchemist_library.html' is inside the 'web-alchemist-lab' subfolder within your 'Chapter_9' directory.")
# except Exception as e:
#     # This 'catch-all' exception handles any other unexpected disruptions during the reading process.
#     print(f"An unexpected disruption occurred while retrieving the scroll: {e}")




# '''

#     Messenger Raven reports: HTML scroll successfully retrieved!

# --- A Glimpse into the Raw Scroll (First 500 characters) ---

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>The Grand Alchemist's Library</title>
#     <style>
#         body { font-family: 'Times New Roman', serif; line-height: 1.6;
#                color: #333; max-width: 800px; margin: 20px auto; 
#                padding: 0 15px; background: #fdf5e6; }
#         h1, h2, h3 { color: #5a2d00; }
#         .section-title { border-bottom: 2px solid #5a2d00;
#                padding-bottom: 5px; margin-top: 30p

# '''







###################### Chapter 9 topic 9.3 The Pattern Seeker's Quill: Parsing HTML with Beautiful Soup ###########

# # Example_9.2.py: Parsing the Alchemist's Library HTML with Beautiful Soup
# # This spell uses the Pattern Seeker's Quill (Beautiful Soup) to navigate and extract data.

# from bs4 import BeautifulSoup # Import the Beautiful Soup library
# import os # Import os module for path manipulation

# # Define the path to our local HTML scroll.
# # Ensure 'alchemist_library.html' is inside the 'web-alchemist-lab' subfolder.
# html_file_path = os.path.join("web-alchemist-lab", "alchemist_library.html")

# try:
#     with open(html_file_path, "r", encoding="utf-8") as file:
#         html_content = file.read()

#     # Step 1: Create a Beautiful Soup object.
#     # This transforms the raw HTML string into a navigable Python object.
#     # 'html.parser' is the standard parser Beautiful Soup uses to understand the HTML structure.
#     soup = BeautifulSoup(html_content, 'html.parser')

#     print("--- Divining Secrets from the Library ---")

#     # Alchemical Challenge 1: Extract the Library's Grand Title
#     # The <title> tag in HTML contains the page's title. Beautiful Soup makes it easy to access.
#     # 'soup.title' finds the <title> tag, and '.text' retrieves its visible text content.
#     library_title = soup.title.text
#     print(f"\nLibrary Title: {library_title}")

#     # Alchemical Challenge 2: Find all Ancient Artifacts and their details
#     # Artifacts are enclosed in <div class="artifact"> tags.
#     # .find_all() is a powerful method to find all occurrences of a tag that match specific criteria.
#     # Here, we're looking for all 'div' tags that have a 'class' attribute equal to 'artifact'.
#     # We use 'class_=' because 'class' is a reserved keyword in Python.
#     artifacts = soup.find_all('div', class_='artifact')

#     print(f"\nFound {len(artifacts)} Ancient Artifacts:")
#     for i, artifact_div in enumerate(artifacts):
#         # Within each 'artifact_div', we can now search for its specific elements.

#         # The artifact's name is inside an <h3> tag.
#         # .find('h3') finds the first <h3> tag within this artifact_div.
#         # .text.strip() retrieves its text content and removes any extra spaces.
#         name = artifact_div.find('h3').text.strip()

#         # The type and power level are within <p> tags, with a <span> for the attribute name.
#         # We use .find() to locate the <span> with a specific class and text.
#         # .next_sibling gets the element immediately following the span (which is our value).
#         artifact_type_span = artifact_div.find('span', class_='attribute', string='Type:')
#         artifact_type = artifact_type_span.next_sibling.strip() if artifact_type_span else "N/A"

#         power_level_span = artifact_div.find('span', class_='attribute', string='Power Level:')
#         power_level = power_level_span.next_sibling.strip() if power_level_span else "N/A"

#         # The description is a <p> tag that is a direct child of the artifact div,
#         # but it doesn't have the 'attribute' span inside it.
#         # .select_one() allows us to use CSS selectors (like those used in styling web pages).
#         # 'p:not(:has(span.attribute))' means: find a <p> tag that *does not* have a child <span> with class 'attribute'.
#         description_paragraph = artifact_div.select_one('p:not(:has(span.attribute))')
#         description = description_paragraph.text.strip() if description_paragraph else "No description"

#         # Extract tags (e.g., Rare, Defense, Charm)
#         # These are <span> tags with class 'tag' within a <div class="tags">.
#         tags_div = artifact_div.find('div', class_='tags')
#         # We use a list comprehension to get the text from all found tag spans.
#         tags = [tag.text.strip() for tag in tags_div.find_all('span', class_='tag')] if tags_div else []

#         print(f"  Artifact {i+1}:")
#         print(f"    Name: {name}")
#         print(f"    Type: {artifact_type}")
#         print(f"    Power Level: {power_level}")
#         print(f"    Description: {description}")
#         print(f"    Tags: {', '.join(tags)}")
        
#         # Alchemical Challenge 2.1 (Bonus): Extract the 'View Full Lore' link URL
#         # .find('a') finds the first anchor (link) tag.
#         # We access attributes of a tag (like 'href') using dictionary-like syntax: tag['attribute_name'].
#         lore_link_tag = artifact_div.find('a')
#         lore_url = lore_link_tag['href'] if lore_link_tag and 'href' in lore_link_tag.attrs else "No Lore Link"
#         print(f"    Lore Link: {lore_url}")
#         print("-" * 30) # Separator for clarity

#     # Alchemical Challenge 3: Extract all Potent Spells and their effects
#     spells = soup.find_all('div', class_='spell')
#     print(f"\nFound {len(spells)} Potent Spells:")
#     for i, spell_div in enumerate(spells):
#         spell_name = spell_div.find('h3').text.strip()
#         mana_cost_span = spell_div.find('span', class_='attribute', string='Mana Cost:')
#         mana_cost = mana_cost_span.next_sibling.strip() if mana_cost_span else "N/A"
#         effect_span = spell_div.find('span', class_='attribute', string='Effect:')
#         effect = effect_span.next_sibling.strip() if effect_span else "N/A"

#         print(f"  Spell {i+1}:")
#         print(f"    Name: {spell_name}")
#         print(f"    Mana Cost: {mana_cost}")
#         print(f"    Effect: {effect}")

#         # Extract list items for spell details (e.g., 'Requires Fire Affinity')
#         spell_details_list = spell_div.find('ul')
#         if spell_details_list:
#             details = [li.text.strip() for li in spell_details_list.find_all('li')]
#             print(f"    Details: {'; '.join(details)}")
#         else:
#             print("    Details: No specific details found.")
        
#         # Extract spell tags
#         spell_tags_div = spell_div.find('div', class_='tags')
#         spell_tags = [tag.text.strip() for tag in spell_tags_div.find_all('span', class_='tag')] if spell_tags_div else []
#         print(f"    Tags: {', '.join(spell_tags)}")
#         print("-" * 30)

#     # Alchemical Challenge 4: Extract Mythical Creatures
#     creatures = soup.find_all('div', class_='creature')
#     print(f"\nFound {len(creatures)} Mythical Creatures:")
#     for i, creature_div in enumerate(creatures):
#         creature_name = creature_div.find('h3').text.strip()
#         habitat_span = creature_div.find('span', class_='attribute', string='Habitat:')
#         habitat = habitat_span.next_sibling.strip() if habitat_span else "N/A"
#         temperament_span = creature_div.find('span', class_='attribute', string='Temperament:')
#         temperament = temperament_span.next_sibling.strip() if temperament_span else "N/A"
        
#         # The description is a <p> tag that is a direct child of the creature div,
#         # but it doesn't have the 'attribute' span inside it.
#         description_creature = creature_div.select_one('p:not(:has(span.attribute))')
#         description_creature_text = description_creature.text.strip() if description_creature else "No description"

#         print(f"  Creature {i+1}:")
#         print(f"    Name: {creature_name}")
#         print(f"    Habitat: {habitat}")
#         print(f"    Temperament: {temperament}")
#         print(f"    Description: {description_creature_text}")
#         print("-" * 30)

#     # Alchemical Challenge 5: Find all unique tags across all items in the library
#     # We use a set to automatically collect unique values, preventing duplicates.
#     all_unique_tags = set()
#     for tag_element in soup.find_all('span', class_='tag'):
#         all_unique_tags.add(tag_element.text.strip())
#     print(f"\nUnique Magical Tags Found Across Library: {', '.join(sorted(list(all_unique_tags)))}")

#     # Alchemical Challenge 6: Extract contact email from the footer
#     # We find the footer div, then the 'a' (anchor/link) tag within it that has an 'href' attribute.
#     footer_div = soup.find('div', class_='footer')
#     contact_link_tag = footer_div.find('a', href=True)
    
#     contact_email = contact_link_tag.text.strip() if contact_link_tag else "Archivist contact not found."
#     print(f"\nArchivist Contact: {contact_email}")


# except FileNotFoundError:
#     print(f"Error: The scroll '{html_file_path}' was not found.")
#     print("Please ensure 'alchemist_library.html' is inside the 'web-alchemist-lab' subfolder within your 'Chapter_9' directory.")
# except Exception as e:
#     print(f"An unexpected disruption occurred during divination: {e}")
#     import traceback; traceback.print_exc() # This line is helpful for debugging to see the full error.






###################### Chapter 9 topic 9.4 The Alchemist's Ledger: Storing Divined Data ####################




from bs4 import BeautifulSoup # Still need Beautiful Soup for parsing
import os # Still need os for path manipulation
import json # NEW! Import the json module for working with JSON data


html_file_path = os.path.join("web-alchemist-lab", "alchemist_library.html")
output_json_file = os.path.join("web-alchemist-lab", "divined_library_ledger.json")
extracted_artifacts_data = []
extracted_spells_data = []
extracted_creatures_data = []
all_unique_tags = set() 

try:
    # Read the HTML content from our local scroll
    with open(html_file_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    # Create the Beautiful Soup object to parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    print("--- Divining Secrets for the Alchemist's Ledger ---")

    # --- Extracting Artifacts ---
    artifacts = soup.find_all('div', class_='artifact')
    for artifact_div in artifacts:
        name = artifact_div.find('h3').text.strip()
        artifact_type_span = artifact_div.find('span', class_='attribute', string='Type:')
        artifact_type = artifact_type_span.next_sibling.strip() if artifact_type_span else "N/A"
        power_level_span = artifact_div.find('span', class_='attribute', string='Power Level:')
        # Convert power_level to an integer for better data handling (Chapter 1: Data Types).
        power_level = int(power_level_span.next_sibling.strip()) if power_level_span\
                      and power_level_span.next_sibling.strip().isdigit() else 0
        description_paragraph = artifact_div.select_one('p:not(:has(span.attribute))')
        description = description_paragraph.text.strip() if description_paragraph\
                                                         else "No description"
        tags_div = artifact_div.find('div', class_='tags')
        tags = [tag.text.strip() for tag in tags_div.find_all('span', class_='tag')] if tags_div else []
        
        # Add all tags from this artifact to our overall unique tags set
        for tag in tags:
            all_unique_tags.add(tag)
       
        artifact_data = {
            "name": name,
            "type": artifact_type,
            "power_level": power_level,
            "description": description,
            "tags": tags # Store tags as a list
        }
        extracted_artifacts_data.append(artifact_data) # Add the dictionary to our list

    print(f"Divined {len(extracted_artifacts_data)} Ancient Artifacts.")

    # --- Extracting Spells ---
    spells = soup.find_all('div', class_='spell')
    for spell_div in spells:
        spell_name = spell_div.find('h3').text.strip()
        mana_cost_span = spell_div.find('span', class_='attribute', string='Mana Cost:')
        mana_cost = int(mana_cost_span.next_sibling.strip()) if mana_cost_span and mana_cost_span.next_sibling.strip().isdigit() else 0
        effect_span = spell_div.find('span', class_='attribute', string='Effect:')
        effect = effect_span.next_sibling.strip() if effect_span else "N/A"
        
        spell_details_list = spell_div.find('ul')
        details = [li.text.strip() for li in spell_details_list.find_all('li')] if spell_details_list else []
        
        spell_tags_div = spell_div.find('div', class_='tags')
        spell_tags = [tag.text.strip() for tag in spell_tags_div.find_all('span', class_='tag')] if spell_tags_div else []

        # Add all tags from this spell to our overall unique tags set
        for tag in spell_tags:
            all_unique_tags.add(tag)

        spell_data = {
            "name": spell_name,
            "mana_cost": mana_cost,
            "effect": effect,
            "details": details, # Store details as a list
            "tags": spell_tags
        }
        extracted_spells_data.append(spell_data)

    print(f"Divined {len(extracted_spells_data)} Potent Spells.")

    # --- Extracting Creatures ---
    creatures = soup.find_all('div', class_='creature')
    for creature_div in creatures:
        creature_name = creature_div.find('h3').text.strip()
        habitat_span = creature_div.find('span', class_='attribute', string='Habitat:')
        habitat = habitat_span.next_sibling.strip() if habitat_span else "N/A"
        temperament_span = creature_div.find('span', class_='attribute', string='Temperament:')
        temperament = temperament_span.next_sibling.strip() if temperament_span else "N/A"
        description_creature = creature_div.select_one('p:not(:has(span.attribute))')
        description_creature_text = description_creature.text.strip() if description_creature else "No description"

        creature_data = {
            "name": creature_name,
            "habitat": habitat,
            "temperament": temperament,
            "description": description_creature_text
        }
        extracted_creatures_data.append(creature_data)

    print(f"Divined {len(extracted_creatures_data)} Mythical Creatures.")
    print(f"Total Unique Magical Tags Divined: {len(all_unique_tags)}.")

    # --- Consolidate all data into one grand ledger ---
    # This creates a single dictionary where keys are categories and values are lists of items.
    grand_ledger = {
        "library_title": soup.title.text.strip(),
        "ancient_artifacts": extracted_artifacts_data,
        "potent_spells": extracted_spells_data,
        "mythical_creatures": extracted_creatures_data,
        "unique_tags": sorted(list(all_unique_tags)), # Convert set to list and sort for consistent output
        "archivist_contact": soup.find('div', class_='footer').find('a', href=True).text.strip()
    }

    # Step 2: Save the extracted data to a JSON file (our Alchemist's Ledger)
    # 'w' means write mode. If the file exists, it will be overwritten.
    # 'encoding="utf-8"' ensures correct character storage.
    
    with open(output_json_file, "w", encoding="utf-8") as json_file:
        # json.dump() writes the Python data structure (grand_ledger) directly to the file.
        # 'indent=4' makes the JSON output beautifully human-readable with 4-space indentation.
        # 'ensure_ascii=False' allows non-ASCII characters (like special symbols if any) to be written directly.
        
        
        json.dump(grand_ledger, json_file, indent=4, ensure_ascii=False)


    print(f"\nSuccessfully compiled the Alchemist's Ledger: '{output_json_file}'!")
    print("Open this file in VS Code to behold your divined knowledge!")

except FileNotFoundError:
    print(f"Error: The scroll '{html_file_path}' was not found.")
    print("Please ensure 'alchemist_library.html' is inside the 'web-alchemist-lab' subfolder within your 'Chapter_9' directory.")
except Exception as e:
    print(f"An unexpected disruption occurred during data storage: {e}")
    import traceback; traceback.print_exc() # This line is helpful for debugging to see the full error.



'''
--- Divining Secrets for the Alchemist's Ledger ---
Divined 3 Ancient Artifacts.
Divined 2 Potent Spells.
Divined 2 Mythical Creatures.
Total Unique Magical Tags Divined: 15.

Successfully compiled the Alchemist's Ledger: 
             'web-alchemist-lab\divined_library_ledger.json'!
Open this file in VS Code to behold your divined knowledge!

'''




