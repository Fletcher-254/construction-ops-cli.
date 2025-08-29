from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# Many-to-many association table
assignment_table = Table(
    "assignments",
    Base.metadata,
    Column("worker_id", Integer, ForeignKey("workers.id"), primary_key=True),
    Column("project_id", Integer, ForeignKey("projects.id"), primary_key=True)
)

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    workers = relationship("Worker", secondary=assignment_table, back_populates="projects")

    def __repr__(self):
        return f"<Project(id={self.id}, name={self.name}, location={self.location})>"

class Worker(Base):
    __tablename__ = "workers"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    projects = relationship("Project", secondary=assignment_table, back_populates="workers")

    def __repr__(self):
        return f"<Worker(id={self.id}, name={self.name}, role={self.role})>"
