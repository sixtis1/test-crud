from pydantic import BaseModel


class UserBase(BaseModel):
    full_name: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        from_attributes = True
