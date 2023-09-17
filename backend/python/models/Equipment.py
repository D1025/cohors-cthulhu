from sqlalchemy import UUID, Column, Integer, String
from sqlalchemy.orm import relationship

from models.BaseDatabase import Base

from models.CharacterSheet import character_equipment_association

class Equipment(Base):
    __tablename__ = "equipment"
    id = Column(Integer, primary_key=True, autoincrement=True)     
    name = Column(String)
    description = Column(String)
    
    characterSheet = relationship("CharacterSheet", secondary=character_equipment_association, back_populates="equipment")
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }