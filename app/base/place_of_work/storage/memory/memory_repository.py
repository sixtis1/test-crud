from typing import Dict, Optional
from app.base.place_of_work.storage.base.base import PlaceOfWorkRepository
from app.base.place_of_work.model.place_of_work_model import (
    PlaceOfWorkCreate,
    PlaceOfWorkUpdate,
    PlaceOfWork,
)


class MemoryPlaceOfWorkRepository(PlaceOfWorkRepository):
    def __init__(self):
        self._places: Dict[int, PlaceOfWork] = {}
        self._current_id = 1

    async def create_place_of_work(
        self, place_create: PlaceOfWorkCreate
    ) -> PlaceOfWork:
        place = PlaceOfWork(id=self._current_id, name=place_create.name)
        self._places[self._current_id] = place
        self._current_id += 1
        return place

    async def get_place_of_work(self, place_id: int) -> Optional[PlaceOfWork]:
        return self._places.get(place_id)

    async def update_place_of_work(
        self, place_id: int, place_update: PlaceOfWorkUpdate
    ) -> Optional[PlaceOfWork]:
        place = self._places.get(place_id)
        if place:
            updated_place = PlaceOfWork(id=place_id, name=place_update.name)
            self._places[place_id] = updated_place
            return updated_place
        return None

    async def delete_place_of_work(self, place_id: int) -> bool:
        return self._places.pop(place_id, None) is not None
