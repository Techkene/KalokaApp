from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Optional

class FarmDataBase(BaseModel):
    stock_qty: Optional[str] = None
    feed_type: Optional[str] = None
    morning_mortality: Optional[str] = None
    evening_mortality: Optional[str] = None
    feed_qty: Optional[str] = None
    unusual_observation: Optional[str] = None
    medication_used: Optional[str] = None

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
