from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from db.database import Base
import uuid

class FarmData(Base):
    __tablename__ = "farm_data"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    farm_id = Column(UUID(as_uuid=True), ForeignKey("farms.id"))
    farm = relationship("Farm", back_populates="data_points")
    timestamp = Column(DateTime)
    ph_level = Column(Float)
    water_temperature = Column(Float)
    water_color = Column(String)
    duration_of_change = Column(Float)
    feed_type = Column(String)
    feed_quantity = Column(Float)
