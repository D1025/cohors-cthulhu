import uuid
from sqlalchemy import UUID, Column, Enum, Integer, String

from enums.WeaponType import WeaponType

from models.BaseDatabase import Base

class Weapons(Base):
    __tablename__ = 'weapons'
    id = Column(Integer, primary_key=True, autoincrement=True) 
    name = Column(String)
    weaponType = Column(Enum(WeaponType))
    range = Column(String)
    damage = Column(Integer)
    effects = Column(String)