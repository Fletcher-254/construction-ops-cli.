from .connection import get_session, Base, engine
from .models import Project, Worker

# Create all tables
Base.metadata.create_all(engine)

def seed_data():
    session = get_session()

    # --- Sample Projects ---
    projects = [
        Project(name="Mombasa Road Expansion", location="Mombasa"),
        Project(name="Nairobi Highway Rehab", location="Nairobi"),
        Project(name="Ngong Road Upgrade", location="Ngong"),
        Project(name="Thika Superhighway Repair", location="Thika"),
        Project(name="Kisumu Bridge Construction", location="Kisumu")
    ]
    session.add_all(projects)

    # --- Sample Workers  ---
    workers = [
        Worker(name="Alice", role="Engineer"),
        Worker(name="Bob", role="Foreman"),
        Worker(name="Charlie", role="Laborer"),
        Worker(name="Diana", role="Surveyor"),
        Worker(name="Ethan", role="Architect"),
        Worker(name="Fiona", role="Engineer"),
        Worker(name="George", role="Technician"),
        Worker(name="Hannah", role="Laborer"),
        Worker(name="Ian", role="Foreman"),
        Worker(name="Julia", role="Project Manager")
    ]
    session.add_all(workers)
    session.commit()  # Commit projects and workers first to get IDs

    # --- Assign workers to projects ---
    projects[0].workers.extend([workers[0], workers[1], workers[2]])  # Mombasa Road
    projects[1].workers.extend([workers[3], workers[4], workers[5]])  # Nairobi Highway
    projects[2].workers.extend([workers[6], workers[7]])               # Ngong Road
    projects[3].workers.extend([workers[8], workers[9]])               # Thika Superhighway
    projects[4].workers.extend([workers[0], workers[4], workers[7]])  # Kisumu Bridge

    session.commit()
    session.close()
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_data()
