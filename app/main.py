from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.dependencies import engine
from app.models import Base
from app.routers import users


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app = FastAPI(title="User API")

app.include_router(users.router)

