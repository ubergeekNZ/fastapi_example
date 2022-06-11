from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.invoice import InvoiceRepository
from app.db.errors import EntityDoesNotExist
from app.models.schemas.invoices import (
    ListOfInvoicesInResponse,
    DEFAULT_INVOICES_LIMIT,
    DEFAULT_INVOICES_OFFSET
)
from app.resources import strings

router = APIRouter()

@router.get("", response_model=ListOfInvoicesInResponse, name="invoice_lines:get-all")
async def get_all(
    limit: int = Query(DEFAULT_INVOICES_LIMIT, ge=1),
    offset: int = Query(DEFAULT_INVOICES_OFFSET, ge=0),
    invoice_repo: InvoiceRepository = Depends(get_repository(InvoiceRepository)),
) -> ListOfInvoicesInResponse:
    records = await invoice_repo.get_all(limit=limit, offset=offset)
    print(records)
    return ListOfInvoicesInResponse(invoices=records)