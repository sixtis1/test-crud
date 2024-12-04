from app.base.user.container import container
from app.base.user.model.user_model import UserUpdate, UserCreate
from app.base.user.storage.base.base import UserRepository
from app.base.user.storage.base.repository import Repository


class UserAPI:
    def __init__(self, repository: Repository):
        self.repository = repository

    async def create_user(self, user_create: UserCreate):
        return await self.repository.create_user(user_create)

    async def get_user(self, user_id: int):
        user = await self.repository.get_user(user_id)
        if user:
            return user
        return {"error": "User not found"}

    async def update_user(self, user_id: int, user_update: UserUpdate):
        user = await self.repository.update_user(user_id, user_update)
        if user:
            return user
        return {"error": "User not found"}

    async def delete_user(self, user_id: int):
        success = await self.repository.delete_user(user_id)
        if success:
            return {"message": "User deleted"}
        return {"error": "User not found"}


repo_provider = container.resolve(UserRepository)
repository_instance = Repository(repo_provider)
user_api = UserAPI(repository_instance)
