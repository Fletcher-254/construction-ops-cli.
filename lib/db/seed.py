from lib.db.connection import get_session

def seed_data():
    session = get_session()

    # Clear existing data
    session.execute("DELETE FROM assignments")
    session.execute("DELETE FROM workers")
    session.execute("DELETE FROM projects")
    session.commit()

    # Insert sample projects
    projects = [
        ("Mlolongo Feeder Road", "Nairobi"),
        ("Kisumu Highway Expansion", "Kisumu"),
        ("Nairobi-Kajiado Rehabilitation", "Nairobi-Kajiado"),
        ("Machakos Admin Block", "Machakos"),
        ("Nyeri Primary School Roads", "Nyeri"),
        ("Mombasa Coastal Highway Upgrade", "Mombasa"),
        ("Kitale Market Access Roads", "Kitale")
    ]

    for name, location in projects:
        session.execute("INSERT INTO projects (name, location) VALUES (?, ?)", (name, location))

    # Insert sample workers
    workers = [
        ("Alice", "Resident Engineer"),
        ("Bob", "Foreman"),
        ("Charlie", "Laborer"),
        ("Diana", "Surveyor"),
        ("Elias", "Site Engineer"),
        ("Fatuma", "Laborer"),
        ("George", "Resident Engineer")
    ]

    for name, role in workers:
        session.execute("INSERT INTO workers (name, role) VALUES (?, ?)", (name, role))

    session.commit()

    # Assign workers to projects
    assignments = [
        (1, 1),  # Alice -> Mlolongo Feeder Road
        (2, 1),  # Bob -> Mlolongo Feeder Road
        (3, 1),  # Charlie -> Mlolongo Feeder Road
        (1, 2),  # Alice -> Kisumu Highway Expansion
        (4, 2),  # Diana -> Kisumu Highway Expansion
        (5, 3),  # Elias -> Nairobi-Kajiado Rehabilitation
        (6, 3),  # Fatuma -> Nairobi-Kajiado Rehabilitation
        (7, 4),  # George -> Machakos Admin Block
        (2, 5),  # Bob -> Nyeri Primary School Roads
        (3, 6),  # Charlie -> Mombasa Coastal Highway Upgrade
        (1, 7),  # Alice -> Kitale Market Access Roads
    ]

    for worker_id, project_id in assignments:
        session.execute("INSERT INTO assignments (worker_id, project_id) VALUES (?, ?)", (worker_id, project_id))

    session.commit()
    session.close()
    print("Sample Kenyan construction data inserted successfully!")

if __name__ == "__main__":
    seed_data()
