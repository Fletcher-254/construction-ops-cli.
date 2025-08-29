from lib.db.connection import get_session, initialize_db
from lib.db.models import Project, Worker, Assignment
from tabulate import tabulate

def create_project():
    name = input("Project name: ")
    location = input("Project location: ")
    session = get_session()
    p = Project(name=name, location=location)
    session.add(p)
    session.commit()
    session.close()
    print(f"Project '{name}' added successfully!")

def create_worker():
    name = input("Worker name: ")
    role = input("Worker role: ")
    session = get_session()
    w = Worker(name=name, role=role)
    session.add(w)
    session.commit()
    session.close()
    print(f"Worker '{name}' added successfully!")

def list_projects():
    session = get_session()
    projects = session.query(Project).all()
    session.close()
    table = [(p.id, p.name, p.location) for p in projects]
    print(tabulate(table, headers=["ID", "Name", "Location"], tablefmt="fancy_grid"))

def list_workers():
    session = get_session()
    workers = session.query(Worker).all()
    session.close()
    table = [(w.id, w.name, w.role) for w in workers]
    print(tabulate(table, headers=["ID", "Name", "Role"], tablefmt="fancy_grid"))

def assign_worker():
    list_projects()
    project_id = int(input("Project ID to assign worker to: "))
    list_workers()
    worker_id = int(input("Worker ID to assign: "))
    session = get_session()
    a = Assignment(project_id=project_id, worker_id=worker_id)
    session.add(a)
    session.commit()
    session.close()
    print(f"Worker {worker_id} assigned to project {project_id}.")

def list_assignments():
    session = get_session()
    assignments = session.query(Assignment).all()
    table = [(a.id, a.project.name, a.worker.name) for a in assignments]
    session.close()
    print(tabulate(table, headers=["Assignment ID", "Project", "Worker"], tablefmt="fancy_grid"))

def menu():
    initialize_db()  # Ensure tables exist
    while True:
        print("\n--- Construction Ops CLI ---")
        print("1. Add Project")
        print("2. Add Worker")
        print("3. List Projects")
        print("4. List Workers")
        print("5. Assign Worker to Project")
        print("6. List Assignments")
        print("7. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            create_project()
        elif choice == "2":
            create_worker()
        elif choice == "3":
            list_projects()
        elif choice == "4":
            list_workers()
        elif choice == "5":
            assign_worker()
        elif choice == "6":
            list_assignments()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
