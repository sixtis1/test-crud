from app.base.place_of_work.storage.base.base import PlaceOfWorkRepository
from app.base.place_of_work.model.place_of_work_model import (
    PlaceOfWorkCreate,
    PlaceOfWorkUpdate,
)


class PlaceOfWorkAPI:
    def __init__(self, repository: PlaceOfWorkRepository):
        self.repository = repository

    async def create_place_of_work(self, place_create: PlaceOfWorkCreate):
        return await self.repository.create_place_of_work(place_create)

    async def get_place_of_work(self, place_id: int):
        place = await self.repository.get_place_of_work(place_id)
        if place:
            return place
        return {"error": "Place of Work not found"}

    async def update_place_of_work(
        self, place_id: int, place_update: PlaceOfWorkUpdate
    ):
        place = await self.repository.update_place_of_work(place_id, place_update)
        if place:
            return place
        return {"error": "Place of Work not found"}

    async def delete_place_of_work(self, place_id: int):
        success = await self.repository.delete_place_of_work(place_id)
        if success:
            return {"message": "Place of Work deleted"}
        return {"error": "Place of Work not found"}
