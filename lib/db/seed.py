from connection import get_connection

def seed_data():
    conn = get_connection()
    cursor = conn.cursor()

    # Insert sample projects
    cursor.execute("INSERT INTO projects (name, location) VALUES (?, ?)", ("Highway Expansion", "Nairobi"))
    cursor.execute("INSERT INTO projects (name, location) VALUES (?, ?)", ("Office Complex", "Mombasa"))

    # Insert sample workers
    cursor.execute("INSERT INTO workers (name, role) VALUES (?, ?)", ("Alice", "Engineer"))
    cursor.execute("INSERT INTO workers (name, role) VALUES (?, ?)", ("Bob", "Foreman"))
    cursor.execute("INSERT INTO workers (name, role) VALUES (?, ?)", ("Charlie", "Laborer"))

    conn.commit()
    conn.close()
    print("Sample data inserted.")

if __name__ == "__main__":
    seed_data()
