from typing import List

from app.models.domain.invoices import Invoice, InvoiceLine
from pydantic import BaseModel

DEFAULT_INVOICES_LIMIT = 20
DEFAULT_INVOICES_OFFSET = 0
class ListOfInvoicesInResponse(BaseModel):
    invoices: List[Invoice]

class ListOfInvoiceLinesInResponse(BaseModel):
    invoiceLines: List[InvoiceLine]