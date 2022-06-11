from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.customer import CustomerRepository
from app.db.errors import EntityDoesNotExist
from app.models.schemas.customers import (
    ListOfCustomersInResponse,
    DEFAULT_CUSTOMERS_LIMIT,
    DEFAULT_CUSTOMERS_OFFSET
)
from app.resources import strings

router = APIRouter()

@router.get("", response_model=ListOfCustomersInResponse, name="customers:get-all")
async def get_all(
    limit: int = Query(DEFAULT_CUSTOMERS_LIMIT, ge=1),
    offset: int = Query(DEFAULT_CUSTOMERS_OFFSET, ge=0),
    customer_repo: CustomerRepository = Depends(get_repository(CustomerRepository)),
) -> ListOfCustomersInResponse:
    records = await customer_repo.get_all(limit=limit, offset=offset)
    print(records)
    return ListOfCustomersInResponse(customers=records)