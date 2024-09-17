from pydantic import BaseModel
from datetime import datetime

class RecommendationBase(BaseModel):
    farm_id: int
    timestamp: datetime
    recommendation_text: str

class RecommendationCreate(RecommendationBase):
    pass

class RecommendationUpdate(RecommendationBase):
    pass

class RecommendationInDBBase(RecommendationBase):
    id: int

    class Config:
        orm_mode = True

class Recommendation(RecommendationInDBBase):
    pass

class RecommendationInDB(RecommendationInDBBase):
    pass
