from pydantic import BaseModel, UUID4
from typing import List

class FarmBase(BaseModel):
    name: str
    location: str
    size: float

class FarmCreate(FarmBase):
    pass

class FarmUpdate(FarmBase):
    pass

class FarmInDBBase(FarmBase):
    id: UUID4

    class Config:
        orm_mode = True

class Farm(FarmInDBBase):
    pass

class FarmInDB(FarmInDBBase):
    pass
