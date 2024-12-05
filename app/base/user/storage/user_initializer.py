from app.base.user.storage.base.base import UserRepository
from app.base.user.view.user_api import UserAPI

class UserInitializer:
    def __init__(self, repository: UserRepository):
        self.user_api = UserAPI(repository)
