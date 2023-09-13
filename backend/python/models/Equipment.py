import uuid
from sqlalchemy import UUID, Column, ForeignKey, Integer, String

from models.BaseDatabase import Base

class Equipment(Base):
    __tablename__ = 'equipment'
    id = Column(Integer, primary_key=True, autoincrement=True)     
    name = Column(String)
    description = Column(String)
    characterId = Column(Integer, ForeignKey('character_sheet.id'))