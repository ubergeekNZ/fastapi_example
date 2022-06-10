from typing import List

from app.models.domain.employees import Employee
from pydantic import BaseModel


class ListOfEmployeesInResponse(BaseModel):
    employees: List[Employee]