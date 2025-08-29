from lib.db.connection import get_session
from lib.db.models import Project, Worker, Assignment
from tabulate import tabulate


def show_projects():
    session = get_session()
    rows = []
    projects = session.query(Project).all()
    for project in projects:
        workers = [a.worker.name for a in project.assignments]
        rows.append([project.id, project.name, project.location, ", ".join(workers)])
    print(tabulate(rows, headers=["ID", "Project Name", "Location", "Workers"], tablefmt="fancy_grid"))
    session.close()


def show_workers():
    session = get_session()
    rows = []
    workers = session.query(Worker).all()
    for worker in workers:
        projects = [a.project.name for a in worker.assignments]
        rows.append([worker.id, worker.name, worker.role, ", ".join(projects)])
    print(tabulate(rows, headers=["ID", "Worker Name", "Role", "Projects"], tablefmt="fancy_grid"))
    session.close()


def show_assignments():
    session = get_session()
    rows = []
    assignments = session.query(Assignment).all()
    for a in assignments:
        project_name = a.project.name if a.project else "❌ Deleted Project"
        worker_name = a.worker.name if a.worker else "❌ Deleted Worker"
        rows.append([a.id, project_name, worker_name])
    print(tabulate(rows, headers=["ID", "Project", "Worker"], tablefmt="fancy_grid"))
    session.close()


def add_project():
    session = get_session()
    name = input("Enter project name: ")
    location = input("Enter project location: ")
    project = Project(name=name, location=location)
    session.add(project)
    session.commit()
    print("✅ Project added successfully.")
    session.close()


def add_worker():
    session = get_session()
    name = input("Enter worker name: ")
    role = input("Enter worker role: ")
    worker = Worker(name=name, role=role)
    session.add(worker)
    session.commit()
    print("✅ Worker added successfully.")
    session.close()


def assign_worker():
    session = get_session()
    show_projects()
    project_id = int(input("Enter project ID: "))
    show_workers()
    worker_id = int(input("Enter worker ID: "))

    assignment = Assignment(project_id=project_id, worker_id=worker_id)
    session.add(assignment)
    try:
        session.commit()
        print("✅ Worker assigned successfully.")
    except Exception:
        session.rollback()
        print("⚠️ This worker is already assigned to that project.")
    session.close()


def delete_project():
    session = get_session()
    show_projects()
    project_id = int(input("Enter project ID to delete: "))
    project = session.query(Project).get(project_id)
    if project:
        session.delete(project)
        session.commit()
        print("🗑️ Project deleted.")
    else:
        print("⚠️ Project not found.")
    session.close()


def delete_worker():
    session = get_session()
    show_workers()
    worker_id = int(input("Enter worker ID to delete: "))
    worker = session.query(Worker).get(worker_id)
    if worker:
        session.delete(worker)
        session.commit()
        print("🗑️ Worker deleted.")
    else:
        print("⚠️ Worker not found.")
    session.close()


def menu():
    while True:
        print("\n📋 Construction Ops CLI")
        print("1. Show Projects")
        print("2. Show Workers")
        print("3. Show Assignments")
        print("4. Add Project")
        print("5. Add Worker")
        print("6. Assign Worker to Project")
        print("7. Delete Project")
        print("8. Delete Worker")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_projects()
        elif choice == "2":
            show_workers()
        elif choice == "3":
            show_assignments()
        elif choice == "4":
            add_project()
        elif choice == "5":
            add_worker()
        elif choice == "6":
            assign_worker()
        elif choice == "7":
            delete_project()
        elif choice == "8":
            delete_worker()
        elif choice == "9":
            print("Exiting Aquiltech systems!")
            break
        else:
            print("⚠️ Invalid choice, try again.")


if __name__ == "__main__":
    menu()
