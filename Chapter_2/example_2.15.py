
has_master_key = False
knows_secret_password = True
can_enter_library = has_master_key or knows_secret_password
print(f"Can enter the library? {can_enter_library}") 

# Output: Can enter the library? True

# What if both fail?
has_master_key_lost = False
knows_secret_password_forgotten = False
can_enter_library_failed = has_master_key_lost or knows_secret_password_forgotten
print(f"Can enter the library (both failed)? {can_enter_library_failed}")
 
# Output: Can enter the library (both failed)? False