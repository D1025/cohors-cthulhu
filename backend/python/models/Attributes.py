from sqlalchemy import UUID, Column, Integer, String, Uuid
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class characterSheet(Base):
    __tablename__ = 'attributes'
    id = Column(UUID, primary_key=True, default=Uuid.uuid4, unique=True, nullable=False)
    agility = Column(Integer)
    brawn = Column(Integer)
    coordination = Column(Integer)
    gravitas = Column(Integer)
    insight = Column(Integer)
    reason = Column(Integer)
    will = Column(Integer)