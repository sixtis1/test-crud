import punq

from app.base.user.storage.base.base import UserRepository
from app.base.user.storage.memory.memory_repository import MemoryUserRepository
from app.base.user.storage.postgres.db_repository import DBUserRepository
from app.config import settings

container = punq.Container()

repository_type = settings.REPOSITORY_TYPE
if repository_type == "postgres":
    container.register(UserRepository, DBUserRepository)
else:
    container.register(UserRepository, MemoryUserRepository)
