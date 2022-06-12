from uuid import UUID
from typing import Dict
from aioodbc.cursor import Cursor
from app.db.repositories.base import BaseRepository
from app.db.errors import EntityDoesNotExist
from app.models.domain.invoices import Invoice
from pypika import Query, Table, Field

# TODO - create queries

class InvoiceRepository(BaseRepository):
    
    def __init__(self, cursor: Cursor) -> None:
        super().__init__(cursor)

    async def get_all(self, offset, limit):
        q = Query.from_('invoice').select('*')[offset:limit]
        db = self.cursor
        await db.execute(str(q)+';')
        records = await db.fetchall()
        out = []
        for record in records:
            out.append(record)
        return out        

    async def get_by_id(self, id: int) -> Invoice:
        invoice = Table('invoice')
        q = Query.from_('invoice').select('*').where(
            invoice.invoice_id == id
        )
        db = self.cursor
        await db.execute(str(q)+';')
        record = await db.fetchall()
        if len(record):
            return Invoice(
                invoice_id=record[0][0],
                customer_id = record[0][1],
                invoice_date = record[0][2],
                billing_address = record[0][3],
                billing_city = record[0][4],
                billing_state = record[0][5],
                billing_country = record[0][6],
                billing_postal_code = record[0][7],
                total = record[0][8],
            )
        else:
            raise EntityDoesNotExist("Invoice with id {0} does not exist".format(id))

    async def create_invoice(self, data: Invoice):
        invoice = Table('invoice')
        q = Query.into(invoice).insert(
            data.invoice_id,
            data.customer_id,
            data.invoice_date,
            data.billing_address,
            data.billing_city,
            data.billing_state,
            data.billing_country,
            data.billing_postal_code,
            data.total,
        )
        db = self.cursor
        await db.execute(str(q)+";")
        q = Query.from_('invoice').select('*').where(
            invoice.invoice_id == data.invoice_id
        )
        await db.execute(str(q)+";")
        record = await db.fetchone()
        if len(record):
            return Invoice(
                invoice_id=record[0][0],
                customer_id = record[0][1],
                invoice_date = record[0][2],
                billing_address = record[0][3],
                billing_city = record[0][4],
                billing_state = record[0][5],
                billing_country = record[0][6],
                billing_postal_code = record[0][7],
                total = record[0][8],
            )
        else:
            raise EntityDoesNotExist("Invoice with id {0} does not exist".format(id))

    async def update(self, data: Invoice):

        # customers = Table('customers')

        # Query.update(customers).set(customers.last_login, '2017-01-01 10:00:00')

        # Query.update(customers).set(customers.lname, 'smith').where(customers.id == 10)
        pass

    async def delete(self, data: Invoice):
        invoice = Table('invoice')
        # t = Table("abc")
        # q = Query.from_(
        #     t.for_portion(t.valid_period.from_to('2020-01-01', '2020-02-01'))
        # ).delete()
        pass

