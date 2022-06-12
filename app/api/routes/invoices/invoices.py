from app.models.domain.invoices import Invoice
from fastapi import APIRouter, Depends, HTTPException, Query, Body, Response
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.invoice import InvoiceRepository
from app.db.errors import EntityDoesNotExist
from app.models.schemas.invoices import (
    ListOfInvoicesInResponse,
    InvoiceInResponse,
    InvoiceInCreate,
    InvoiceInUpdate,
    DEFAULT_INVOICES_LIMIT,
    DEFAULT_INVOICES_OFFSET
)
from app.resources import strings
from app.api.dependencies.invoice import (
    get_invoice_by_id_from_path
)


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


@router.get("/{invoice_id}", response_model=InvoiceInResponse, name="invoices:get-by-id")
async def get_by_id(
    invoice: Invoice = Depends(get_invoice_by_id_from_path),
) -> InvoiceInResponse:
    return InvoiceInResponse(invoice=invoice)


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=InvoiceInResponse,
    name="invoices:create-invoice",
)
async def create_invoice(
    invoice_create: InvoiceInCreate = Body(..., embed=True, alias="invoice"),
    invoice_repo: InvoiceRepository = Depends(get_repository(InvoiceRepository)),
) -> InvoiceInResponse:
    invoice = await invoice_repo.create_invoice(invoice_create.invoice)
    return InvoiceInResponse(invoice=invoice)


@router.delete(
    "/{invoice_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    name="invoices:delete-invoice",
    response_class=Response,
)
async def delete_comment_from_article(
    invoice: Invoice = Depends(get_invoice_by_id_from_path),
    invoice_repo: InvoiceRepository = Depends(get_repository(InvoiceRepository)),
) -> None:
    await invoice_repo.delete(data=invoice)

@router.put("", response_model=InvoiceInResponse, name="invoices:update-invoice")
async def update_invoice(
    invoice_update: InvoiceInUpdate = Body(..., embed=True, alias="invoice"),
    invoice_repo: InvoiceRepository = Depends(get_repository(InvoiceRepository)),
) -> InvoiceInResponse:
    await invoice_repo.update(data=invoice_update.invoice)
    return InvoiceInResponse(invoice=invoice_update.invoice)