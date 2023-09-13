from sqlalchemy import UUID, Column, Integer, String, Uuid

from backend.python.models.BaseDatabase import Base

class Attributes(Base):
    __tablename__ = 'attributes'
    id = Column(UUID, primary_key=True, default=Uuid.uuid4, unique=True, nullable=False)
    agility = Column(Integer)
    brawn = Column(Integer)
    coordination = Column(Integer)
    gravitas = Column(Integer)
    insight = Column(Integer)
    reason = Column(Integer)
    will = Column(Integer)