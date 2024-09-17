from pydantic import BaseModel
from typing import List

class ClusterBase(BaseModel):
    name: str

class ClusterCreate(ClusterBase):
    pass

class ClusterUpdate(ClusterBase):
    pass

class ClusterInDBBase(ClusterBase):
    id: int

    class Config:
        orm_mode = True

class Cluster(ClusterInDBBase):
    members: List['Farmer'] = []
    agent: List['Agent'] = []

class ClusterInDB(ClusterInDBBase):
    pass

from schemas import Farmer, Agent
Cluster.model_rebuild()
