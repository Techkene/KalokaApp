from pydantic import BaseModel
from typing import List

class FarmBase(BaseModel):
    name: str
    location: str
    size: float

class FarmCreate(FarmBase):
    owner_id: str

class FarmUpdate(FarmBase):
    pass

class FarmInDBBase(FarmBase):
    id: str
    owner_id: str

    class Config:
        orm_mode = True

class Farm(FarmInDBBase):
    data_points: List['FarmData'] = []

class FarmInDB(FarmInDBBase):
    pass

from . import FarmData
Farm.model_rebuild()
