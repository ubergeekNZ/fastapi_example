from uuid import UUID
from typing import Dict
from aioodbc.cursor import Cursor
from app.db.repositories.base import BaseRepository
from app.db.errors import EntityDoesNotExist
from app.models.domain.employees import Employee
from pypika import Query, Table, Field

# TODO - create queries

class EmployeeRepository(BaseRepository):
    
    def __init__(self, cursor: Cursor) -> None:
        super().__init__(cursor)

    async def get_all(self, offset, limit):
        q = Query.from_('employee').select('*')[offset:limit]
        db = self.cursor
        await db.execute(str(q)+';')
        records = await db.fetchall()
        out = []
        for record in records:
            out.append(record)
        return out        

    async def get_by_id(self, id: int) -> Employee:
        employee = Table('employee')
        q = Query.from_('employee').select('*').where(
            employee.employee_id == id
        )
        db = self.cursor
        await db.execute(str(q)+';')
        record = await db.fetchall()
        if len(record):
            return Employee(
                employee_id=record[0][0],
                last_name=record[0][1],
                first_name=record[0][2],
                title=record[0][3],
                reports_to=record[0][4],
                birth_date=record[0][5],
                hire_date=record[0][6],
                address=record[0][7],
                city=record[0][8],
                state=record[0][9],
                country=record[0][10],
                postal_code=record[0][11],
                phone=record[0][12],
                fax=record[0][13],
                email=record[0][14]
            )
        else:
            raise EntityDoesNotExist("employee with id {0} does not exist".format(id))

    async def create_employee(self, data: Employee):
        employee = Table('employee')
        q = Query.into(employee).insert(
            data.employee_id,
            data.last_name,
            data.first_name,
            data.title,
            data.reports_to,
            data.birth_date,
            data.hire_date,
            data.address,
            data.city,
            data.state,
            data.country,
            data.postal_code,
            data.phone,
            data.fax,
            data.email
        )
        db = self.cursor
        await db.execute(str(q)+";")
        q = Query.from_('employee').select('*').where(
            employee.employee_id == data.employee_id
        )
        await db.execute(str(q)+";")
        record = await db.fetchone()
        if len(record):
            return Employee(
                employee_id=record[0][0],
                last_name=record[0][1],
                first_name=record[0][2],
                title=record[0][3],
                reports_to=record[0][4],
                birth_date=record[0][5],
                hire_date=record[0][6],
                address=record[0][7],
                city=record[0][8],
                state=record[0][9],
                country=record[0][10],
                postal_code=record[0][11],
                phone=record[0][12],
                fax=record[0][13],
                email=record[0][14]
            )
        else:
            raise EntityDoesNotExist("employee with id {0} does not exist".format(id))

    async def update(self, data: Employee):

        # customers = Table('customers')

        # Query.update(customers).set(customers.last_login, '2017-01-01 10:00:00')

        # Query.update(customers).set(customers.lname, 'smith').where(customers.id == 10)
        pass

    async def delete(self, data: Employee):
        employee = Table('employee')
        # t = Table("abc")
        # q = Query.from_(
        #     t.for_portion(t.valid_period.from_to('2020-01-01', '2020-02-01'))
        # ).delete()
        pass

