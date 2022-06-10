from typing import List
from pydantic import BaseModel, Field, validator
from app.models.domain.rwmodel import RWModel
from typing import Optional

class Customer(RWModel):
    customer_id: int = Field(0, alias="customer_id")
    last_name: str
    first_name: str
    company: Optional[str] = None
    address: str
    city: str
    state: Optional[str] = None
    country: Optional[str] = None
    postal_code: Optional[str] = None
    phone: Optional[str] = None
    fax: Optional[str] = None
    email: Optional[str] = None
    support_rep_id: int