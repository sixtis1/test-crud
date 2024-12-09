from typing import Optional
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.base.place_of_work.storage.postgres.place_of_work_db_model import (
    PlaceOfWorkDBModel,
)
from app.base.place_of_work.storage.base.base import PlaceOfWorkRepository
from app.base.place_of_work.model.place_of_work_model import (
    PlaceOfWorkCreate,
    PlaceOfWorkUpdate,
    PlaceOfWork,
)


class DBPlaceOfWorkRepository(PlaceOfWorkRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_place_of_work(
        self, place_create: PlaceOfWorkCreate
    ) -> PlaceOfWork:
        place_db = PlaceOfWorkDBModel(name=place_create.name)
        self.session.add(place_db)
        await self.session.commit()
        await self.session.refresh(place_db)
        return PlaceOfWork(id=place_db.id, name=place_db.name)

    async def get_place_of_work(self, place_id: int) -> Optional[PlaceOfWork]:
        result = await self.session.execute(
            select(PlaceOfWorkDBModel).where(PlaceOfWorkDBModel.id == place_id)
        )
        place_db = result.scalars().first()
        if place_db:
            return PlaceOfWork(id=place_db.id, name=place_db.name)
        return None

    async def update_place_of_work(
        self, place_id: int, place_update: PlaceOfWorkUpdate
    ) -> Optional[PlaceOfWork]:
        result = await self.session.execute(
            select(PlaceOfWorkDBModel).where(PlaceOfWorkDBModel.id == place_id)
        )
        place_db = result.scalars().first()
        if place_db:
            place_db.name = place_update.name
            await self.session.commit()
            await self.session.refresh(place_db)
            return PlaceOfWork(id=place_db.id, name=place_db.name)
        return None

    async def delete_place_of_work(self, place_id: int) -> bool:
        result = await self.session.execute(
            select(PlaceOfWorkDBModel).where(PlaceOfWorkDBModel.id == place_id)
        )
        place_db = result.scalars().first()
        if place_db:
            await self.session.delete(place_db)
            await self.session.commit()
            return True
        return False
