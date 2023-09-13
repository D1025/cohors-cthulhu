from sqlalchemy import ARRAY, UUID, Column, Integer, String, Uuid

from backend.python.models.BaseDatabase import Base
class Skills(Base):
    __tablename__ = 'skills'
    id = Column(UUID, primary_key=True, default=Uuid.uuid4, unique=True, nullable=False)
    academia = Column(Integer)
    academiaFocus = Column(ARRAY(String))
    fighting = Column(Integer)
    fightingFocus = Column(ARRAY(String))