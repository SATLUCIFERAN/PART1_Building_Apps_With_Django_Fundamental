
ancient_curse_active = False
should_proceed = not ancient_curse_active
print(f"Should proceed? {should_proceed}") 

# Output: Should proceed? True

# What if the curse IS active?
ancient_curse_active_now = True
should_proceed_now = not ancient_curse_active_now
print(f"Should proceed (curse active)? {should_proceed_now}") 

# Output: Should proceed (curse active)? False
