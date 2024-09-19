from pydantic import BaseModel, UUID4
from datetime import datetime

class FarmDataBase(BaseModel):
    farm_id: UUID4
    timestamp: datetime
    ph_level: float
    ammonia: float
    dissolved_oxygen: float
    dissolved_solid: float
    temperature: float
    rainfall: float
    weight: float
    feed_size: float
    quantity_of_feed: float

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
