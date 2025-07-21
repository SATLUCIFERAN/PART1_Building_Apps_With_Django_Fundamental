
import sqlite3

def setup_quest_log(db_name="quest_ledger.db"):
    """Connects to the database and ensures the quests table exists."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS quests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL UNIQUE,
                description TEXT,
                status TEXT DEFAULT 'Pending',
                reward_gold INTEGER,
                difficulty TEXT
            )
        ''')
        conn.commit()
    print(f"Quest ledger '{db_name}' setup complete.")

def add_quest(db_name, title, description, reward_gold, difficulty):
    """Adds a new quest to the ledger."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO quests (title, description, reward_gold, difficulty) VALUES (?, ?, ?, ?)",
                           (title, description, reward_gold, difficulty))
            conn.commit()
            print(f"Quest '{title}' added.")
        except sqlite3.IntegrityError:
            print(f"Quest '{title}' already exists (title must be unique).")

def update_quest_status(db_name, title, new_status):
    """Updates the status of an existing quest."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE quests SET status = ? WHERE title = ?", (new_status, title))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"Status for '{title}' updated to '{new_status}'.")
        else:
            print(f"Quest '{title}' not found.")

def get_quests(db_name, status_filter=None):
    """Retrieves quests, optionally filtered by status."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        if status_filter:
            cursor.execute("SELECT id, title, status, reward_gold, difficulty FROM quests WHERE status = ?", (status_filter,))
        else:
            cursor.execute("SELECT id, title, status, reward_gold, difficulty FROM quests")
        quests = cursor.fetchall()
        return quests

def delete_quest(db_name, title):
    """Deletes a quest from the ledger."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM quests WHERE title = ?", (title,))
        conn.commit()
        if cursor.rowcount > 0:
            print(f"Quest '{title}' deleted.")
        else:
            print(f"Quest '{title}' not found.")

# --- Execute Quest Log Operations ---
db_file = "quest_ledger.db"
setup_quest_log(db_file)

print("\n--- Adding Quests ---")
add_quest(db_file, "The Lost Amulet", "Find the ancient amulet in the Whispering Forest.", 250, "Easy")
add_quest(db_file, "Dragon's Hoard", "Slay the dragon and claim its treasure.", 1000, "Hard")
add_quest(db_file, "Rescue Villagers", "Save the villagers from the goblin horde.", 150, "Medium")
add_quest(db_file, "The Lost Amulet", "Duplicate quest attempt.", 250, "Easy") # Will show error

print("\n--- Current Quests ---")
current_quests = get_quests(db_file)
for q in current_quests:
    print(f"ID: {q[0]}, Title: {q[1]}, Status: {q[2]}, Reward: {q[3]}, Difficulty: {q[4]}")

print("\n--- Updating Quest Status ---")
update_quest_status(db_file, "The Lost Amulet", "Completed")
update_quest_status(db_file, "Dragon's Hoard", "In Progress")
update_quest_status(db_file, "Non-Existent Quest", "Failed")

print("\n--- Completed Quests ---")
completed_quests = get_quests(db_file, status_filter="Completed")
for q in completed_quests:
    print(f"ID: {q[0]}, Title: {q[1]}, Status: {q[2]}, Reward: {q[3]}, Difficulty: {q[4]}")

print("\n--- Deleting a Quest ---")
delete_quest(db_file, "Rescue Villagers")

print("\n--- Final Quest List ---")
final_quests = get_quests(db_file)
for q in final_quests:
    print(f"ID: {q[0]}, Title: {q[1]}, Status: {q[2]}, Reward: {q[3]}, Difficulty: {q[4]}")
