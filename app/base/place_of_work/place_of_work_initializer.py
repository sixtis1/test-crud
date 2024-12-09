from fastapi import FastAPI
from app.base.place_of_work.storage.base.base import PlaceOfWorkRepository
from app.base.place_of_work.view.place_of_work_api import PlaceOfWorkAPI
from app.container import container


class PlaceOfWorkInitializer:
    def __init__(self):
        self.place_repository = container.resolve(PlaceOfWorkRepository)
        self.place_api = PlaceOfWorkAPI(self.place_repository)

    def register_routes(self, app: FastAPI):
        app.post("/places", tags=["Post Methods"])(self.place_api.create_place_of_work)
        app.get("/places/{place_id}", tags=["Get Methods"])(
            self.place_api.get_place_of_work
        )
        app.put("/places/{place_id}", tags=["Put Methods"])(
            self.place_api.update_place_of_work
        )
        app.delete("/places/{place_id}", tags=["Delete Methods"])(
            self.place_api.delete_place_of_work
        )
