from typing import List

from app.models.domain.employees import Employee
from pydantic import BaseModel

DEFAULT_EMPLOYEES_LIMIT = 20
DEFAULT_EMPLOYEES_OFFSET = 0
class ListOfEmployeesInResponse(BaseModel):
    employees: List[Employee]