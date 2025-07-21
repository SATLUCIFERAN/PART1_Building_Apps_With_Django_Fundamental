
moonstone_glows = True
sunstone_hums = True
portal_active = moonstone_glows and sunstone_hums
print(f"Is the Portal active? {portal_active}") 

# Output: Is the Portal active? True

# What if one fails?
sunstone_hums_broken = False
portal_active_broken = moonstone_glows and sunstone_hums_broken
print(f"Is the Portal active (broken sunstone)? {portal_active_broken}") 

# Output: Is the Portal active (broken sunstone)? False
