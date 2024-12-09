from typing import Optional
from app.base.place_of_work.model.place_of_work_model import (
    PlaceOfWorkCreate,
    PlaceOfWorkUpdate,
    PlaceOfWork,
)


class PlaceOfWorkRepository:
    async def create_place_of_work(
        self, place_create: PlaceOfWorkCreate
    ) -> PlaceOfWork:
        raise NotImplementedError

    async def get_place_of_work(self, place_id: int) -> Optional[PlaceOfWork]:
        raise NotImplementedError

    async def update_place_of_work(
        self, place_id: int, place_update: PlaceOfWorkUpdate
    ) -> Optional[PlaceOfWork]:
        raise NotImplementedError

    async def delete_place_of_work(self, place_id: int) -> bool:
        raise NotImplementedError
