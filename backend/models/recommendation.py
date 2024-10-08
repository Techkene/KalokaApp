from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from db.database import Base
import uuid

class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    farm_id = Column(UUID(as_uuid=True), ForeignKey("farms.id"))
    timestamp = Column(DateTime)
    recommendation_text = Column(String)
