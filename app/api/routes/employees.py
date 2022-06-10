from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.employee import EmployeeRepository
from app.db.errors import EntityDoesNotExist
from app.models.schemas.employees import (
    ListOfEmployeesInResponse
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

@router.get("", response_model=ListOfEmployeesInResponse, name="employees:get-all")
async def get_all(
    employee_repo: EmployeeRepository = Depends(get_repository(EmployeeRepository)),
) -> ListOfEmployeesInResponse:
    records = await employee_repo.get_all()
    print(records)
    return ListOfEmployeesInResponse(employees=records)