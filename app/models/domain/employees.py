from datetime import date
from typing import List
from pydantic import BaseModel, Field, validator
from app.models.domain.rwmodel import RWModel
from typing import Optional

class Employee(RWModel):
    employee_id: int = Field(0, alias="employee_id")
    last_name: str
    first_name: str
    title: str
    reports_to: Optional[str] = None
    birth_date: Optional[date] = None
    hire_date: date
    address: str
    city: str
    state: str
    country: str
    postal_code: str
    phone: str
    fax: str
    email: str