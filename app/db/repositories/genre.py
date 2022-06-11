from uuid import UUID
from typing import Dict
from aioodbc.cursor import Cursor
from app.db.repositories.base import BaseRepository
from pypika import Query, Table, Field

# TODO - create queries

class GenreRepository(BaseRepository):
    
    def __init__(self, cursor: Cursor) -> None:
        super().__init__(cursor)

    async def get_all(self, offset, limit):
        q = Query.from_('genre').select('*')[offset:limit]
        db = self.cursor
        await db.execute(str(q)+';')
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




# conn = await aioodbc.connect(dsn=dsn, loop=loop)
#     cur = await conn.cursor()

#     try:
#         q = '''
#         SELECT *
#         FROM genre;
#         '''
#         await cur.execute(q)
#         rows = await cur.fetchall()
#         print(rows)
#     except Exception:
#         pass
#     finally:
#         await cur.close()
#         await conn.close()