from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from .connection import Base

# Association table for many-to-many
assignments = Table(
    'assignments',
    Base.metadata,
    Column('project_id', Integer, ForeignKey('projects.id'), primary_key=True),
    Column('worker_id', Integer, ForeignKey('workers.id'), primary_key=True)
)

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)

    # Link to workers
    workers = relationship("Worker", secondary=assignments, back_populates="projects")

class Worker(Base):
    __tablename__ = "workers"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)

    # Link to projects
    projects = relationship("Project", secondary=assignments, back_populates="workers")
