import sqlite3
from lib.db.connection import get_connection

# --- CREATE ---
def create_project(name, location):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO projects (name, location) VALUES (?, ?)", (name, location))
    conn.commit()
    conn.close()
    print(f"Project '{name}' added successfully!")

def create_worker(name, role):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO workers (name, role) VALUES (?, ?)", (name, role))
    conn.commit()
    conn.close()
    print(f"Worker '{name}' added successfully!")

# --- READ ---
def list_projects():
    conn = get_connection()
    cursor = conn.cursor()
    rows = cursor.execute("SELECT * FROM projects").fetchall()
    conn.close()
    print("\n--- Projects ---")
    for row in rows:
        print(row)

def list_workers():
    conn = get_connection()
    cursor = conn.cursor()
    rows = cursor.execute("SELECT * FROM workers").fetchall()
    conn.close()
    print("\n--- Workers ---")
    for row in rows:
        print(row)

# --- UPDATE ---
def update_project(project_id, name=None, location=None):
    conn = get_connection()
    cursor = conn.cursor()
    if name:
        cursor.execute("UPDATE projects SET name=? WHERE id=?", (name, project_id))
    if location:
        cursor.execute("UPDATE projects SET location=? WHERE id=?", (location, project_id))
    conn.commit()
    conn.close()
    print(f"Project {project_id} updated successfully!")

def update_worker(worker_id, name=None, role=None):
    conn = get_connection()
    cursor = conn.cursor()
    if name:
        cursor.execute("UPDATE workers SET name=? WHERE id=?", (name, worker_id))
    if role:
        cursor.execute("UPDATE workers SET role=? WHERE id=?", (role, worker_id))
    conn.commit()
    conn.close()
    print(f"Worker {worker_id} updated successfully!")

# --- DELETE ---
def delete_project(project_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM projects WHERE id=?", (project_id,))
    conn.commit()
    conn.close()
    print(f"Project {project_id} deleted successfully!")

def delete_worker(worker_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM workers WHERE id=?", (worker_id,))
    conn.commit()
    conn.close()
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
        print("9. Exit")

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
            project_id = input("Project ID to update: ")
            name = input("New name (leave blank to skip): ")
            location = input("New location (leave blank to skip): ")
            update_project(project_id, name or None, location or None)
        elif choice == "6":
            worker_id = input("Worker ID to update: ")
            name = input("New name (leave blank to skip): ")
            role = input("New role (leave blank to skip): ")
            update_worker(worker_id, name or None, role or None)
        elif choice == "7":
            project_id = input("Project ID to delete: ")
            delete_project(project_id)
        elif choice == "8":
            worker_id = input("Worker ID to delete: ")
            delete_worker(worker_id)
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    menu()
