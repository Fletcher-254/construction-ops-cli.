from lib.db.connection import get_session
from lib.db.models import Project, Worker, assignments
from tabulate import tabulate

# --- CREATE ---
def create_project(name, location):
    session = get_session()
    new_project = Project(name=name, location=location)
    session.add(new_project)
    session.commit()
    print(f"Project '{name}' added successfully!")

def create_worker(name, role):
    session = get_session()
    new_worker = Worker(name=name, role=role)
    session.add(new_worker)
    session.commit()
    print(f"Worker '{name}' added successfully!")

# --- ASSIGN / UNASSIGN ---
def assign_worker_to_project(worker_id, project_id):
    session = get_session()
    worker = session.query(Worker).filter_by(id=worker_id).first()
    project = session.query(Project).filter_by(id=project_id).first()
    if not worker or not project:
        print("Invalid worker or project ID.")
        return
    if worker not in project.workers:
        project.workers.append(worker)
        session.commit()
        print(f"Assigned {worker.name} to {project.name}.")
    else:
        print(f"{worker.name} is already assigned to {project.name}.")

def unassign_worker_from_project(worker_id, project_id):
    session = get_session()
    worker = session.query(Worker).filter_by(id=worker_id).first()
    project = session.query(Project).filter_by(id=project_id).first()
    if not worker or not project:
        print("Invalid worker or project ID.")
        return
    if worker in project.workers:
        project.workers.remove(worker)
        session.commit()
        print(f"Unassigned {worker.name} from {project.name}.")
    else:
        print(f"{worker.name} is not assigned to {project.name}.")

# --- LIST / SNAPSHOT ---
def list_projects():
    session = get_session()
    projects = session.query(Project).all()
    table = []
    for p in projects:
        worker_names = ", ".join([w.name for w in p.workers]) or "None"
        table.append({"ID": p.id, "Name": p.name, "Location": p.location, "Workers": worker_names})
    print("\n--- Projects ---")
    if table:
        print(tabulate(table, headers="keys", tablefmt="fancy_grid"))
    else:
        print("No projects found.")

def list_workers():
    session = get_session()
    workers = session.query(Worker).all()
    table = []
    for w in workers:
        project_names = ", ".join([p.name for p in w.projects]) or "None"
        table.append({"ID": w.id, "Name": w.name, "Role": w.role, "Projects": project_names})
    print("\n--- Workers ---")
    if table:
        print(tabulate(table, headers="keys", tablefmt="fancy_grid"))
    else:
        print("No workers found.")

def show_snapshot():
    print("\n=== Database Snapshot ===")
    list_projects()
    list_workers()

# --- UPDATE / DELETE ---
def update_project(project_id, name=None, location=None):
    session = get_session()
    project = session.query(Project).filter_by(id=project_id).first()
    if not project:
        print(f"No project found with ID {project_id}")
        return
    if name:
        project.name = name
    if location:
        project.location = location
    session.commit()
    print(f"Project {project_id} updated successfully!")

def update_worker(worker_id, name=None, role=None):
    session = get_session()
    worker = session.query(Worker).filter_by(id=worker_id).first()
    if not worker:
        print(f"No worker found with ID {worker_id}")
        return
    if name:
        worker.name = name
    if role:
        worker.role = role
    session.commit()
    print(f"Worker {worker_id} updated successfully!")

def delete_project(project_id):
    session = get_session()
    project = session.query(Project).filter_by(id=project_id).first()
    if not project:
        print(f"No project found with ID {project_id}")
        return
    session.delete(project)
    session.commit()
    print(f"Project {project_id} deleted successfully!")

def delete_worker(worker_id):
    session = get_session()
    worker = session.query(Worker).filter_by(id=worker_id).first()
    if not worker:
        print(f"No worker found with ID {worker_id}")
        return
    session.delete(worker)
    session.commit()
    print(f"Worker {worker_id} deleted successfully!")

# --- MENU ---
def menu():
    while True:
        print("\n--- Construction Ops CLI ---")
        print("1. Add Project")
        print("2. Add Worker")
        print("3. List Projects")
        print("4. List Workers")
        print("5. Update Project")
        print("6. Update Worker")
        print("7. Delete Project")
        print("8. Delete Worker")
        print("9. Assign Worker to Project")
        print("10. Unassign Worker from Project")
        print("11. Show Snapshot")
        print("12. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Project name: ")
            location = input("Project location: ")
            create_project(name, location)
        elif choice == "2":
            name = input("Worker name: ")
            role = input("Worker role: ")
            create_worker(name, role)
        elif choice == "3":
            list_projects()
        elif choice == "4":
            list_workers()
        elif choice == "5":
            project_id = int(input("Project ID to update: "))
            name = input("New name (leave blank to skip): ")
            location = input("New location (leave blank to skip): ")
            update_project(project_id, name or None, location or None)
        elif choice == "6":
            worker_id = int(input("Worker ID to update: "))
            name = input("New name (leave blank to skip): ")
            role = input("New role (leave blank to skip): ")
            update_worker(worker_id, name or None, role or None)
        elif choice == "7":
            project_id = int(input("Project ID to delete: "))
            delete_project(project_id)
        elif choice == "8":
            worker_id = int(input("Worker ID to delete: "))
            delete_worker(worker_id)
        elif choice == "9":
            worker_id = int(input("Worker ID to assign: "))
            project_id = int(input("Project ID to assign to: "))
            assign_worker_to_project(worker_id, project_id)
        elif choice == "10":
            worker_id = int(input("Worker ID to unassign: "))
            project_id = int(input("Project ID to remove from: "))
            unassign_worker_from_project(worker_id, project_id)
        elif choice == "11":
            show_snapshot()
        elif choice == "12":
            print("Exiting Aquiltech Systems!")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    menu()
