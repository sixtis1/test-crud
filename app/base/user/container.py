import punq
from app.base.user.storage.base.base import UserRepository
from app.base.user.storage.memory.memory_repository import MemoryUserRepository
from app.base.user.storage.postgres.db_repository import DBUserRepository
from app.config import settings
from app.base.user.storage.base.session_factory import SessionFactory

container = punq.Container()

repository_type = settings.REPOSITORY_TYPE

if repository_type == "postgres":
    session_factory = SessionFactory()
    container.register(SessionFactory, instance=session_factory)
    container.register(UserRepository, factory=lambda: DBUserRepository(session_factory.get_session()))
else:
    container.register(UserRepository, MemoryUserRepository)
