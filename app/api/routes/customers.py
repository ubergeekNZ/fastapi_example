from fastapi import APIRouter, Depends, HTTPException, Query, Response, Body
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.customer import CustomerRepository
from app.db.errors import EntityDoesNotExist
from app.models.domain.customers import Customer
from app.models.schemas.customers import (
    ListOfCustomersInResponse,
    CustomerInCreate,
    CustomerInResponse,
    CustomerInUpdate,
    DEFAULT_CUSTOMERS_LIMIT,
    DEFAULT_CUSTOMERS_OFFSET
)
from app.resources import strings
from app.api.dependencies.customer import (
    get_customer_by_id_from_path
)

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


@router.get("/{customer_id}", response_model=CustomerInResponse, name="customers:get-by-id")
async def get_by_id(
    customer: Customer = Depends(get_customer_by_id_from_path),
) -> CustomerInResponse:
    return CustomerInResponse(customer=customer)


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=CustomerInResponse,
    name="customers:create-customer",
)
async def create_customer(
    customer_create: CustomerInCreate = Body(..., embed=True, alias="customer"),
    customer_repo: CustomerRepository = Depends(get_repository(CustomerRepository)),
) -> CustomerInResponse:
    customer = await customer_repo.create_customer(customer_create.customer)
    return CustomerInResponse(customer=customer)


@router.delete(
    "/{customer_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    name="customers:delete-customer",
    response_class=Response,
)
async def delete_comment_from_article(
    customer: Customer = Depends(get_customer_by_id_from_path),
    customer_repo: CustomerRepository = Depends(get_repository(CustomerRepository)),
) -> None:
    await customer_repo.delete(data=customer)

@router.put("", response_model=CustomerInResponse, name="customers:update-customer")
async def update_customer(
    customer_update: CustomerInUpdate = Body(..., embed=True, alias="customer"),
    customer_repo: CustomerRepository = Depends(get_repository(CustomerRepository)),
) -> CustomerInResponse:
    await customer_repo.update(data=customer_update.customer)
    return CustomerInResponse(customer=customer_update.customer)