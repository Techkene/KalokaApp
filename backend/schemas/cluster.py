from pydantic import BaseModel, UUID4
from typing import List

class ClusterBase(BaseModel):
    name: str

class ClusterCreate(ClusterBase):
    pass

class ClusterUpdate(ClusterBase):
    pass

class ClusterInDBBase(ClusterBase):
    id: UUID4

    class Config:
        orm_mode = True

class Cluster(ClusterInDBBase):
    pass

class ClusterInDB(ClusterInDBBase):
    pass
