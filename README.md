# Construction Operations CLI

**Author:** Fletcher Nyawira  
**Project Type:** Python CLI Tool  
**Database:** SQLite  
**ORM:** SQLAlchemy  

---

## 📌 Project Overview

The **Construction Operations CLI** is a command-line interface tool designed to help construction project managers efficiently manage projects and workers.  

With this tool, you can:  
- Create, read, update, and delete projects and workers  
- Assign workers to multiple projects (many-to-many relationship)  
- Unassign workers from projects  
- View a **snapshot** of the database showing all projects with their assigned workers and all workers with their projects  

This project is useful for **small-scale construction operations** and as a **learning project** for database, ORM, and CLI development.

---

## 🚀 Features

1. **Add Projects and Workers** → Create new records directly from the CLI.  
2. **List Projects and Workers** → Display neatly formatted tables of all entries.  
3. **Update and Delete** → Modify or remove projects and workers.  
4. **Assignments Management** → Assign and unassign workers to projects.  
5. **Database Snapshot** → Get a combined view of all projects, workers, and their assignments.  

---


- **`cli.py`** → Main command-line interface file  
- **`db/connection.py`** → Database connection and session management  
- **`db/models.py`** → SQLAlchemy ORM models (`Project`, `Worker`, `Assignment`)  
- **`db/seed.py`** → Script to populate the database with sample data  

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone <repository-url>
cd construction_ops_cli

pip install pipenv
pipenv install
pipenv shell
python -m lib.db.seed

▶️ Usage

Run the CLI:

python -m lib.cli


You will see a menu with options like:
1Add Project
Add Worker
List Projects
List Workers
Update Project
Update Worker
Delete Project
Delete Worker
Assign Worker to Project
Unassign Worker from Project
Show Snapshot
Exit

##⚙️ Installation

Python 3.10+ → Core programming language
SQLite → Lightweight relational database
SQLAlchemy → ORM for database interaction
Tabulate → For neatly formatted CLI tables


