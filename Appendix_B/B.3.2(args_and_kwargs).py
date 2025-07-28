
# Pythonic: Flexible spell casting
def cast_grand_ritual(ritual_name, *participants, **modifications):
    print(f"Initiating Grand Ritual: {ritual_name}")
    if participants:
        print(f"Participants: {', '.join(participants)}")
    if modifications:
        print("Magical Modifications:")
        for key, value in modifications.items():
            print(f"  - {key}: {value}")
    print("Ritual complete!\n")


print("--- Pythonic Flexible Rituals ---")


cast_grand_ritual("Summon Elemental", "Elara", "Kael", 
                  power_boost="Major", duration="Long")

'''
Initiating Grand Ritual: Summon Elemental
Participants: Elara, Kael
Magical Modifications:
  - power_boost: Major
  - duration: Long
Ritual complete!

'''


cast_grand_ritual("Ward of Silence", "Apprentice Leo")

'''
Initiating Grand Ritual: Ward of Silence
Participants: Apprentice Leo
Ritual complete!

'''


cast_grand_ritual("Cosmic Alignment", phase="Full Moon", 
                  alignment_type="Perfect")

'''
Initiating Grand Ritual: Cosmic Alignment
Magical Modifications:
  - phase: Full Moon
  - alignment_type: Perfect
Ritual complete!

'''
