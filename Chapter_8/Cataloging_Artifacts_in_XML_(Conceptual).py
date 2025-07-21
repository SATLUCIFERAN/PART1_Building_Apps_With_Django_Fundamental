
import xml.etree.ElementTree as ET
# Import minidom for pretty printing
from xml.dom import minidom 

# Creating an XML structure
root = ET.Element("MagicalArtifact")
name = ET.SubElement(root, "Name")
name.text = "Staff of Whispers"
type_elem = ET.SubElement(root, "Type")
type_elem.text = "Conjuration"
power = ET.SubElement(root, "PowerLevel")
power.text = "95"
enchantments = ET.SubElement(root, "Enchantments")

ET.SubElement(enchantments, "Enchantment").text = "Whispering Guidance"
ET.SubElement(enchantments, "Enchantment").text = "Spirit Communication"
origin = ET.SubElement(root, "Origin")
ET.SubElement(origin, "Realm").text = "Shadowfell"
ET.SubElement(origin, "Era").text = "Forgotten"

# Convert to XML string (without pretty_print, 
# as it's not a valid argument for ET.tostring)
xml_string_raw = ET.tostring(root, encoding='unicode')

# Use minidom for pretty printing the XML string for display and saving
xml_pretty_string = minidom.parseString(xml_string_raw).toprettyxml(indent="  ")


# print("--- Converting Python Data to XML ---")
# print(xml_pretty_string)

'''
<?xml version="1.0" ?>
<MagicalArtifact>
  <Name>Staff of Whispers</Name>
  <Type>Conjuration</Type>
  <PowerLevel>95</PowerLevel>
  <Enchantments>
    <Enchantment>Whispering Guidance</Enchantment>
    <Enchantment>Spirit Communication</Enchantment>
  </Enchantments>
  <Origin>
    <Realm>Shadowfell</Realm>
    <Era>Forgotten</Era>
  </Origin>
</MagicalArtifact>

'''

# Save to file
with open("staff_of_whispers.xml", "w") as xml_file:
    xml_file.write(xml_pretty_string) # Write the pretty-printed version
print("\nArtifact data saved to 'staff_of_whispers.xml'")

print("\n--- Reading XML from File and Parsing ---")
# Parse XML from file
tree = ET.parse("staff_of_whispers.xml")
root_loaded = tree.getroot()

# Accessing data
loaded_name = root_loaded.find("Name").text
loaded_power = root_loaded.find("PowerLevel").text
loaded_enchantments = [e.text for e in root_loaded.findall("Enchantments/Enchantment")]

print(f"Loaded Artifact Name: {loaded_name}")
print(f"Loaded Artifact Power: {loaded_power}")
print(f"Loaded Artifact Enchantments: {loaded_enchantments}")

'''
Loaded Artifact Name: Staff of Whispers
Loaded Artifact Power: 95
Loaded Artifact Enchantments: ['Whispering Guidance', 'Spirit Communication']

'''