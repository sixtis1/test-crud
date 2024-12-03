from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
    AsyncEngine,
)

from app.config import settings
from app.base.user.storage.postgres.user_db_model import Base
from app.base.user.storage.base import UserRepository
from app.base.user.storage.memory.memory_repository import MemoryUserRepository
from app.base.user.storage.postgres.db_repository import DBUserRepository


async def get_engine() -> AsyncEngine:
    engine = create_async_engine(
        settings.DATABASE_URL,
        future=True,
        echo=True,
    )
    return engine


async def get_async_session() -> AsyncSession:
    async_session = async_sessionmaker(get_engine(), expire_on_commit=False)
    return async_session


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with get_async_session() as session:
        yield session


async def create_tables() -> None:
    async with get_engine().begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_user_repository() -> AsyncGenerator[UserRepository, None]:
    if settings.REPOSITORY_TYPE == "memory":
        memory_repository = MemoryUserRepository()
        yield memory_repository
    else:
        async with get_async_session() as session:
            yield DBUserRepository(session)
