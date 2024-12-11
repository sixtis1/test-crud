from fastapi import HTTPException
from app.base.user.model.user_model import UserUpdate, UserCreate
from app.base.user.services import UserService


class UserAPI:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    async def create_user(self, user_create: UserCreate):
        message = await self.user_service.create_user(user_create.full_name)
        return {"message": message}

    async def get_user(self, user_id: int):
        result = await self.user_service.get_user(user_id)
        if "User found" in result:
            parts = result.split(", ")
            user_id_part = parts[0]
            full_name_part = parts[1]
            user_id = int(user_id_part.split(": ")[1])
            full_name = full_name_part.split(": ")[1]
            return {"id": user_id, "full_name": full_name}
        raise HTTPException(status_code=404, detail="User not found")

    async def update_user(self, user_id: int, user_update: UserUpdate):
        result = await self.user_service.update_user(user_id, user_update.full_name)
        if "User updated" in result:
            parts = result.split(", ")
            user_id_part = parts[0]
            full_name_part = parts[1]
            user_id = int(user_id_part.split(": ")[1])
            full_name = full_name_part.split(": ")[1]
            return {"id": user_id, "full_name": full_name}
        raise HTTPException(status_code=404, detail="User not found")

    async def delete_user(self, user_id: int):
        result = await self.user_service.delete_user(user_id)
        if result == "User deleted":
            return {"detail": "User deleted successfully"}
        raise HTTPException(status_code=404, detail="User not found")
