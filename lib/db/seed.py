from lib.db.connection import get_session
from lib.db.models import Project, Worker, Assignment

def seed_data():
    session = get_session()

    # Projects
    projects = [
        ("Mombasa Road Expansion", "Mombasa"),
        ("Nairobi Highway Rehabilitation", "Nairobi"),
        ("Thika Town Feeder Roads", "Thika"),
        ("Eldoret Admin Block Construction", "Eldoret"),
        ("Kisumu Drainage Works", "Kisumu"),
        ("Nakuru Small Roads Upgrade", "Nakuru"),
        ("Kitale Residential Development", "Kitale")
    ]
    for name, location in projects:
        session.add(Project(name=name, location=location))

    # Workers
    workers = [
        ("Alice", "Engineer"),
        ("Bob", "Foreman"),
        ("Charlie", "Laborer"),
        ("Diana", "Technician"),
        ("Edward", "Surveyor")
    ]
    for name, role in workers:
        session.add(Worker(name=name, role=role))

    session.commit()

    # Assign workers to projects
    project_ids = [p.id for p in session.query(Project).all()]
    worker_ids = [w.id for w in session.query(Worker).all()]

    # Some sample assignments
    assignments = [
        (project_ids[0], worker_ids[0]),
        (project_ids[0], worker_ids[1]),
        (project_ids[1], worker_ids[0]),
        (project_ids[1], worker_ids[2]),
        (project_ids[2], worker_ids[1]),
        (project_ids[3], worker_ids[3]),
        (project_ids[4], worker_ids[4]),
        (project_ids[5], worker_ids[2]),
        (project_ids[6], worker_ids[0]),
        (project_ids[6], worker_ids[4])
    ]

    for proj_id, worker_id in assignments:
        session.add(Assignment(project_id=proj_id, worker_id=worker_id))

    session.commit()
    session.close()
    print("Sample data inserted.")

if __name__ == "__main__":
    seed_data()
