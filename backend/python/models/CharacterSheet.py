from sqlalchemy import UUID, Column, ForeignKey, Integer, String, Uuid
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class characterSheet(Base):
    __tablename__ = 'character_sheet'
    id = Column(UUID, primary_key=True, default=Uuid.uuid4, unique=True, nullable=False)
    name = Column(String)
    description = Column(String)
    attributes = Column(UUID, ForeignKey('attributes.id'))
    
