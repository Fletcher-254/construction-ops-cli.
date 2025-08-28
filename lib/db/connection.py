import sqlite3

DB_NAME = "construction_ops.db"

def get_connection():
    """Return a new database connection."""
    conn = sqlite3.connect(DB_NAME)
    return conn
