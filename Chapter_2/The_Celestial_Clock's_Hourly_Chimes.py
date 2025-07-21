
print("--- The Celestial Clock Begins Its Hourly Chimes ---")

for hour in range(24): # hour will go from 0 to 23
    chime_message = f"Hour {hour:02d}: The Celestial Clock chimes." 
    # :02d formats number to 2 digits, e.g., 01, 02

    if hour == 0: # Midnight
        chime_message += " A faint shimmer of starlight appears."
    elif hour == 6: # Dawn
        chime_message += " The first rays of dawn energize the air!"
    elif hour == 12: # Noon
        chime_message += " The sun's power peaks! A warm glow envelops the realm."
    elif hour == 18: # Dusk
        chime_message += " Shadows lengthen. Creatures of twilight awaken."
    elif hour % 3 == 0: # Every 3rd hour (e.g., 3, 9, 15, 21)
        chime_message += " A subtle magical pulse resonates."

    print(chime_message)
    
print("--- The Day's Cycle Concludes ---")