from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from src.database import Base


class WorkTypesORM(Base):
    __tablename__ = "workTypes"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    work_id: Mapped[int]
    workSubtypes_ids: Mapped[int]