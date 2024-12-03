from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.base.user.storage.postgres.user_db_model import UserDBModel
from app.base.user.storage.base import UserRepository
from app.base.user.model.user_model import UserCreate, UserUpdate, User


class DBUserRepository(UserRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(self, user_create: UserCreate) -> User:
        user_db = UserDBModel(full_name=user_create.full_name)
        self.session.add(user_db)
        await self.session.commit()
        await self.session.refresh(user_db)
        return User.model_validate(user_db)

    async def get_user(self, user_id: int) -> Optional[User]:
        result = await self.session.execute(
            select(UserDBModel).where(UserDBModel.id == user_id)
        )
        user_db = result.scalars().first()
        if user_db:
            return User.model_validate(user_db)
        return None

    async def update_user(
        self, user_id: int, user_update: UserUpdate
    ) -> Optional[User]:
        result = await self.session.execute(
            select(UserDBModel).where(UserDBModel.id == user_id)
        )
        user_db = result.scalars().first()
        if user_db:
            user_db.full_name = user_update.full_name
            await self.session.commit()
            await self.session.refresh(user_db)
            return User.model_validate(user_db)
        return None

    async def delete_user(self, user_id: int) -> bool:
        result = await self.session.execute(
            select(UserDBModel).where(UserDBModel.id == user_id)
        )
        user_db = result.scalars().first()
        if user_db:
            await self.session.delete(user_db)
            await self.session.commit()
            return True
        return False
