from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from models.BaseDatabase import Base

class Attributes(Base):
    __tablename__ = "attributes"
    id = Column(Integer, primary_key=True, autoincrement=True)    
    agility = Column(Integer)
    brawn = Column(Integer)
    coordination = Column(Integer)
    gravitas = Column(Integer)
    insight = Column(Integer)
    reason = Column(Integer)
    will = Column(Integer)
    
    characterSheet = relationship("CharacterSheet", back_populates="attributes")
    
    
    def to_dict(self):
        return {
            "id": self.id,
            "agility": self.agility,
            "brawn": self.brawn,
            "coordination": self.coordination,
            "gravitas": self.gravitas,
            "insight": self.insight,
            "reason": self.reason,
            "will": self.will
        }