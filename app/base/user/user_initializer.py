from fastapi import FastAPI

from app.container import container
from app.base.user.storage.base.base import UserRepository
from app.base.user.view.user_api import UserAPI

class UserInitializer:
    def __init__(self):
        self.user_repository = container.resolve(UserRepository)
        self.user_api = UserAPI(self.user_repository)

    def register_routes(self, app: FastAPI):
        app.post("/users")(self.user_api.create_user)
        app.get("/users/{user_id}")(self.user_api.get_user)
        app.put("/users/{user_id}")(self.user_api.update_user)
        app.delete("/users/{user_id}")(self.user_api.delete_user)