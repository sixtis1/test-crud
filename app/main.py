from fastapi import FastAPI

from app.base.place_of_work.place_of_work_initializer import PlaceOfWorkInitializer
from app.base.user.user_initializer import UserInitializer

app = FastAPI(title="User API")


initializers = [UserInitializer(), PlaceOfWorkInitializer()]

# Register routes from initializers
for initializer in initializers:
    initializer.register_routes(app)
