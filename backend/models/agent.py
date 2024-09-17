from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models import Base
from uuid import uuid4

class Agent(Base):
    __tablename__ = "agent"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    cluster_id = Column(Integer, ForeignKey("clusters.id"))
    cluster = relationship("Cluster", back_populates="agent")
