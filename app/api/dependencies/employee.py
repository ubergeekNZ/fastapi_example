from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.employee import EmployeeRepository
from app.db.errors import EntityDoesNotExist
from app.models.domain.employees import Employee
from app.resources import strings

async def get_Employee_by_id_from_path(
    mployee_id: int,
    employee_repo: EmployeeRepository = Depends(get_repository(EmployeeRepository)),
) -> Employee:
    try:
        return await employee_repo.get_by_id(id=mployee_id)
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.EMPLOYEE_DOES_NOT_EXIST_ERROR,
        )
