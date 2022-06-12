from uuid import UUID
from typing import Dict
from aioodbc.cursor import Cursor
from app.db.repositories.base import BaseRepository
from app.db.errors import EntityDoesNotExist
from app.models.domain.customers import Customer
from pypika import Query, Table, Field

# TODO - create queries

class CustomerRepository(BaseRepository):
    
    def __init__(self, cursor: Cursor) -> None:
        super().__init__(cursor)

    async def get_all(self, offset, limit):
        q = Query.from_('customer').select('*')[offset:limit]
        db = self.cursor
        await db.execute(str(q)+';')
        records = await db.fetchall()
        out = []
        for record in records:
            out.append(record)
        return out        

    async def get_by_id(self, id: int) -> Customer:
        customer = Table('customer')
        q = Query.from_('customer').select('*').where(
            customer.customer_id == id
        )
        db = self.cursor
        await db.execute(str(q)+';')
        record = await db.fetchall()
        if len(record):
            return Customer(
                customer_id = record[0][0],
                last_name = record[0][1],
                first_name = record[0][2],
                company = record[0][3],
                address = record[0][4],
                city = record[0][5],
                state = record[0][6],
                country = record[0][7],
                postal_code = record[0][8],
                phone = record[0][9],
                fax = record[0][10],
                email = record[0][11],
                support_rep_id = record[0][12],
            )
        else:
            raise EntityDoesNotExist("customer with id {0} does not exist".format(id))

    async def create_customer(self, data: Customer):
        customer = Table('customer')
        q = Query.into(customer).insert(
            data.customer_id,
            data.last_name,
            data.first_name,
            data.company,
            data.address,
            data.city,
            data.state,
            data.country,
            data.postal_code,
            data.phone,
            data.fax,
            data.email,
            data.support_rep_id,
        )
        db = self.cursor
        await db.execute(str(q)+";")
        q = Query.from_('customer').select('*').where(
            customer.customer_id == data.customer_id
        )
        await db.execute(str(q)+";")
        record = await db.fetchone()
        if len(record):
            return Customer(
                customer_id = record[0][0],
                last_name = record[0][1],
                first_name = record[0][2],
                company = record[0][3],
                address = record[0][4],
                city = record[0][5],
                state = record[0][6],
                country = record[0][7],
                postal_code = record[0][8],
                phone = record[0][9],
                fax = record[0][10],
                email = record[0][11],
                support_rep_id = record[0][12],
            )
        else:
            raise EntityDoesNotExist("customer with id {0} does not exist".format(id))

    async def update(self, data: Customer):

        # customers = Table('customers')

        # Query.update(customers).set(customers.last_login, '2017-01-01 10:00:00')

        # Query.update(customers).set(customers.lname, 'smith').where(customers.id == 10)
        pass

    async def delete(self, data: Customer):
        customer = Table('customer')
        # t = Table("abc")
        # q = Query.from_(
        #     t.for_portion(t.valid_period.from_to('2020-01-01', '2020-02-01'))
        # ).delete()
        pass
