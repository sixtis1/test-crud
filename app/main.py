from fastapi import FastAPI
from app.base.user.user_initializer import UserInitializer

app = FastAPI(title="User API")

initializers = [
    UserInitializer(),
]

# Register routes from initializers
for initializer in initializers:
    initializer.register_routes(app)