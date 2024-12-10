from typing import Optional
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.base.user.storage.base.base import UserRepository
from app.base.user.model.user_model import UserCreate, UserUpdate, User
from app.base.user.storage.postgres.user_db_model import UserDBModel

class DBUserRepository(UserRepository):
    def __init__(self, session_maker):
        # session_maker is an async_sessionmaker, not a single session
        self.session_maker = session_maker

    async def create_user(self, user_create: UserCreate) -> User:
        async with self.session_maker() as session:
            user_db = UserDBModel(full_name=user_create.full_name)
            session.add(user_db)
            await session.commit()
            await session.refresh(user_db)
            return User.model_validate(user_db)

    async def get_user(self, user_id: int) -> Optional[User]:
        async with self.session_maker() as session:
            result = await session.execute(
                select(UserDBModel).where(UserDBModel.id == user_id)
            )
            user_db = result.scalars().first()
            if user_db:
                return User.model_validate(user_db)
            return None

    async def update_user(self, user_id: int, user_update: UserUpdate) -> Optional[User]:
        async with self.session_maker() as session:
            result = await session.execute(
                select(UserDBModel).where(UserDBModel.id == user_id)
            )
            user_db = result.scalars().first()
            if user_db:
                user_db.full_name = user_update.full_name
                await session.commit()
                await session.refresh(user_db)
                return User.model_validate(user_db)
            return None

    async def delete_user(self, user_id: int) -> bool:
        async with self.session_maker() as session:
            result = await session.execute(
                select(UserDBModel).where(UserDBModel.id == user_id)
            )
            user_db = result.scalars().first()
            if user_db:
                await session.delete(user_db)
                await session.commit()
                return True
            return False
