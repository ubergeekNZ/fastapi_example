from datetime import date
from typing import List
from pydantic import BaseModel, Field, validator
from app.models.domain.rwmodel import RWModel

class InvoiceLine(RWModel):
    invoice_line_id: int = Field(0, alias="invoice_line_id")
    invoice_id: int
    track_id: int
    unit_price: float
    quantity: int

class Invoice(RWModel):
    invoice_id: int = Field(0, alias="invoice_id")
    customer_id: int
    invoice_date: date
    billing_address: str
    billing_city: str
    billing_state: str
    billing_country: str
    billing_postal_code: str
    total: int
