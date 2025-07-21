
import sqlite3

with sqlite3.connect('alchemist_ledger.db') as conn:
    cursor = conn.cursor()

    print("\n--- Updating Artifact Power ---")
    # Increase Healing Potion power
    cursor.execute("UPDATE artifacts SET power = ? WHERE name = ?", (60, "Healing Potion"))
    conn.commit()
    print("Healing Potion power updated.")

    '''
    --- Updating Artifact Power ---
    Healing Potion power updated.

    '''

    print("\n--- Removing Cursed Artifact ---")
    # Delete the Cursed Dagger
    cursor.execute("DELETE FROM artifacts WHERE name = ?", ("Cursed Dagger",))
    conn.commit()
    print("Cursed Dagger removed from ledger.")

    '''
    --- Removing Cursed Artifact ---
    Cursed Dagger removed from ledger.

    '''

    print("\n--- Current Artifacts After Updates ---")
    cursor.execute("SELECT id, name, type, power, is_cursed FROM artifacts")
    artifacts_after_update = cursor.fetchall()
    for artifact in artifacts_after_update:
        print(artifact)

    '''
    --- Current Artifacts After Updates ---
    (1, 'Orb of Foresight', 'Divination', 85, 0)
    (3, 'Healing Potion', 'Consumable', 60, 0)
    
    '''
