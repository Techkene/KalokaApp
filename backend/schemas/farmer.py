from typing_extensions import Annotated, Optional
from pydantic import BaseModel, EmailStr, StringConstraints, UUID4

class FarmerBase(BaseModel):
    username: str
    email: EmailStr
    phone_number: str
    is_independent: bool = False

class FarmerLogin(BaseModel):
    username: str
    password: str

class FarmerCreate(FarmerBase):
    password: str
    pin: Annotated[
                    str,
                    StringConstraints(min_length=4, max_length=4)
                ]

class FarmerUpdate(FarmerBase):
    password: Optional[str] = None
    pin: Optional[
            Annotated[
                    str,
                    StringConstraints(min_length=4, max_length=4)
                ]
        ] = None

class FarmerInDBBase(FarmerBase):
    id: UUID4

    class Config:
        orm_mode = True

class Farmer(FarmerInDBBase):
    pass

class FarmerInDB(FarmerInDBBase):
    hashed_password: str
    hashed_pin: str
