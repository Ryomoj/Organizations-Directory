from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import ARRAY
from typing import List, Optional
from src.database import Base
from src.models import *
from src.models.organizations_activities import organization_activity


class OrganizationsORM(Base):
    __tablename__ = "organizations"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False, index=True)
    phone_numbers: Mapped[Optional[List[str]]] = mapped_column(ARRAY(String))

    building_id: Mapped[int] = mapped_column(ForeignKey('buildings.id'), nullable=False)

    building: Mapped["BuildingsORM"] = relationship(back_populates="organizations")
    activities: Mapped[List["ActivitiesORM"]] = relationship(
        secondary=organization_activity,
        back_populates="organizations"
    )