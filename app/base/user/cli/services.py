from app.base.user.model.user_model import UserCreate, UserUpdate
from app.base.user.storage.base.base import UserRepository
from app.container import container

async def create_user_service(full_name: str) -> str:
    user_repository: UserRepository = container.resolve(UserRepository)
    user = await user_repository.create_user(UserCreate(full_name=full_name))
    return f"User created: ID={user.id}, FullName={user.full_name}"

async def get_user_service(user_id: int) -> str:
    user_repository: UserRepository = container.resolve(UserRepository)
    user = await user_repository.get_user(user_id)
    if user:
        return f"User found: ID={user.id}, FullName={user.full_name}"
    return "User not found"

async def update_user_service(user_id: int, full_name: str) -> str:
    user_repository: UserRepository = container.resolve(UserRepository)
    updated_user = await user_repository.update_user(user_id, UserUpdate(full_name=full_name))
    if updated_user:
        return f"User updated: ID={updated_user.id}, FullName={updated_user.full_name}"
    return "User not found"

async def delete_user_service(user_id: int) -> str:
    user_repository: UserRepository = container.resolve(UserRepository)
    success = await user_repository.delete_user(user_id)
    if success:
        return "User deleted"
    return "User not found"
