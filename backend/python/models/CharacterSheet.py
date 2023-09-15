from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.BaseDatabase import Base
character_weapons_association = Table(
    'character_weapons_association',
    Base.metadata,
    Column('character_id', Integer, ForeignKey('character_sheet.id')),
    Column('weapon_id', Integer, ForeignKey('weapons.id'))
)

character_talents_association = Table(
    'character_talents_association',
    Base.metadata,
    Column('character_id', Integer, ForeignKey('character_sheet.id')),
    Column('talent_id', Integer, ForeignKey('talents.id'))
)

character_equipment_association = Table(
    'character_equipment_association',
    Base.metadata,
    Column('character_id', Integer, ForeignKey('character_sheet.id')),
    Column('equipment_id', Integer, ForeignKey('equipment.id'))
)

class CharacterSheet(Base):
    __tablename__ = 'character_sheet'
    id = Column(Integer, primary_key=True, autoincrement=True) 
    name = Column(String)
    description = Column(String)
    attributes_id = Column(Integer, ForeignKey('attributes.id'))
    skills_id = Column(Integer, ForeignKey('skills.id'))
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
    

    attributes = relationship("Attributes", back_populates="characterSheet")
    talents = relationship("Talents", secondary=character_talents_association, back_populates="characterSheet")
    weapons = relationship("Weapons", secondary=character_weapons_association, back_populates="characterSheet")
    equipment = relationship("Equipment", secondary=character_equipment_association, back_populates="characterSheet")
    skills = relationship('Skills', back_populates='characterSheet')
    
    def to_dict(self):
        attributes_dict = self.attributes.to_dict() if self.attributes else None

        talents_list = [talent.to_dict() for talent in self.talents]

        weapons_list = [weapon.to_dict() for weapon in self.weapons]

        equipment_list = [equip.to_dict() for equip in self.equipment]

        skills_dict = self.skills.to_dict() if self.skills else None

        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'attributes': attributes_dict,
            'actualStress': self.actualStress,
            'maxStress': self.maxStress,
            'actualInjuries': self.actualInjuries,
            'maxInjuries': self.maxInjuries,
            'armour': self.armour,
            'courage': self.courage,
            'caste': self.caste,
            'resources': self.resources,
            'background': self.background,
            'personalAgenda': self.personalAgenda,
            'characteristic': self.characteristic,
            'talents': talents_list,
            'weapons': weapons_list,
            'equipment': equipment_list,
            'skills': skills_dict
        }