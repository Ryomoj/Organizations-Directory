from sqlalchemy import Table, Column, ForeignKey

from src.database import Base

# many-to-many для Organization и Activity
organization_activity = Table(
    'organization_activity',
    Base.metadata,

    Column('organization_id', ForeignKey('organizations.id'), primary_key=True),
    Column('activity_id', ForeignKey('activities.id'), primary_key=True)
)