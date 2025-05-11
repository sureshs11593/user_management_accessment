from pydantic import BaseModel, EmailStr
from uuid import UUID

class UserBase(BaseModel):
    full_name: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    is_active: bool

class UserOut(UserBase):
    id: UUID
    is_active: bool

    class Config:
        orm_mode = True
