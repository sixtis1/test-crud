from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import settings
from app.dependencies import create_tables
from app.routers import users

@asynccontextmanager
async def lifespan(app: FastAPI):
    if settings.REPOSITORY_TYPE == "db":
        await create_tables()
    yield

app = FastAPI(title="User API", lifespan=lifespan)

app.include_router(users.router)


