from typing import Optional

from app.base.user.model.user_model import UserCreate, User, UserUpdate
from app.base.user.storage.base.base import UserRepository


class Repository:
    def __init__(self, provider: UserRepository):
        self._provider = provider

    async def create_user(self, user_create: UserCreate) -> User:
        return await self._provider.create_user(user_create)

    async def get_user(self, user_id: int) -> Optional[User]:
        return await self._provider.get_user(user_id)

    async def update_user(
        self, user_id: int, user_update: UserUpdate
    ) -> Optional[User]:
        return await self._provider.update_user(user_id, user_update)

    async def delete_user(self, user_id: int) -> bool:
        return await self._provider.delete_user(user_id)
