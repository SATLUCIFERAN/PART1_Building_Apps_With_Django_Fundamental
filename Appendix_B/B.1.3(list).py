

# Non-Pythonic: Building a list with a traditional loop
raw_power_readings = [50, 92, 30, 85, 60]
high_power_artifacts = []
for power in raw_power_readings:
    if power >= 70:
        high_power_artifacts.append(power)
print(f"High Power Artifacts (Non-Pythonic): {high_power_artifacts}")


# High Power Artifacts (Non-Pythonic): [92, 85]


# Pythonic: List comprehension for filtering
raw_power_readings = [50, 92, 30, 85, 60]
high_power_artifacts_py = [power for power in raw_power_readings if power >= 70]
print(f"High Power Artifacts (Pythonic): {high_power_artifacts_py}")


# High Power Artifacts (Pythonic): [92, 85]



