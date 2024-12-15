from pydantic import BaseModel


class UserCreatedEvent(BaseModel):
    user_id: int
    full_name: str
