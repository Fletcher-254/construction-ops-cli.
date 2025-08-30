# Construction Operations CLI

**Author:** Fletcher Nyawira  
**Project Type:** Python CLI Tool  
**Database:** SQLite  
**ORM:** SQLAlchemy  

---

## Project Overview

The **Construction Operations CLI** is a command-line interface tool designed to help construction project managers efficiently manage projects and workers. The tool allows users to:

- Create, read, update, and delete projects and workers.  
- Assign workers to multiple projects (many-to-many relationship).  
- Unassign workers from projects.  
- View a snapshot of the database showing all projects with assigned workers and all workers with their projects.  

This tool is intended for small-scale construction operations or as a learning project for project and workforce management.

---

## Features

1. Add Projects and Workers  
2. List Projects and Workers  
3. Update and Delete  
4. Assign/Unassign Workers to Projects  
5. Database Snapshot  

---

## Project Structure

# Construction Operations CLI

**Author:** Fletcher Nyawira  
**Project Type:** Python CLI Tool  
**Database:** SQLite  
**ORM:** SQLAlchemy  

---

## Overview

A command-line interface to manage construction projects and workers. Features:

- Create, read, update, and delete projects and workers  
- Assign workers to multiple projects and unassign them  
- View a database snapshot showing projects and assigned workers  

---

## Features

1. Add Projects and Workers  
2. List Projects and Workers  
3. Update and Delete entries  
4. Assign/Unassign Workers to Projects  
5. Database Snapshot  

---

## Project Structure

construction_ops_cli/
│ README.md
│ Pipfile
│ Pipfile.lock
│ construction_ops.db
│
└───lib
│ cli.py
│ init.py
│
└───db
│ connection.py
│ models.py
│ seed.py
│ init.py


---

## Installation

```bash
git clone <repository-url>
cd construction_ops_cli
pip install pipenv
pipenv install
pipenv shell
python -m lib.db.seed

python -m lib.cli

Usage

Run the CLI:
python -m lib.cli


Menu options:
Follow the prompts to perform actions.

Technologies Used
Python 3.10+
SQLite
SQLAlchemy
Tabulate

Author- Fletcher Nyawira
