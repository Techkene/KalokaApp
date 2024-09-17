from pydantic import BaseModel, EmailStr

class FarmerBase(BaseModel):
    username: str
    email: EmailStr
    is_independent: bool = False

class FarmerCreate(FarmerBase):
    password: str

class FarmerUpdate(FarmerBase):
    password: str | None = None

class FarmerInDBBase(FarmerBase):
    id: int
    cluster_id: int | None = None

    class Config:
        orm_mode = True

class Farmer(FarmerInDBBase):
    pass

class FarmerInDB(FarmerInDBBase):
    hashed_password: str
