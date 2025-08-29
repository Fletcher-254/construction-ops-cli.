from lib.db.connection import get_session, initialize_db
from lib.db.models import Project, Worker

def seed_data():
    initialize_db()
    session = get_session()

    # Clear old data
    session.query(Project).delete()
    session.query(Worker).delete()
    session.commit()

    # Sample projects
    projects = [
        Project(name="Mombasa Road Expansion", location="Mombasa"),
        Project(name="Nairobi West Feeder Road", location="Nairobi"),
        Project(name="Kisumu Highway Rehabilitation", location="Kisumu"),
        Project(name="Machakos Admin Block Construction", location="Machakos"),
        Project(name="Thika Small Bridge Project", location="Thika"),
        Project(name="Kajiado Local Road Upgrade", location="Kajiado"),
        Project(name="Nakuru Residential Complex", location="Nakuru")
    ]

    # Sample workers
    workers = [
        Worker(name="Alice Mwangi", role="Resident Engineer"),
        Worker(name="Bob Otieno", role="Foreman"),
        Worker(name="Charlie Njoroge", role="Laborer"),
        Worker(name="Diana Wambui", role="Architect"),
        Worker(name="Ezekiel Ochieng", role="Site Supervisor"),
        Worker(name="Faith Kamau", role="Quantity Surveyor"),
        Worker(name="George Kiptoo", role="Safety Officer")
    ]

    session.add_all(projects)
    session.add_all(workers)
    session.commit()

    # Assign workers to projects
    projects[0].workers.extend([workers[0], workers[1], workers[2]])
    projects[1].workers.extend([workers[0], workers[3], workers[4]])
    projects[2].workers.extend([workers[1], workers[5], workers[6]])
    projects[3].workers.extend([workers[3], workers[0]])
    projects[4].workers.extend([workers[4], workers[5]])
    projects[5].workers.extend([workers[6], workers[1]])
    projects[6].workers.extend([workers[3], workers[2], workers[0]])

    session.commit()
    session.close()
    print("Sample data inserted successfully.")

if __name__ == "__main__":
    seed_data()
