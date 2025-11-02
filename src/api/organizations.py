from fastapi import APIRouter, Query

from src.api.dependencies import DatabaseDep
from src.services.organizations import OrganizationsService

router = APIRouter(prefix="/organizations", tags=["Организации"])

@router.get("/name/{organization_name}", summary="Поиск организаций по названию")
async def get_organization_by_name(
        db: DatabaseDep,
        organization_name: str
):
    organization = await OrganizationsService(db).get_organization_by_name(organization_name=organization_name)
    return {"Status": "OK", "data": organization}



@router.get("/id/{organization_id}", summary="Поиск организаций по идентификатору")
async def get_organization_by_id(
        db: DatabaseDep,
        organization_id: int
):
    organization = await OrganizationsService(db).get_organization_by_id(organization_id=organization_id)
    return {"Status": "OK", "data": organization}


@router.get("/address/{address}", summary="Поиск организаций по адресу")
async def get_one_building_organizations(
        db: DatabaseDep,
        address: str
):
    organizations = await OrganizationsService(db).get_one_building_organizations(address=address)
    return {"Status": "OK", "data": organizations}


@router.get("/activity_name/{activity_name}", summary="Поиск организаций по наименованию вида деятельности")
async def get_one_activity_organizations(
        db: DatabaseDep,
        activity_name: str
):
    organizations = await OrganizationsService(db).get_one_activity_organizations(activity_name=activity_name)
    return {"Status": "OK", "data": organizations}

@router.get("/geolocation}", summary="Поиск организаций по точке на карте")
async def get_organizations_by_point_on_map(
        db: DatabaseDep,
        longitude: float = Query(),
        latitude: float = Query(),
        radius_km: float = Query(1)
):
    organizations = await OrganizationsService(db).get_organizations_by_point_on_map(
        longitude=longitude,
        latitude=latitude,
        radius_km=radius_km
    )
    return organizations
