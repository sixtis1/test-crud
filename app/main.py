from fastapi import FastAPI
from app.base.user.container import container
from app.base.user.storage.user_initializer import UserInitializer

from app.base.user.storage.base.base import UserRepository

app = FastAPI(title="User API")

user_repository = container.resolve(UserRepository)
user_initializer = UserInitializer(user_repository)
user_api = user_initializer.user_api

app.post("/users")(user_api.create_user)
app.get("/users/{user_id}")(user_api.get_user)
app.put("/users/{user_id}")(user_api.update_user)
app.delete("/users/{user_id}")(user_api.delete_user)