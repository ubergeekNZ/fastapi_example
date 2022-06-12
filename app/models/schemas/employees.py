from typing import List, Optional
from datetime import date

from app.models.domain.employees import Employee
from app.models.schemas.rwschema import RWSchema
from pydantic import BaseModel


DEFAULT_EMPLOYEES_LIMIT = 20
DEFAULT_EMPLOYEES_OFFSET = 0
class ListOfEmployeesInResponse(BaseModel):
    employees: List[Employee]

class EmployeeInResponse(RWSchema):
    employee: Employee


class EmployeeInCreate(RWSchema):
    employee: Employee

class EmployeeInUpdate(BaseModel):
    employee_id: Optional[int]=None
    last_name:  Optional[str]=None
    first_name:  Optional[str]=None
    title:  Optional[str]=None
    reports_to: Optional[str] = None
    birth_date: Optional[date] = None
    hire_date: Optional[date] = None
    address:  Optional[str]=None
    city:  Optional[str]=None
    state:  Optional[str]=None
    country:  Optional[str]=None
    postal_code:  Optional[str]=None
    phone:  Optional[str]=None
    fax:  Optional[str]=None
    email:  Optional[str]=None