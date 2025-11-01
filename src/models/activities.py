from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional
from src.database import Base
from src.models.organizations import OrganizationsORM
from src.models.organizations_activities import organization_activity


class ActivitiesORM(Base):
    __tablename__ = "activities"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    parent_id: Mapped[Optional[int]] = mapped_column(ForeignKey('activities.id'), nullable=True)

    parent: Mapped[Optional["ActivitiesORM"]] = relationship(
        remote_side=[id],
        back_populates="children"
    )
    children: Mapped[List["ActivitiesORM"]] = relationship(back_populates="parent")

    organizations: Mapped[List["OrganizationsORM"]] = relationship(
        secondary=organization_activity,
        back_populates="activities"
    )
