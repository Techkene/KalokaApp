from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from db.database import Base
import uuid

class Agent(Base):
    __tablename__ = "agent"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    hashed_pin = Column(String, nullable=False)
    cluster_id = Column(Integer, ForeignKey("clusters.id"))
    cluster = relationship("Cluster", back_populates="agent")
