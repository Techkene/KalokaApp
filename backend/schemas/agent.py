from pydantic import BaseModel, EmailStr

class AgentBase(BaseModel):
    username: str
    email: EmailStr

class AgentCreate(AgentBase):
    password: str
    cluster_id: int

class AgentUpdate(AgentBase):
    password: str | None = None

class AgentInDBBase(AgentBase):
    id: int
    cluster_id: int

    class Config:
        orm_mode = True

class Agent(AgentInDBBase):
    pass

class AgentInDB(AgentInDBBase):
    hashed_password: str
