from pydantic import BaseModel, UUID4
from datetime import datetime

class FarmDataBase(BaseModel):
    farm_id: UUID4
    timestamp: datetime
    stock_quantity: int
    feed_type: str
    mortality_count_morning: str
    mortality_count_evening: str
    feed_quantity: str
    observation: str
    medication_used: str

class FarmDataUse(BaseModel):
    stock_quantity: int
    feed_type: str
    mortality_count_morning: str
    mortality_count_evening: str
    feed_quantity: str
    observation: str
    medication_used: str

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
