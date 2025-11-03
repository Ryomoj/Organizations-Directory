from typing import Dict, Sequence, Type

from pydantic import BaseModel

from src.database import async_session_maker
from src.repositories.organizations import OrganizationsRepository


async def insert_test_data_2_db(repo_class, session, data: Dict[str, Sequence[BaseModel]]):
    if not isinstance(data, dict):
        raise TypeError("data must be a dict[str, Sequence[BaseModel]]")

    repo = repo_class(session)

    for _, items in data.items():
        if not items:
            continue
        # Ensure the items are Pydantic models with model_dump available
        for item in items:
            if not isinstance(item, BaseModel):
                raise TypeError("All items must be instances of pydantic.BaseModel")
        await repo.add_bulk(items)

    # One commit for all batches (caller may also manage transactions; adjust as needed)
    await session.commit()


insert_test_data_2_db(OrganizationsRepository, async_session_maker, ...)