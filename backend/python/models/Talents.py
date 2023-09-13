from sqlalchemy import ARRAY, UUID, Column, Integer, String, Uuid

from backend.python.models.BaseDatabase import Base

class Talents(Base):
    __tablename__ = 'talents'
    id = Column(UUID, primary_key=True, default=Uuid.uuid4, unique=True, nullable=False)
    name = Column(String)
    description = Column(String)