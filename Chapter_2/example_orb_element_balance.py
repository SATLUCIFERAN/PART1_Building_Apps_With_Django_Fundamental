
# Initial elemental energies in the Orb
fire_energy = 150
water_energy = 120
earth_energy = 90
air_energy = 180

# --- Phase 1: Daily Elemental Fluctuations ---
# Fire energy increases by 10%
fire_energy *= 1.10
# Water energy decreases by 5 units due to evaporation
water_energy -= 5
# Earth energy is half of the current water energy
earth_energy = water_energy // 2
# Air energy is the sum of fire and earth, but capped at 200
air_energy = (fire_energy + earth_energy) if (fire_energy + earth_energy) <= 200 else 200

print("--- Orb Energy After Fluctuations ---")
print(f"Fire: {fire_energy:.2f}")
print(f"Water: {water_energy}")
print(f"Earth: {earth_energy}")
print(f"Air: {air_energy}")

# --- Phase 2: Alchemist's Intervention ---
# Check if any element is critically low (< 100) OR critically high (> 180)
is_fire_critical = fire_energy < 100 or fire_energy > 180
is_water_critical = water_energy < 100 or water_energy > 180
is_earth_critical = earth_energy < 100 or earth_energy > 180
is_air_critical = air_energy < 100 or air_energy > 180

# Is the Orb's balance disrupted?
orb_disrupted = is_fire_critical or is_water_critical or is_earth_critical or is_air_critical

print("\n--- Alchemist's Diagnosis ---")
print(f"Is Fire Critical? {is_fire_critical}")
print(f"Is Water Critical? {is_water_critical}")
print(f"Is Earth Critical? {is_earth_critical}")
print(f"Is Air Critical? {is_air_critical}")
print(f"Is Orb Balance Disrupted? {orb_disrupted}")

# If the orb is disrupted, infuse a stabilizing essence
if orb_disrupted:
    stabilizing_essence_infusion = 50
    fire_energy += stabilizing_essence_infusion
    water_energy += stabilizing_essence_infusion
    earth_energy += stabilizing_essence_infusion
    air_energy += stabilizing_essence_infusion
    print("\nStabilizing essence infused into all elements!")
    print(f"New Fire: {fire_energy:.2f}, Water: {water_energy}, Earth: {earth_energy}, Air: {air_energy}")
