from typing import Dict, Optional

from app.base.user.storage.base import UserRepository
from app.base.user.model.user_model import UserCreate, UserUpdate, User


class MemoryUserRepository(UserRepository):
    def __init__(self):
        self.users: Dict[int, User] = {}
        self.current_id: int = 1

    async def create_user(self, user_create: UserCreate) -> User:
        user = User(id=self.current_id, full_name=user_create.full_name)
        self.users[self.current_id] = user
        self.current_id += 1
        return user

    async def get_user(self, user_id: int) -> Optional[User]:
        return self.users.get(user_id)

    async def update_user(
        self, user_id: int, user_update: UserUpdate
    ) -> Optional[User]:
        user = self.users.get(user_id)
        if user:
            updated_user = User(id=user_id, full_name=user_update.full_name)
            self.users[user_id] = updated_user
            return updated_user
        return None

    async def delete_user(self, user_id: int) -> bool:
        return self.users.pop(user_id, None) is not None
