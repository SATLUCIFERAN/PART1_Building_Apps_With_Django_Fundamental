
def cast_blessing(target, strength="minor", duration_hours=1):
    """Casts a blessing spell with customizable strength and duration."""
    print(f"Casting a {strength} blessing on {target} for {duration_hours} hour(s).")

# Casting with default values
cast_blessing("Villager John")
# Output: Casting a minor blessing on Villager John for 1 hour(s).

# Casting with custom strength, default duration
cast_blessing("Brave Knight", strength="major")
# Output: Casting a major blessing on Brave Knight for 1 hour(s).

# Casting with custom duration, default strength
cast_blessing("Ancient Tree", duration_hours=24)
# Output: Casting a minor blessing on Ancient Tree for 24 hour(s).

# Casting with all custom values
cast_blessing("Elder Dragon", strength="legendary", duration_hours=72)
# Output: Casting a legendary blessing on Elder Dragon for 72 hour(s).
