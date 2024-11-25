import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv(dotenv_path="app/.env")

class Settings(BaseSettings):
    REPOSITORY_TYPE: str
    DATABASE_URL: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    class Config:
        env_file = "app/.env"
        env_file_encoding = "utf-8"
        extra = "ignore"

settings = Settings()
