import uuid
from sqlalchemy import ARRAY, UUID, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.BaseDatabase import Base

class characterSheet(Base):
    __tablename__ = 'character_sheet'
    id = Column(Integer, primary_key=True, autoincrement=True) 
    name = Column(String)
    description = Column(String)
    attributes = Column(Integer, ForeignKey('attributes.id'))
    languages = Column(ARRAY(String))
    actualStress = Column(Integer)
    maxStress = Column(Integer)
    actualInjuries = Column(Integer)
    maxInjuries = Column(Integer)
    armour = Column(Integer)
    courage = Column(Integer)
    caste = Column(String)
    resources = Column(Integer)
    background = Column(String)
    personalAgenda = Column(String)
    characteristic = Column(String)
    talents = Column(Integer, ForeignKey('talents.id'))
    weapons = Column(Integer, ForeignKey('weapons.id'))
    equipment = relationship('equipment', backref='character_sheet')
