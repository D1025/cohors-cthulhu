from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.BaseDatabase import Base
skills_focus_association = Table(
    'skills_focus_association',
    Base.metadata,
    Column('skill_id', Integer, ForeignKey('skills.id')),
    Column('focus_id', Integer, ForeignKey('focus.id'))
)

class Skills(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True, autoincrement=True)
    academia = Column(Integer)
    athletics = Column(Integer)
    crafting = Column(Integer)
    engineering = Column(Integer)
    fighting = Column(Integer)
    medicine = Column(Integer)
    observation = Column(Integer)
    persuasion = Column(Integer)
    resilience = Column(Integer)
    stealth = Column(Integer)
    survival = Column(Integer)
    tactics = Column(Integer)
    
    characterSheet = relationship('CharacterSheet', back_populates='skills')
    focus = relationship("Focus", secondary=skills_focus_association, back_populates="skills")
    
    def to_dict(self):
        # Tworzenie słownika ze wszystkimi atrybutami umiejętności
        skills_dict = {
            'id': self.id,
            'academia': self.academia,
            'athletics': self.athletics,
            'crafting': self.crafting,
            'engineering': self.engineering,
            'fighting': self.fighting,
            'medicine': self.medicine,
            'observation': self.observation,
            'persuasion': self.persuasion,
            'resilience': self.resilience,
            'stealth': self.stealth,
            'survival': self.survival,
            'tactics': self.tactics,
        }

        if self.focus:
            skills_dict['focus'] = [focus.to_dict() for focus in self.focus]

        return skills_dict

class Focus(Base):
    __tablename__ = 'focus'
    id = Column(Integer, primary_key=True, autoincrement=True)
    skill_name = Column(String)
    focus_name = Column(String)
    
    skills = relationship("Skills", secondary=skills_focus_association, back_populates="focus")

    def to_dict(self):
            return {
                'id': self.id,
                'skill_name': self.skill_name,
                'focus_name': self.focus_name
            }