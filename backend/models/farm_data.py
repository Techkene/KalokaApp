from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from db.database import Base
import uuid

class FarmData(Base):
    __tablename__ = "farm_data"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    stock_qty = Column(String)
    feed_type = Column(String)
    morning_mortality = Column(String)
    evening_mortality = Column(String)
    feed_qty = Column(String)
    unusual_observation = Column(String)
    medication_used = Column(String)
