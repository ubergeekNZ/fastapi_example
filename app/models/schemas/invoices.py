from typing import List

from app.models.domain.invoices import Invoice, InvoiceLine
from pydantic import BaseModel


class ListOfInvoicesInResponse(BaseModel):
    invoices: List[Invoice]

class ListOfInvoiceLinesInResponse(BaseModel):
    invoiceLines: List[InvoiceLine]