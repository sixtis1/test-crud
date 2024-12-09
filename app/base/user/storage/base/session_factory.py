from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.config import DataBaseSettings, database_settings


class SessionFactory:
    def __init__(self):
        self.engine = create_async_engine(
            url=database_settings.DATABASE_URL,
            future=database_settings.DATABASE_FUTURE,
            echo=database_settings.DATABASE_ECHO,
        )
        self.async_sessionmaker = async_sessionmaker(self.engine, expire_on_commit=False)

    def get_session(self):
        return self.async_sessionmaker()