from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.invoice import InvoiceRepository
from app.db.errors import EntityDoesNotExist
from app.models.domain.invoices import Invoice
from app.resources import strings

async def get_invoice_by_id_from_path(
    invoice_id: int,
    invoice_repo: InvoiceRepository = Depends(get_repository(InvoiceRepository)),
) -> Invoice:
    try:
        return await invoice_repo.get_by_id(id=invoice_id)
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.INVOICE_DOES_NOT_EXIST_ERROR,
        )
