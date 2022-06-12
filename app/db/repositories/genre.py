from uuid import UUID
from typing import Dict
from aioodbc.cursor import Cursor
from app.db.repositories.base import BaseRepository
from app.db.repositories.base import BaseRepository
from app.db.errors import EntityDoesNotExist
from app.models.domain.genres import Genre
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

    async def get_by_id(self, id: int) -> Genre:
        genre = Table('genre')
        q = Query.from_('genre').select('*').where(
            genre.genre_id == id
        )
        db = self.cursor
        await db.execute(str(q)+';')
        record = await db.fetchall()
        if len(record):
            return Genre(genre_id=record[0][0], name=record[0][1])
        else:
            raise EntityDoesNotExist("genre with id {0} does not exist".format(id))

    async def create_genre(self, data: Genre):
        genre = Table('genre')
        q = Query.into(genre).insert(data.genre_id, data.name)
        db = self.cursor
        await db.execute(str(q)+";")
        q = Query.from_('genre').select('*').where(
            genre.genre_id == data.genre_id
        )
        await db.execute(str(q)+";")
        record = await db.fetchone()
        if len(record):
            return Genre(genre_id=record[0], name=record[1])
        else:
            raise EntityDoesNotExist("genre with id {0} does not exist".format(id))

    async def update(self, data: Genre):

        # customers = Table('customers')

        # Query.update(customers).set(customers.last_login, '2017-01-01 10:00:00')

        # Query.update(customers).set(customers.lname, 'smith').where(customers.id == 10)
        pass

    async def delete(self, data: Genre):
        genre = Table('genre')
        # t = Table("abc")
        # q = Query.from_(
        #     t.for_portion(t.valid_period.from_to('2020-01-01', '2020-02-01'))
        # ).delete()
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