from typing import List, Optional

from app.models.domain.customers import Customer
from app.models.schemas.rwschema import RWSchema
from pydantic import BaseModel


DEFAULT_CUSTOMERS_LIMIT = 20
DEFAULT_CUSTOMERS_OFFSET = 0
class ListOfCustomersInResponse(BaseModel):
    customers: List[Customer]

class CustomerInResponse(RWSchema):
    customer: Customer


class CustomerInCreate(RWSchema):
    customer: Customer

class CustomerInUpdate(BaseModel):
    customer_id: Optional[int]=None
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    company: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    postal_code: Optional[str] = None
    phone: Optional[str] = None
    fax: Optional[str] = None
    email: Optional[str] = None
    support_rep_id: Optional[int] = None