from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.customer import CustomerRepository
from app.db.errors import EntityDoesNotExist
from app.models.domain.customers import Customer
from app.resources import strings

async def get_customer_by_id_from_path(
    customer_id: int,
    customer_repo: CustomerRepository = Depends(get_repository(CustomerRepository)),
) -> Customer:
    try:
        return await customer_repo.get_by_id(id=customer_id)
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.CUSTOMER_DOES_NOT_EXIST_ERROR,
        )
