
import sqlite3

with sqlite3.connect('alchemist_ledger.db') as conn:
    cursor = conn.cursor()

    print("\n--- All Artifacts in the Ledger ---")
    cursor.execute("SELECT id, name, type, power, is_cursed FROM artifacts")
    artifacts = cursor.fetchall() # Fetch all results
    for artifact in artifacts:
        print(artifact)

    '''
    --- All Artifacts in the Ledger ---
    (1, 'Orb of Foresight', 'Divination', 85, 0)
    (2, 'Cursed Dagger', 'Weapon', 30, 1)
    (3, 'Healing Potion', 'Consumable', 50, 0)

    '''

    print("\n--- Divination Artifacts Only ---")
    cursor.execute("SELECT name, power FROM artifacts WHERE type = ?", ("Divination",))
    divination_artifacts = cursor.fetchall()
    for artifact in divination_artifacts:
        print(artifact)

    '''
    --- Divination Artifacts Only ---
    ('Orb of Foresight', 85)
    '''       

    print("\n--- Powerful Artifacts (Power > 40) ---")
    cursor.execute("SELECT name, power FROM artifacts WHERE power > ?", (40,))
    powerful_artifacts = cursor.fetchall()
    for artifact in powerful_artifacts:
        print(artifact)

    '''
    --- Powerful Artifacts (Power > 40) ---
    ('Orb of Foresight', 85)
    ('Healing Potion', 50)

    '''

    print("\n--- Apprentice Kael's Details ---")
    cursor.execute("SELECT name, specialty, level FROM apprentices WHERE name = ?", ("Kael",))
    kael_details = cursor.fetchone() # Fetch only one result
    if kael_details:
        print(kael_details)
    else:
        print("Kael not found.")

    '''
    --- Apprentice Kael's Details ---
    ('Kael', 'Enchantments', 5)

    '''