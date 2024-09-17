from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from models import Base
from uuid import uuid4

class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(Integer, primary_key=True, index=True)
    farm_id = Column(Integer, ForeignKey("farms.id"))
    timestamp = Column(DateTime)
    recommendation_text = Column(String)
