import sqlite3

def create_database():

    conn = sqlite3.connect("tasks.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()