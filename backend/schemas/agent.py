from typing_extensions import Annotated, Optional
from pydantic import BaseModel, EmailStr, StringConstraints

class AgentBase(BaseModel):
    username: str
    email: EmailStr
    phone_number: str

class AgentCreate(AgentBase):
    password: str
    cluster_id: int
    pin: Annotated[
                str,
                StringConstraints(min_length=4, max_length=4)
            ]

class AgentUpdate(AgentBase):
    password: Optional[str] = None
    pin: Optional[
            Annotated[
                    str,
                    StringConstraints(min_length=4, max_length=4)
                ]
        ] = None

class AgentInDBBase(AgentBase):
    id: int
    cluster_id: int

    class Config:
        orm_mode = True

class Agent(AgentInDBBase):
    pass

class AgentInDB(AgentInDBBase):
    hashed_password: str
    hashed_pin: str
