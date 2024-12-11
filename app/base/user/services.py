from app.base.user.model.user_model import UserCreate, UserUpdate
from app.base.user.storage.base.base import UserRepository
from app.base.user.event.publisher import EventPublisher
from app.base.user.event.events import UserCreatedEvent


class UserService:
    def __init__(
        self, user_repository: UserRepository, event_publisher: EventPublisher
    ):
        self.user_repository = user_repository
        self.event_publisher = event_publisher

    async def create_user(self, full_name: str) -> str:
        user = await self.user_repository.create_user(UserCreate(full_name=full_name))
        event = UserCreatedEvent(user_id=user.id, full_name=user.full_name)
        await self.event_publisher.publish(event)
        return f"User created: ID={user.id}, FullName={user.full_name}"

    async def get_user(self, user_id: int) -> str:
        user = await self.user_repository.get_user(user_id)
        if user:
            return f"User found: ID={user.id}, FullName={user.full_name}"
        return "User not found"

    async def update_user(self, user_id: int, full_name: str) -> str:
        updated_user = await self.user_repository.update_user(
            user_id, UserUpdate(full_name=full_name)
        )
        if updated_user:
            return (
                f"User updated: ID={updated_user.id}, FullName={updated_user.full_name}"
            )
        return "User not found"

    async def delete_user(self, user_id: int) -> str:
        success = await self.user_repository.delete_user(user_id)
        return "User deleted" if success else "User not found"
