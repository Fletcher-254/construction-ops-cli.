from lib.db.connection import get_session, initialize_db
from lib.db.models import Project, Worker
from tabulate import tabulate

def list_projects(session):
    projects = session.query(Project).all()
    table = [(p.id, p.name, p.location) for p in projects]
    print(tabulate(table, headers=["ID", "Name", "Location"], tablefmt="fancy_grid"))

def list_workers(session):
    workers = session.query(Worker).all()
    table = [(w.id, w.name, w.role) for w in workers]
    print(tabulate(table, headers=["ID", "Name", "Role"], tablefmt="fancy_grid"))

def assign_worker(session):
    list_workers(session)
    worker_id = int(input("Enter Worker ID to assign: "))
    list_projects(session)
    project_id = int(input("Enter Project ID to assign to: "))
    worker = session.query(Worker).get(worker_id)
    project = session.query(Project).get(project_id)
    if worker and project:
        project.workers.append(worker)
        session.commit()
        print(f"{worker.name} assigned to {project.name}")
    else:
        print("Invalid IDs")

def list_assignments(session):
    projects = session.query(Project).all()
    table = []
    for p in projects:
        for w in p.workers:
            table.append([p.name, p.location, w.name, w.role])
    print(tabulate(table, headers=["Project", "Location", "Worker", "Role"], tablefmt="fancy_grid"))

def project_snapshot(session):
    projects = session.query(Project).all()
    table = []

    for p in projects:
        workers_list = [f"{w.name} ({w.role})" for w in p.workers]
        workers_str = ", ".join(workers_list) if workers_list else "No workers assigned"
        table.append([p.id, p.name, p.location, workers_str])

    print(tabulate(table, headers=["ID", "Project", "Location", "Workers"], tablefmt="fancy_grid"))

def menu():
    initialize_db()
    session = get_session()
    while True:
        print("\n--- Construction Ops CLI ---")
        print("1. List Projects")
        print("2. List Workers")
        print("3. Assign Worker to Project")
        print("4. List Assignments")
        print("5. Project Snapshot")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            list_projects(session)
        elif choice == "2":
            list_workers(session)
        elif choice == "3":
            assign_worker(session)
        elif choice == "4":
            list_assignments(session)
        elif choice == "5":
            project_snapshot(session)
        elif choice == "6":
            session.close()
            print("Exiting Aquiltech Systems!")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    menu()
