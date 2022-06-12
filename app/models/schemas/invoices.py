from typing import List, Optional
from datetime import date
from app.models.domain.invoices import Invoice, InvoiceLine
from app.models.schemas.rwschema import RWSchema
from pydantic import BaseModel


DEFAULT_INVOICES_LIMIT = 20
DEFAULT_INVOICES_OFFSET = 0
class ListOfInvoicesInResponse(BaseModel):
    invoices: List[Invoice]

class ListOfInvoiceLinesInResponse(BaseModel):
    invoiceLines: List[InvoiceLine]

class InvoiceInResponse(RWSchema):
    invoice: Invoice


class InvoiceInCreate(RWSchema):
    invoice: Invoice

class InvoiceInUpdate(BaseModel):
    invoice_id: Optional[int]=None
    customer_id: Optional[int]=None
    invoice_date: Optional[date]=None
    billing_address: Optional[str]=None
    billing_city: Optional[str]=None
    billing_state: Optional[str]=None
    billing_country: Optional[str]=None
    billing_postal_code: Optional[str]=None
    total: Optional[int]=None
