from uuid import UUID
from typing import Dict
from aioodbc.cursor import Cursor
from app.db.repositories.base import BaseRepository


# TODO - create queries

class InvoiceRepository(BaseRepository):
    
    def __init__(self, cursor: Cursor) -> None:
        super().__init__(cursor)

    async def get_all(self):
        query = '''
                SELECT *
                FROM invoice;
                '''
        db = self.cursor
        await db.execute(query)
        records = await db.fetchall()
        out = []
        for record in records:
            out.append(record)
        return out        

    async def get_by_id(self, id: UUID):
        pass

    async def create(self, data: Dict):
        pass

    async def update(self, id: UUID, data: Dict):
        pass

    async def delete(self, id: UUID):
        pass

