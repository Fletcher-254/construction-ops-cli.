from lib.db.connection import get_session
from tabulate import tabulate
from sqlalchemy import text

def create_project(name, location):
    session = get_session()
    session.execute(text("INSERT INTO projects (name, location) VALUES (:name, :location)"), {"name": name, "location": location})
    session.commit()
    session.close()
    print(f"Project '{name}' added successfully!")

def create_worker(name, role):
    session = get_session()
    session.execute(text("INSERT INTO workers (name, role) VALUES (:name, :role)"), {"name": name, "role": role})
    session.commit()
    session.close()
    print(f"Worker '{name}' added successfully!")

def list_projects():
    session = get_session()
    rows = session.execute(text("SELECT * FROM projects")).fetchall()
    session.close()
    if rows:
        print(tabulate(rows, headers=["ID","Project Name","Location"], tablefmt="fancy_grid"))
    else:
        print("No projects found.")

def list_workers():
    session = get_session()
    rows = session.execute(text("SELECT * FROM workers")).fetchall()
    session.close()
    if rows:
        print(tabulate(rows, headers=["ID","Worker Name","Role"], tablefmt="fancy_grid"))
    else:
        print("No workers found.")

def assign_worker_to_project(worker_id, project_id):
    session = get_session()
    session.execute(text("INSERT INTO assignments (worker_id, project_id) VALUES (:worker_id, :project_id)"), {"worker_id": worker_id, "project_id": project_id})
    session.commit()
    session.close()
    print(f"Worker {worker_id} assigned to project {project_id} successfully!")

def list_assignments():
    session = get_session()
    rows = session.execute(text("""
        SELECT a.id AS AssignmentID, w.name AS WorkerName, w.role AS WorkerRole, p.name AS ProjectName, p.location AS ProjectLocation
        FROM assignments a
        JOIN workers w ON a.worker_id = w.id
        JOIN projects p ON a.project_id = p.id
        ORDER BY p.id
    """)).fetchall()
    session.close()
    if rows:
        print(tabulate(rows, headers=["Assignment ID","Worker","Role","Project","Location"], tablefmt="fancy_grid"))
    else:
        print("No assignments found.")

def show_project_snapshot():
    session = get_session()
    results = session.execute(text("""
        SELECT
            p.id AS ProjectID,
            p.name AS ProjectName,
            p.location AS Location,
            w.name AS WorkerName,
            w.role AS WorkerRole
        FROM assignments a
        JOIN projects p ON a.project_id = p.id
        JOIN workers w ON a.worker_id = w.id
        ORDER BY p.id;
    """)).fetchall()
    session.close()
    
    if results:
        print(tabulate(results, headers=["ProjectID","ProjectName","Location","WorkerName","WorkerRole"], tablefmt="fancy_grid"))
    else:
        print("No assignments found.")

def menu():
    while True:
        print("\n--- Construction Ops CLI ---")
        print("1. Add Project")
        print("2. Add Worker")
        print("3. List Projects")
        print("4. List Workers")
        print("5. Assign Worker to Project")
        print("6. List Assignments")
        print("7. Show Project Snapshot")
        print("8. Exit")

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
            list_workers()
            worker_id = input("Enter worker ID to assign: ")
            list_projects()
            project_id = input("Enter project ID to assign to: ")
            assign_worker_to_project(worker_id, project_id)
        elif choice == "6":
            list_assignments()
        elif choice == "7":
            show_project_snapshot()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    menu()
