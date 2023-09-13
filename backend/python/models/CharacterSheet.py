from sqlalchemy import ARRAY, UUID, Column, ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import relationship

from backend.python.models.BaseDatabase import Base

class characterSheet(Base):
    __tablename__ = 'character_sheet'
    id = Column(UUID, primary_key=True, default=Uuid.uuid4, unique=True, nullable=False)
    name = Column(String)
    description = Column(String)
    attributes = Column(UUID, ForeignKey('attributes.id'))
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
    talents = Column(UUID, ForeignKey('talents.id'))
    weapons = Column(UUID, ForeignKey('weapons.id'))
    equipment = relationship('equipment', backref='character_sheet')
