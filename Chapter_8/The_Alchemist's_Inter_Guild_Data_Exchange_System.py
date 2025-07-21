
import json
import xml.etree.ElementTree as ET
from xml.dom import minidom # Import minidom for pretty printing

# --- Data to be exchanged (Python dictionary) ---
quest_data = {
    "quest_id": "QST-001",
    "title": "The Whispering Caves Expedition",
    "description": "Investigate strange hums from the Whispering Caves. Recover any ancient texts.",
    "reward_gold": 500,
    "difficulty": "Medium",
    "objectives": [
        {"name": "Reach Cave Entrance", "status": "completed"},
        {"name": "Locate Ancient Texts", "status": "pending"},
        {"name": "Return to Guild", "status": "pending"}
    ],
    "assigned_to": "Elara"
}

# --- Function to convert Python dict to JSON and save ---
def export_quest_to_json(data: dict, filename: str):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Quest exported to {filename} (JSON).")

# --- Function to convert Python dict to XML and save ---
def export_quest_to_xml(data: dict, filename: str):
    root = ET.Element("Quest")
    for key, value in data.items():
        if isinstance(value, dict):
            sub_elem = ET.SubElement(root, key.capitalize())
            for sub_key, sub_value in value.items():
                ET.SubElement(sub_elem, sub_key.capitalize()).text = str(sub_value)
        elif isinstance(value, list):
            list_elem = ET.SubElement(root, key.capitalize())
            for item in value:
                if isinstance(item, dict):
                    # Use name as tag, replace spaces for valid XML tag names
                    item_elem = ET.SubElement(list_elem, item.get("name", "Item").replace(" ", ""))
                    for item_key, item_val in item.items():
                        ET.SubElement(item_elem, item_key.capitalize()).text = str(item_val)
                else:
                    ET.SubElement(list_elem, "Item").text = str(item)
        else:
            ET.SubElement(root, key.capitalize()).text = str(value)

    # Convert ElementTree to a raw XML string first
    xml_string_raw = ET.tostring(root, encoding='utf-8', xml_declaration=True)

    # Use minidom to pretty print the XML string
    # .toprettyxml() expects bytes if xml_declaration=True was used, so decode first
    xml_pretty_string = minidom.parseString(xml_string_raw.decode('utf-8')).toprettyxml(indent="  ", encoding='utf-8')

    # Write the pretty-printed string to the file
    with open(filename, "wb") as f: # Open in binary write mode ('wb') for bytes from toprettyxml
        f.write(xml_pretty_string)
    print(f"Quest exported to {filename} (XML).")

# --- Function to load JSON and convert to Python dict ---
def import_quest_from_json(filename: str) -> dict:
    with open(filename, "r") as f:
        data = json.load(f)
    print(f"Quest imported from {filename} (JSON).")
    return data

# --- Function to load XML and convert to Python dict (simplified for this example) ---
def import_quest_from_xml(filename: str) -> dict:
    tree = ET.parse(filename)
    root = tree.getroot()
    imported_data = {}
    for elem in root:
        if elem.text and not elem.findall('*'): # If it's a simple element with text
            imported_data[elem.tag.lower()] = elem.text
        elif elem.findall('*'): # If it has children (nested structure)
            if elem.tag.lower() == "objectives": # Special handling for objectives list
                objectives_list = []
                for obj_elem in elem:
                    objective_dict = {}
                    for sub_elem in obj_elem:
                        objective_dict[sub_elem.tag.lower()] = sub_elem.text
                    objectives_list.append(objective_dict)
                imported_data[elem.tag.lower()] = objectives_list
            else: # Generic nested dict
                nested_dict = {}
                for sub_elem in elem:
                    nested_dict[sub_elem.tag.lower()] = sub_elem.text
                imported_data[elem.tag.lower()] = nested_dict
    print(f"Quest imported from {filename} (XML).")
    return imported_data

# --- Execute the data exchange ---
print("--- Alchemist's Inter-Guild Data Exchange ---")

# Export as JSON for one guild
export_quest_to_json(quest_data, "quest_data.json")

# Export as XML for another guild
export_quest_to_xml(quest_data, "quest_data.xml")

# Import from JSON
loaded_json_quest = import_quest_from_json("quest_data.json")
print(f"JSON Quest Title: {loaded_json_quest['title']}")

# Import from XML
loaded_xml_quest = import_quest_from_xml("quest_data.xml")
print(f"XML Quest Title: {loaded_xml_quest['title']}")
print(f"XML Quest Objectives: {loaded_xml_quest['objectives']}") # Note: XML parsing to dict can be complex for lists
