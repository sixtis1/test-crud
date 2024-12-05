from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.config import settings

class SessionFactory:
    def __init__(self):
        self.database_url = settings.DATABASE_URL
        self.engine = create_async_engine(
            self.database_url,
            future=True,
            echo=True,
        )
        self.async_sessionmaker = async_sessionmaker(self.engine, expire_on_commit=False)

    def get_session(self):
        return self.async_sessionmaker()
    