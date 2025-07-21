
def cast_elemental_blast(element, power_level):
    print(f"Unleashing a {power_level}-power {element} blast!")

# Arguments are matched by position: 'Fire' goes to 'element', 80 goes to 'power_level'
cast_elemental_blast("Fire", 80)
# Output: Unleashing a 80-power Fire blast!

# Incorrect order would lead to logical errors or TypeErrors
cast_elemental_blast(80, "Fire") # This would try to treat 80 as element and 'Fire' as power_level
# Output: Unleashing a Fire-power 80 blast!