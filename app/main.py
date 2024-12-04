from fastapi import FastAPI

from app.base.user.view.user_api import user_api


app = FastAPI(title="User API")

app.post("/users")(user_api.create_user)
app.get("/users/{user_id}")(user_api.get_user)
app.put("/users/{user_id}")(user_api.update_user)
app.delete("/users/{user_id}")(user_api.delete_user)
