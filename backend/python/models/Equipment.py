from sqlalchemy import ARRAY, UUID, Column, ForeignKey, Integer, String, Uuid

from backend.python.models.BaseDatabase import Base

class Equipment(Base):
    __tablename__ = 'equipment'
    id = Column(UUID, primary_key=True, default=Uuid.uuid4, unique=True, nullable=False)
    name = Column(String)
    description = Column(String)
    characterId = Column(UUID, ForeignKey('character_sheet.id'))