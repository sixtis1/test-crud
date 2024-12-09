from pydantic import BaseModel, ConfigDict


class PlaceOfWorkBase(BaseModel):
    name: str


class PlaceOfWorkCreate(PlaceOfWorkBase):
    pass


class PlaceOfWorkUpdate(PlaceOfWorkBase):
    pass


class PlaceOfWork(PlaceOfWorkBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
