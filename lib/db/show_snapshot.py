from tabulate import tabulate
from lib.db.connection import get_session
from lib.db.models import Project, Worker

def list_projects():
    session = get_session()
    projects = session.query(Project).all()
    table = []
    for p in projects:
        worker_names = ", ".join([w.name for w in p.workers]) or "None"
        table.append({"ID": p.id, "Project Name": p.name, "Location": p.location, "Assigned Workers": worker_names})

    print("\n--- Projects ---")
    if table:
        print(tabulate(table, headers="keys", tablefmt="fancy_grid", stralign="center"))
    else:
        print("No projects found.")

def list_workers():
    session = get_session()
    workers = session.query(Worker).all()
    table = []
    for w in workers:
        project_names = ", ".join([p.name for p in w.projects]) or "None"
        table.append({"ID": w.id, "Worker Name": w.name, "Role": w.role, "Projects Assigned": project_names})

    print("\n--- Workers ---")
    if table:
        print(tabulate(table, headers="keys", tablefmt="fancy_grid", stralign="center"))
    else:
        print("No workers found.")

def show_snapshot():
    print("\n=== DATABASE SNAPSHOT ===")
    list_projects()
    list_workers()
    print("\n=========================\n")
