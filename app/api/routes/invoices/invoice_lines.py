from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.invoice import InvoiceRepository
from app.db.errors import EntityDoesNotExist
from app.models.schemas.invoices import (
    ListOfInvoicesInResponse
)
from app.resources import strings

router = APIRouter()

# @router.get(
#     "",
#     response_model=ListOfCommentsInResponse,
#     name="comments:get-comments-for-article",
# )
# @router.get("/", status_code=200) 
# async def root():
#     return {"message": "Hello World"}

@router.get("", response_model=ListOfInvoicesInResponse, name="invoice_lines:get-all")
async def get_all(
    invoice_repo: InvoiceRepository = Depends(get_repository(InvoiceRepository)),
) -> ListOfInvoicesInResponse:
    records = await invoice_repo.get_all()
    print(records)
    return ListOfInvoicesInResponse(invoices=records)