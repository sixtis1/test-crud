import punq

from app.base.place_of_work.storage.base.base import PlaceOfWorkRepository
from app.base.place_of_work.storage.memory.memory_repository import (
    MemoryPlaceOfWorkRepository,
)
from app.base.place_of_work.storage.postgres.db_repository import (
    DBPlaceOfWorkRepository,
)
from app.base.user.storage.base.base import UserRepository
from app.base.user.storage.memory.memory_repository import MemoryUserRepository
from app.base.user.storage.postgres.db_repository import DBUserRepository
from app.config import app_settings
from app.base.user.storage.base.session_factory import SessionFactory

container = punq.Container()

repository_type = app_settings.REPOSITORY_TYPE

if repository_type == "postgres":
    session_factory = SessionFactory()
    container.register(SessionFactory, instance=session_factory)

    container.register(
        UserRepository, factory=lambda: DBUserRepository(session_factory.get_session())
    )
    container.register(
        PlaceOfWorkRepository,
        factory=lambda: DBPlaceOfWorkRepository(session_factory.get_session()),
    )
else:
    container.register(UserRepository, MemoryUserRepository)
    container.register(PlaceOfWorkRepository, MemoryPlaceOfWorkRepository)
