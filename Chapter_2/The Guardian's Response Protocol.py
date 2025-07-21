
current_time_hour = 22 # 0-23
intruder_type = "shadow_creature" # "human", "beast", "shadow_creature"
guardian_charge_level = 75 # 0-100

print("--- Guardian Protocol Activation ---")

if current_time_hour >= 22 or current_time_hour < 6: # Between 10 PM and 6 AM
    print("It is night. Guardian is on high alert.")
    if intruder_type == "shadow_creature":
        if guardian_charge_level >= 80:
            print("Guardian unleashes full 'Purging Light' spell!")
            action = "Purging Light"
        elif guardian_charge_level >= 50:
            print("Guardian casts 'Binding Chains' spell.")
            action = "Binding Chains"
        else:
            print("Guardian activates 'Stealth Mode' and alerts master.")
            action = "Stealth & Alert"
    elif intruder_type == "human":
        print("Guardian issues a warning projection: 'Halt, mortal!'")
        action = "Warning Projection"
    else: # intruder_type == "beast"
        print("Guardian emits a sonic deterrent.")
        action = "Sonic Deterrent"
elif current_time_hour >= 6 and current_time_hour < 18: # Between 6 AM and 6 PM
    print("It is day. Guardian is in passive observation mode.")
    if intruder_type == "human":
        print("Guardian offers guidance: 'Welcome, traveler. May I assist you?'")
        action = "Guidance"
    else:
        print("Guardian remains hidden, observing.")
        action = "Hidden Observation"
else: # Between 6 PM and 10 PM (Dusk/Dawn)
    print("It is twilight. Guardian is in watchful mode.")
    print("Guardian sends a subtle magical pulse.")
    action = "Subtle Pulse"

print(f"Guardian's Final Action: {action}")


'''
--- Guardian Protocol Activation ---
It is night. Guardian is on high alert.
Guardian casts 'Binding Chains' spell.
Guardian's Final Action: Binding Chains

'''