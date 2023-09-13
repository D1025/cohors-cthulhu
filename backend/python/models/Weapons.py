from sqlalchemy import ARRAY, UUID, Column, Enum, Integer, String, Uuid

from backend.python.enums.WeaponType import WeaponType

from backend.python.models.BaseDatabase import Base

class Weapons(Base):
    __tablename__ = 'weapons'
    id = Column(UUID, primary_key=True, default=Uuid.uuid4, unique=True, nullable=False)
    name = Column(String)
    weaponType = Column(Enum(WeaponType))
    range = Column(String)
    damage = Column(Integer)
    effects = Column(String)