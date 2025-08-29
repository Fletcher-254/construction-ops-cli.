from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_FILE = "sqlite:///construction_ops.db"  # SQLAlchemy database URL
Base = declarative_base()
engine = create_engine(DB_FILE, echo=False)
Session = sessionmaker(bind=engine)

def get_session():
    return Session()

def initialize_db():
    from lib.db.models import Project, Worker, Assignment
    Base.metadata.create_all(engine)
