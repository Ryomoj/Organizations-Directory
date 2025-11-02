from src.services.base import BaseService


class OrganizationsService(BaseService):
    async def get_organization_by_name(
            self,
            organization_name: str
    ):
        model = await self.db.organizations.get_one_or_none(name=organization_name)
        return model


    async def get_organization_by_id(
            self,
            organization_id: int
    ):
        model = await self.db.organizations.get_one_or_none(id=organization_id)
        return model


    async def get_one_building_organizations(
            self,
            address: str
    ):
        return await self.db.organizations.get_organizations_in_one_building(address=address)

    async def get_one_activity_organizations(
            self,
            activity_name: str
    ):
        return await self.db.organizations.get_organizations_with_one_activity(activity_name=activity_name)

    async def get_organizations_by_point_on_map(
            self,
            longitude: float,
            latitude: float,
            radius_km: float
    ):
        return await self.db.organizations.get_organizations_within_radius(
            longitude=longitude,
            latitude=latitude,
            radius_km=radius_km
        )
