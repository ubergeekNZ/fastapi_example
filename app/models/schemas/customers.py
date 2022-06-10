from typing import List

from app.models.domain.customers import Customer
from pydantic import BaseModel


class ListOfCustomersInResponse(BaseModel):
    customers: List[Customer]