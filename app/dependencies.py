from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from app.config import settings
from app.models import Base
from app.repositories.base import UserRepository
from app.repositories.memory_repository import MemoryUserRepository
from app.repositories.db_repository import DBUserRepository

engine = create_async_engine(
    settings.DATABASE_URL,
    future=True,
    echo=True,
)
async_session = async_sessionmaker(engine, expire_on_commit=False)

memory_repository = MemoryUserRepository()


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


async def create_tables() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_user_repository() -> AsyncGenerator[UserRepository, None]:
    if settings.REPOSITORY_TYPE == "memory":
        yield memory_repository
    else:
        async with async_session() as session:
            yield DBUserRepository(session)
