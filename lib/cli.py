import sqlite3
from lib.db.connection import get_connection

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

def menu():
    while True:
        print("\n--- Construction Ops CLI ---")
        print("1. Add Project")
        print("2. Add Worker")
        print("3. List Projects")
        print("4. List Workers")
        print("5. Exit")

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
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    menu()
