from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.config import database_settings


class SessionFactory:
    def __init__(self):
        self.engine = create_async_engine(
            database_settings.DATABASE_URL,
            future=database_settings.DATABASE_FUTURE,
            echo=database_settings.DATABASE_ECHO,
        )
        self.session_maker = async_sessionmaker(self.engine, expire_on_commit=False)

    def get_session_maker(self):
        return self.session_maker
