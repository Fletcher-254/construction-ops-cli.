from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint

Base = declarative_base()

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    assignments = relationship("Assignment", back_populates="project", cascade="all, delete-orphan")

class Worker(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    assignments = relationship("Assignment", back_populates="worker", cascade="all, delete-orphan")

class Assignment(Base):
    __tablename__ = "assignments"
    __table_args__ = (UniqueConstraint("project_id", "worker_id", name="uix_project_worker"),)

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    worker_id = Column(Integer, ForeignKey("workers.id"))

    project = relationship("Project", back_populates="assignments")
    worker = relationship("Worker", back_populates="assignments")
