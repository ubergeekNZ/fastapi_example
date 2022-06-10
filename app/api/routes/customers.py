from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.customer import CustomerRepository
from app.db.errors import EntityDoesNotExist
from app.models.schemas.customers import (
    ListOfCustomersInResponse
)
from app.resources import strings

router = APIRouter()

# @router.get(
#     "",
#     response_model=ListOfCommentsInResponse,
#     name="comments:get-comments-for-article",
# )
# @router.get("/", status_code=200) 
# async def root():
#     return {"message": "Hello World"}

@router.get("", response_model=ListOfCustomersInResponse, name="customers:get-all")
async def get_all(
    customer_repo: CustomerRepository = Depends(get_repository(CustomerRepository)),
) -> ListOfCustomersInResponse:
    records = await customer_repo.get_all()
    print(records)
    return ListOfCustomersInResponse(customers=records)