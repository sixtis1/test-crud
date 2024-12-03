from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(dotenv_path="app/.env")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="app/.env", env_file_encoding="utf-8", extra="ignore"
    )

    REPOSITORY_TYPE: str
    DATABASE_URL: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str


settings = Settings()
