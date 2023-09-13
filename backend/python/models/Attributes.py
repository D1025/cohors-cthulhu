import uuid
from sqlalchemy import UUID, Column, Integer

from models.BaseDatabase import Base

class Attributes(Base):
    __tablename__ = 'attributes'
    id = Column(Integer, primary_key=True, autoincrement=True)    
    agility = Column(Integer)
    brawn = Column(Integer)
    coordination = Column(Integer)
    gravitas = Column(Integer)
    insight = Column(Integer)
    reason = Column(Integer)
    will = Column(Integer)