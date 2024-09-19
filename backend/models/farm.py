from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Farm(Base):
    __tablename__ = "farms"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, index=True)
    location = Column(String)
    size = Column(Float)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("farmers.id"))
    owner = relationship("Farmer", back_populates="farm")
    data_points = relationship("FarmData", back_populates="farm")
