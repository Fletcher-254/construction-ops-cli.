from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from lib.db.connection import Base

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String)
    assignments = relationship("Assignment", back_populates="project")

class Worker(Base):
    __tablename__ = "workers"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    role = Column(String)
    assignments = relationship("Assignment", back_populates="worker")

class Assignment(Base):
    __tablename__ = "assignments"
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    worker_id = Column(Integer, ForeignKey("workers.id"))
    project = relationship("Project", back_populates="assignments")
    worker = relationship("Worker", back_populates="assignments")
