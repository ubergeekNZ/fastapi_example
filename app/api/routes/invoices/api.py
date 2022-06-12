from fastapi import APIRouter

from app.api.routes.invoices import invoice_lines, invoices

router = APIRouter()

router.include_router(invoices.router, prefix="/invoices")
# router.include_router(invoice_lines.router, prefix="/invoices")
