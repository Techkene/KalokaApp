from pydantic import BaseModel, UUID4
from datetime import datetime

class FarmDataBase(BaseModel):
    farm_id: UUID4
    timestamp: datetime
    ph_level: float
    water_temperature: float
    water_color: str
    duration_of_change: float
    feed_type: str
    feed_quantity: float

class FarmDataCreate(FarmDataBase):
    pass

class FarmDataUpdate(FarmDataBase):
    pass

class FarmDataInDBBase(FarmDataBase):
    id: UUID4

    class Config:
        orm_mode = True

class FarmData(FarmDataInDBBase):
    pass

class FarmDataInDB(FarmDataInDBBase):
    pass
