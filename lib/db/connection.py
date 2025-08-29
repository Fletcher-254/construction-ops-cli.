from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Define Base here
Base = declarative_base()

DATABASE_URL = "sqlite:///construction_ops.db"

engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)

def get_session():
    return Session()

def initialize_db():
    from . import models  # Import models here
    Base.metadata.create_all(engine)
