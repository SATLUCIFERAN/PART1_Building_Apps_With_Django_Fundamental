
import datetime

prophet_name = "Mystic Seraphina"
celestial_alignment_score = 8.75 # Out of 10
ancient_artifact_count = 12
current_year = datetime.datetime.now().year

# Generate a prophecy using f-strings
prophecy = f"""
--- A Prophecy from the {prophet_name} ---
Behold! In the year {current_year}, the celestial alignment score stands 
at {celestial_alignment_score:.1f}. 
A new era approaches, marked by the awakening 
of {ancient_artifact_count} ancient artifacts.
The very fabric of reality will shift 
by {celestial_alignment_score * ancient_artifact_count / 100:.3f} percent!
Beware the shadows, for they lengthen when the alignment is below 5.0.
"""

print(prophecy)

# Further manipulation: Check for specific keywords in the prophecy
if "shadows" in prophecy.lower():
    print("\nWarning: Prophecy mentions shadows. Vigilance is advised.")

# Extract the percentage shift
shift_start = prophecy.find("shift by ") + len("shift by ")
shift_end = prophecy.find(" percent!")
shift_value_str = prophecy[shift_start:shift_end]
print(f"Extracted Shift Value: {shift_value_str}")