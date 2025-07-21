
import sqlite3

with sqlite3.connect('alchemist_ledger.db') as conn:
    cursor = conn.cursor()

    # Insert artifacts
    cursor.execute("INSERT INTO artifacts (name, type, power, is_cursed) VALUES (?, ?, ?, ?)",
                   ("Orb of Foresight", "Divination", 85, False))
    cursor.execute("INSERT INTO artifacts (name, type, power, is_cursed) VALUES (?, ?, ?, ?)",
                   ("Cursed Dagger", "Weapon", 30, True))
    cursor.execute("INSERT INTO artifacts (name, type, power, is_cursed) VALUES (?, ?, ?, ?)",
                   ("Healing Potion", "Consumable", 50, False))

    # Insert apprentices
    cursor.execute("INSERT INTO apprentices (name, specialty, level) VALUES (?, ?, ?)",
                   ("Elara", "Potions", 3))
    cursor.execute("INSERT INTO apprentices (name, specialty, level) VALUES (?, ?, ?)",
                   ("Kael", "Enchantments", 5))

    conn.commit() # Save the inserted data
    print("\nArtifacts and apprentices added to the ledger.")
    

    #Artifacts and apprentices added to the ledger.