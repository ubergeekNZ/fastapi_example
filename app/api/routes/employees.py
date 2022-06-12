from fastapi import APIRouter, Depends, HTTPException, Query, Response, Body
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.employee import EmployeeRepository
from app.db.errors import EntityDoesNotExist
from app.models.domain.employees import Employee
from app.models.schemas.employees import (
    ListOfEmployeesInResponse,
    EmployeeInCreate,
    EmployeeInResponse,
    EmployeeInUpdate,
    DEFAULT_EMPLOYEES_LIMIT,
    DEFAULT_EMPLOYEES_OFFSET
)
from app.resources import strings
from app.api.dependencies.employee import (
    get_Employee_by_id_from_path
)

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


@router.get("/{employee_id}", response_model=EmployeeInResponse, name="employees:get-by-id")
async def get_by_id(
    employee: Employee = Depends(get_Employee_by_id_from_path),
) -> EmployeeInResponse:
    return EmployeeInResponse(employee=employee)


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=EmployeeInResponse,
    name="employees:create-employee",
)
async def create_employee(
    employee_create: EmployeeInCreate = Body(..., embed=True, alias="employee"),
    employee_repo: EmployeeRepository = Depends(get_repository(EmployeeRepository)),
) -> EmployeeInResponse:
    employee = await employee_repo.create_employee(employee_create.employee)
    return EmployeeInResponse(employee=employee)


@router.delete(
    "/{employee_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    name="employees:delete-employee",
    response_class=Response,
)
async def delete_comment_from_article(
    employee: Employee = Depends(get_Employee_by_id_from_path),
    employee_repo: EmployeeRepository = Depends(get_repository(EmployeeRepository)),
) -> None:
    await employee_repo.delete(data=employee)

@router.put("", response_model=EmployeeInResponse, name="employees:update-employee")
async def update_employee(
    employee_update: EmployeeInUpdate = Body(..., embed=True, alias="employee"),
    employee_repo: EmployeeRepository = Depends(get_repository(EmployeeRepository)),
) -> EmployeeInResponse:
    await employee_repo.update(data=employee_update.employee)
    return EmployeeInResponse(employee=employee_update.employee)