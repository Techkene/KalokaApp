from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base
from uuid import uuid4

class Farm(Base):
    __tablename__ = "farms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
    size = Column(Float)
    owner_id = Column(Integer, ForeignKey("farmers.id"))
    owner = relationship("Farmer", back_populates="farm")
    data_points = relationship("FarmData", back_populates="farm")
