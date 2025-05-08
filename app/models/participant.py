from sqlalchemy import Column, Integer, String, Text, Enum
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class ProjectType(str, enum.Enum):
    FRONTEND = "frontend"
    BACKEND = "backend"
    FULLSTACK = "fullstack"

class Participant(Base):
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True, index=True)
    github_url = Column(String, unique=True, index=True)
    project_type = Column(Enum(ProjectType))
    description = Column(Text)
    score = Column(Integer, nullable=True)
    feedback = Column(Text, nullable=True) 