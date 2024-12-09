from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

Base = declarative_base()


class PlaceOfWorkDBModel(Base):
    __tablename__ = "places_of_work"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
