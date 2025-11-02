from typing import List
from sqlalchemy import select, func, literal
from sqlalchemy.orm import aliased
from src.models import OrganizationsORM, BuildingsORM, ActivitiesORM
from src.models.organizations_activities import organization_activity
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import OrganizationsDataMapper


class OrganizationsRepository(BaseRepository):
    model = OrganizationsORM
    mapper = OrganizationsDataMapper

    async def get_organizations_in_one_building(self, address: str) -> List[OrganizationsDataMapper]:
        query = (
            select(self.model)
            .join(BuildingsORM, self.model.building_id == BuildingsORM.id)
            .where(BuildingsORM.address == address)
        )
        result = await self.session.execute(query)
        models = result.scalars().all()
        return [self.mapper.map_to_domain_entity(model) for model in models]

    async def get_organizations_with_one_activity(self, activity_name: str) -> List[OrganizationsDataMapper]:
        # Рекурсивный CTE для получения id всех дочерних активностей, начиная с указанной
        base = select(ActivitiesORM.id).where(ActivitiesORM.name == activity_name)

        activities_tree = base.cte(recursive=True, name="activities_tree")
        a = aliased(ActivitiesORM)
        activities_tree = activities_tree.union_all(
            select(a.id).where(a.parent_id == activities_tree.c.id)
        )

        stmt = (
            select(self.model)
            .join(organization_activity, organization_activity.c.organization_id == self.model.id)
            .join(ActivitiesORM, ActivitiesORM.id == organization_activity.c.activity_id)
            .where(ActivitiesORM.id.in_(select(activities_tree.c.id).scalar_subquery()))
            .distinct()
        )

        result = await self.session.execute(stmt)
        models = result.scalars().all()
        return [self.mapper.map_to_domain_entity(model) for model in models]

    async def get_organizations_within_radius(self, longitude: float, latitude: float, radius_km: float) -> List[OrganizationsDataMapper]:
        # фильтр по радиусу в километрах с использованием формулы гаверсинуса на стороне БД
        # радиус земли = 6371 км
        R = 6371
        # Конвертация градусов в радианы прямо в SQL
        lat1 = func.radians(literal(latitude))
        lon1 = func.radians(literal(longitude))
        lat2 = func.radians(BuildingsORM.latitude)
        lon2 = func.radians(BuildingsORM.longitude)

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = func.sin(dlat / 2) * func.sin(dlat / 2) + func.cos(lat1) * func.cos(lat2) * func.sin(dlon / 2) * func.sin(dlon / 2)
        c = 2 * func.atan2(func.sqrt(a), func.sqrt(1 - a))
        distance_km = R * c

        stmt = (
            select(self.model)
            .join(BuildingsORM, self.model.building_id == BuildingsORM.id)
            .where(distance_km <= radius_km)
        )
        result = await self.session.execute(stmt)
        models = result.scalars().all()
        return [self.mapper.map_to_domain_entity(model) for model in models]
