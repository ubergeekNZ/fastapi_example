from typing import List

from app.models.domain.customers import Customer
from pydantic import BaseModel

DEFAULT_CUSTOMERS_LIMIT = 20
DEFAULT_CUSTOMERS_OFFSET = 0
class ListOfCustomersInResponse(BaseModel):
    customers: List[Customer]