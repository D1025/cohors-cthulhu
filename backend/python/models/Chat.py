from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from models.BaseDatabase import Base
from enums.JsonType import JsonType

class Chat(Base):
    __tablename__ = "chat"
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String)
    nickname = Column(String)
    message = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    attributeValue = Column(Integer)
    skillValue = Column(Integer)
    focus = Column(Integer)
    attribute = Column(String)
    skill = Column(String)
    rolls = Column(String)
    complication = Column(Integer)
    successes = Column(Integer)
    rolls = Column(String)
    damage = Column(Integer)
    effects = Column(Integer)

    def createMessage(self, nickname, message):
        self.type = "message"
        self.nickname = nickname
        self.message = message
        
    def createRoll(self, nickname, attributeValue, skillValue, focus, attribute, skill, rolls, complication, successes):
        self.type = "roll"
        self.nickname = nickname
        self.attributeValue = attributeValue
        self.skillValue = skillValue
        self.focus = 1 if focus else 0
        self.attribute = attribute
        self.skill = skill
        self.rolls = str(rolls)
        self.complication = complication
        self.successes = successes
        
    def createDamage(self, nickname, damage, effects, rolls):
        self.type = "damage"
        self.nickname = nickname
        self.damage = damage
        self.effects = effects
        self.rolls = rolls
    
    
    def to_dict(self):
        if self.type == "message":
            return {
                "id": self.id,
                "nickname": self.nickname,
                "message": self.message,
                "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
            }
        elif self.type == "roll":
            return {
                "id": self.id,
                "nickname": self.nickname,
                "attributeValue": self.attributeValue,
                "skillValue": self.skillValue,
                "focus": bool(self.focus),
                "attribute": self.attribute,
                "skill": self.skill,
                "rolls": self.rolls,
                "complication": self.complication,
                "successes": self.successes,
                "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
            }
        elif self.type == "damage":
            return {
                "id": self.id,
                "nickname": self.nickname,
                "damage": self.damage,
                "effects": self.effects,
                "rolls": self.rolls,
                "timestamp": self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
            }
        
    def addToDatabase(self, session):
        session.add(self)
        session.commit()