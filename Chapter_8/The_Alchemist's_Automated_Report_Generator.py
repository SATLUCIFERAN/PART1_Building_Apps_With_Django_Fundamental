
import datetime

def generate_daily_magical_report(activity_data: list[dict]):
    """
    Generates a daily report of magical activity and saves it to a file.
    :param activity_data: A list of dictionaries, each describing a magical event.
    """
    today_date = datetime.date.today().strftime("%Y-%m-%d")
    report_filename = f"magical_report_{today_date}.txt"
    
    report_lines = []
    report_lines.append(f"--- Daily Magical Activity Report ({today_date}) ---\n")
    report_lines.append("Overview:\n")
    
    total_spells_cast = 0
    total_energy_consumed = 0
    anomalies_detected = 0
    
    for event in activity_data:
        event_type = event.get("type", "Unknown")
        description = event.get("description", "No description")
        energy_cost = event.get("energy_cost", 0)
        is_anomaly = event.get("is_anomaly", False)
        
        report_lines.append(f"- Type: {event_type}, Desc: {description}, Energy Cost: {energy_cost}")
        
        if event_type == "Spell Cast":
            total_spells_cast += 1
            total_energy_consumed += energy_cost
        if is_anomaly:
            anomalies_detected += 1
            
    report_lines.append(f"\nSummary for {today_date}:\n")
    report_lines.append(f"Total Spells Cast: {total_spells_cast}\n")
    report_lines.append(f"Total Energy Consumed: {total_energy_consumed}\n")
    report_lines.append(f"Anomalies Detected: {anomalies_detected}\n")
    report_lines.append("\n--- End of Report ---\n")
    
    print(f"\nGenerating report: {report_filename}...")
    with open(report_filename, "w") as report_file:
        report_file.writelines(report_lines)
    print(f"Report '{report_filename}' successfully generated and saved!")

# Sample magical activity data
daily_events = [
    {"type": "Spell Cast", "description": "Healing Aura on injured villager", "energy_cost": 15, "is_anomaly": False},
    {"type": "Artifact Activation", "description": "Orb of Foresight activated", "energy_cost": 5, "is_anomaly": False},
    {"type": "Spell Cast", "description": "Fireball on rogue goblin", "energy_cost": 20, "is_anomaly": False},
    {"type": "Energy Surge", "description": "Minor ley line fluctuation", "energy_cost": 0, "is_anomaly": True},
    {"type": "Spell Cast", "description": "Teleportation to distant shrine", "energy_cost": 50, "is_anomaly": False},
]

generate_daily_magical_report(daily_events)

# You can then open 'magical_report_YYYY-MM-DD.txt' to see the generated report