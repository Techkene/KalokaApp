from pydantic import BaseModel, UUID4
from datetime import datetime

class RecommendationBase(BaseModel):
    farm_id: UUID4
    timestamp: datetime
    recommendation_text: str

class RecommendationCreate(RecommendationBase):
    pass

class RecommendationUpdate(RecommendationBase):
    pass

class RecommendationInDBBase(RecommendationBase):
    id: UUID4

    class Config:
        orm_mode = True

class Recommendation(RecommendationInDBBase):
    pass

class RecommendationInDB(RecommendationInDBBase):
    pass
