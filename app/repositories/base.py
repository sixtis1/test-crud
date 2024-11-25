from abc import ABC, abstractmethod
from typing import List, Optional

from app.schemas import UserCreate, UserUpdate, User


class UserRepository(ABC):
    @abstractmethod
    async def create_user(self, user_create: UserCreate) -> User:
        pass

    @abstractmethod
    async def get_user(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    async def update_user(self, user_id: int, user_update: UserUpdate) -> Optional[User]:
        pass

    @abstractmethod
    async def delete_user(self, user_id: int) -> bool:
        pass
