from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from models.CharacterSheet import character_talents_association

from models.BaseDatabase import Base

class Talents(Base):
    __tablename__ = 'talents'
    id = Column(Integer, primary_key=True, autoincrement=True) 
    name = Column(String)
    description = Column(String)
    
    characterSheet = relationship("CharacterSheet", secondary=character_talents_association, back_populates="talents")
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }