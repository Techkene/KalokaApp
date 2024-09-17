from pydantic import BaseModel
from typing import List

class FarmBase(BaseModel):
    name: str
    location: str
    size: float

class FarmCreate(FarmBase):
    owner_id: int

class FarmUpdate(FarmBase):
    pass

class FarmInDBBase(FarmBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class Farm(FarmInDBBase):
    data_points: List['FarmData'] = []

class FarmInDB(FarmInDBBase):
    pass

from .farm_data import FarmData
Farm.update_forward_refs()
