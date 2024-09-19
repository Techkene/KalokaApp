from pydantic import BaseModel, UUID4
from typing import List

class FarmBase(BaseModel):
    name: str
    location: str
    size: float

class FarmCreate(FarmBase):
    owner_id: UUID4

class FarmUpdate(FarmBase):
    pass

class FarmInDBBase(FarmBase):
    id: UUID4
    owner_id: UUID4

    class Config:
        orm_mode = True

class Farm(FarmInDBBase):
    data_points: List['FarmData'] = []

class FarmInDB(FarmInDBBase):
    pass

from . import FarmData
Farm.model_rebuild()
