from sqlalchemy import UUID, Column, Integer, String, Uuid
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class characterSheet(Base):
    __tablename__ = 'skills'
    id = Column(UUID, primary_key=True, default=Uuid.uuid4, unique=True, nullable=False)
    academia = Column(Integer)
    fighting = Column(Integer)
    