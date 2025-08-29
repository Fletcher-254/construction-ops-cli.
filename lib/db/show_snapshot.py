from lib.db.connection import get_session
from lib.db.models import Project, Worker, Assignment
from tabulate import tabulate

def show_project_snapshot():
    session = get_session()

    # Query projects and related workers
    rows = []
    projects = session.query(Project).all()
    for project in projects:
        workers = [a.worker.name for a in project.assignments]
        rows.append([project.id, project.name, project.location, ", ".join(workers)])

    print(tabulate(rows, headers=["Project ID", "Project Name", "Location", "Assigned Workers"], tablefmt="grid"))
    session.close()

if __name__ == "__main__":
    show_project_snapshot()
