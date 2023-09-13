import uuid
from sqlalchemy import UUID, Column, Integer, String

from models.BaseDatabase import Base

class Talents(Base):
    __tablename__ = 'talents'
    id = Column(Integer, primary_key=True, autoincrement=True) 
    name = Column(String)
    description = Column(String)