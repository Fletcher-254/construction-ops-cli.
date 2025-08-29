from lib.db.connection import get_session, initialize_db
from lib.db.models import Project, Worker, Assignment

def seed_data():
    initialize_db()
    session = get_session()

    # Projects
    p1 = Project(name="Highway Expansion", location="Nairobi")
    p2 = Project(name="Office Complex", location="Mombasa")
    session.add_all([p1, p2])

    # Workers
    w1 = Worker(name="Alice", role="Engineer")
    w2 = Worker(name="Bob", role="Foreman")
    w3 = Worker(name="Charlie", role="Laborer")
    session.add_all([w1, w2, w3])
    session.commit()

    # Assignments
    session.add_all([
        Assignment(project=p1, worker=w1),
        Assignment(project=p1, worker=w2),
        Assignment(project=p2, worker=w3)
    ])
    session.commit()
    session.close()
    print("Sample data inserted.")

if __name__ == "__main__":
    seed_data()
