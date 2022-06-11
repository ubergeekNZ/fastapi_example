from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.employee import EmployeeRepository
from app.db.errors import EntityDoesNotExist
from app.models.schemas.employees import (
    ListOfEmployeesInResponse,
    DEFAULT_EMPLOYEES_LIMIT,
    DEFAULT_EMPLOYEES_OFFSET
)
from app.resources import strings

router = APIRouter()

@router.get("", response_model=ListOfEmployeesInResponse, name="employees:get-all")
async def get_all(
    limit: int = Query(DEFAULT_EMPLOYEES_LIMIT, ge=1),
    offset: int = Query(DEFAULT_EMPLOYEES_OFFSET, ge=0),
    employee_repo: EmployeeRepository = Depends(get_repository(EmployeeRepository)),
) -> ListOfEmployeesInResponse:
    records = await employee_repo.get_all(limit=limit, offset=offset)
    print(records)
    return ListOfEmployeesInResponse(employees=records)