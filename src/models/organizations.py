from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from src.database import Base


class OrganizationsORM(Base):
    __tablename__ = "organizations"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    phone_numbers: Mapped[str]
    building_id: Mapped[int]
    activities: Mapped[int]