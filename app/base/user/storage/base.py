from typing import Optional

from app.base.user.model.user_model import UserCreate, UserUpdate, User


class UserRepository:
    async def create_user(self, user_create: UserCreate) -> User:
        raise NotImplementedError

    async def get_user(self, user_id: int) -> Optional[User]:
        raise NotImplementedError

    async def update_user(
        self, user_id: int, user_update: UserUpdate
    ) -> Optional[User]:
        raise NotImplementedError

    async def delete_user(self, user_id: int) -> bool:
        raise NotImplementedError
