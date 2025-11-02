from src.repositories.mappers.base import DataMapper
from src.models import *
from src.schemas import *


class OrganizationsDataMapper(DataMapper):
    db_model = OrganizationsORM
    schema = OrganizationsSchema


class BuildingsDataMapper(DataMapper):
    db_model = BuildingsORM
    schema = BuildingsSchema


class ActivitiesDataMapper(DataMapper):
    db_model = ActivitiesORM
    schema = ActivitiesSchema

