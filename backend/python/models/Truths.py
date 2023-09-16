from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.CharacterSheet import character_truths_association

from models.BaseDatabase import Base

class Truths(Base):
    __tablename__ = "truths"
    id = Column(Integer, primary_key=True, autoincrement=True)    
    description = Column(String)
    characterSheet = relationship("CharacterSheet", secondary=character_truths_association, back_populates="truths")
    
    
    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description
        }