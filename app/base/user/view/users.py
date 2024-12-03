from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import get_user_repository
from app.base.user.storage.base import UserRepository
from app.base.user.model.user_model import UserCreate, UserUpdate, User

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=User)
async def create_user(
    user_create: UserCreate, repository: UserRepository = Depends(get_user_repository)
):
    return await repository.create_user(user_create)


@router.get("/{user_id}", response_model=User)
async def get_user(
    user_id: int, repository: UserRepository = Depends(get_user_repository)
):
    user = await repository.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=User)
async def update_user(
    user_id: int,
    user_update: UserUpdate,
    repository: UserRepository = Depends(get_user_repository),
):
    user = await repository.update_user(user_id, user_update)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/{user_id}")
async def delete_user(
    user_id: int, repository: UserRepository = Depends(get_user_repository)
):
    success = await repository.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"}
