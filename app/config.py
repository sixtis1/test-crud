import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    REPOSITORY_TYPE: str = os.getenv('REPOSITORY_TYPE', 'memory')
    DATABASE_URL: str = os.getenv('DATABASE_URL', 'postgresql+asyncpg://user:password@localhost:5432/test_db')

    class Config:
        env_file = ".env"


settings = Settings()
