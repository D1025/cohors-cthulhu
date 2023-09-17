from sqlalchemy import Column, Enum, Integer, String
from sqlalchemy.orm import relationship

from models.CharacterSheet import character_weapons_association

from enums.WeaponType import WeaponType

from models.BaseDatabase import Base

class Weapons(Base):
    __tablename__ = "weapons"
    id = Column(Integer, primary_key=True, autoincrement=True) 
    name = Column(String)
    weaponType = Column(Enum(WeaponType))
    range = Column(String)
    damage = Column(Integer)
    effects = Column(String)
    
    characterSheet = relationship("CharacterSheet", secondary=character_weapons_association, back_populates="weapons")
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "weaponType": self.weaponType.value if self.weaponType else None,  # Enum wartość
            "range": self.range,
            "damage": self.damage,
            "effects": self.effects
        }