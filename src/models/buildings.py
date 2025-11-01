from sqlalchemy.orm import  Mapped, mapped_column, relationship
from typing import List
from src.database import Base
from src.models.organizations import OrganizationsORM


class BuildingsORM(Base):
    __tablename__ = "buildings"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    address: Mapped[str] = mapped_column(nullable=False, unique=True, index=True)
    latitude: Mapped[float] = mapped_column(nullable=False)
    longitude: Mapped[float] = mapped_column(nullable=False)

    organizations: Mapped[List["OrganizationsORM"]] = relationship(back_populates="building")

