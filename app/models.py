from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, declarative_base

Base = declarative_base()


class UserDBModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(30))

