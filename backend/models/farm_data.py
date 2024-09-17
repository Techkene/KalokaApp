from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base
from uuid import uuid4

class FarmData(Base):
    __tablename__ = "farm_data"

    id = Column(Integer, primary_key=True, index=True)
    farm_id = Column(Integer, ForeignKey("farms.id"))
    farm = relationship("Farm", back_populates="data_points")
    agent_id = Column(Integer, ForeignKey("agent.id"), nullable=True)
    agent = relationship("Agent")
    timestamp = Column(DateTime)
    ph_level = Column(Float)
    water_temperature = Column(Float)
    water_color = Column(String)
    duration_of_change = Column(Float)
    feed_type = Column(String)
    feed_quantity = Column(Float)
