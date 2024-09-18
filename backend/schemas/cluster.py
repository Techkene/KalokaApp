from pydantic import BaseModel
from typing import List

class ClusterBase(BaseModel):
    name: str

class ClusterCreate(ClusterBase):
    pass

class ClusterUpdate(ClusterBase):
    pass

class ClusterInDBBase(ClusterBase):
    id: str

    class Config:
        orm_mode = True

class Cluster(ClusterInDBBase):
    members: List['Farmer'] = []

class ClusterInDB(ClusterInDBBase):
    pass

from . import Farmer
Cluster.model_rebuild()
