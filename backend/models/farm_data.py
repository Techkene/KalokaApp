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
    stock_quantity = Column(Integer)
    feed_type = Column(String)
    mortality_count_morning = Column(Integer)
    mortality_count_evening = Column(Integer)
    feed_quantity_used = Column(Integer)
    any_unusual_obs = Column(String)
    medications_used = Column(String)
