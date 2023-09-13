import uuid
from sqlalchemy import ARRAY, UUID, Column, Integer, String

from models.BaseDatabase import Base
class Skills(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True, autoincrement=True) 
    academia = Column(Integer)
    academiaFocus = Column(ARRAY(String))
    fighting = Column(Integer)
    fightingFocus = Column(ARRAY(String))