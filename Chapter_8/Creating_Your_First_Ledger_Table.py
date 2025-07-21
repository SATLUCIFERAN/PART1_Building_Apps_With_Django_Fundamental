
import sqlite3

print("--- Setting Up Alchemist's Ledger ---")
# Use 'with' for safe connection handling
with sqlite3.connect('alchemist_ledger.db') as conn:
    cursor = conn.cursor()

    # Create a table for artifacts if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS artifacts (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            power INTEGER,
            is_cursed BOOLEAN
        )
    ''')
    print("Table 'artifacts' ensured to exist.")

    # Create a table for apprentices
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS apprentices (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            specialty TEXT,
            level INTEGER
        )
    ''')
    print("Table 'apprentices' ensured to exist.")

    conn.commit() # Save the table creations
print("Alchemist's Ledger setup complete.")


'''
--- Setting Up Alchemist's Ledger ---
Table 'artifacts' ensured to exist.
Table 'apprentices' ensured to exist.
Alchemist's Ledger setup complete.

'''
