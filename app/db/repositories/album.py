from uuid import UUID
from typing import Dict
from aioodbc.cursor import Cursor
from app.db.repositories.base import BaseRepository
from app.db.errors import EntityDoesNotExist
from app.models.domain.albums import Album
from pypika import Query, Table, Field

# TODO - create queries

class AlbumRepository(BaseRepository):
    
    def __init__(self, cursor: Cursor) -> None:
        super().__init__(cursor)

    async def get_all(self, offset, limit):
        q = Query.from_('album').select('*')[offset:limit]
        db = self.cursor
        await db.execute(str(q)+';')
        records = await db.fetchall()
        out = []
        for record in records:
            out.append(record)
        return out        

    async def get_by_id(self, id: int) -> Album:
        album = Table('album')
        q = Query.from_('album').select('*').where(
            album.album_id == id
        )
        db = self.cursor
        await db.execute(str(q)+';')
        record = await db.fetchall()
        if len(record):
            return Album(album_id=record[0][0], title=record[0][1], artist_id=record[0][2])
        else:
            raise EntityDoesNotExist("album with id {0} does not exist".format(id))

    async def create_album(self, data: Album):
        album = Table('album')
        q = Query.into(album).insert(data.album_id, data.title, data.artist_id)
        db = self.cursor
        await db.execute(str(q)+";")
        q = Query.from_('album').select('*').where(
            album.album_id == data.album_id
        )
        await db.execute(str(q)+";")
        record = await db.fetchone()
        if len(record):
            return Album(album_id=record[0], title=record[1], artist_id=record[2])
        else:
            raise EntityDoesNotExist("album with id {0} does not exist".format(id))

    async def update(self, data: Album):

        # customers = Table('customers')

        # Query.update(customers).set(customers.last_login, '2017-01-01 10:00:00')

        # Query.update(customers).set(customers.lname, 'smith').where(customers.id == 10)
        pass

    async def delete(self, data: Album):
        album = Table('album')
        # t = Table("abc")
        # q = Query.from_(
        #     t.for_portion(t.valid_period.from_to('2020-01-01', '2020-02-01'))
        # ).delete()
        pass



# async def test_insert_with_values(loop=None):
#     """
#     When providing data to your SQL statement make sure to parametrize it with
#     question marks placeholders. Do not use string formatting or make sure
#     your data is escaped to prevent sql injections.

#     NOTE: pyodbc does not support named placeholders syntax.
#     """
#     async with connect(loop=loop) as conn:
#         async with conn.cursor() as cur:
#             # Substitute sql markers with variables
#             await cur.execute('INSERT INTO t1(n, v) VALUES(?, ?);',
#                               ('2', 'test 2'))
#             # NOTE: make sure to pass variables as tuple of strings even if
#             # your data types are different to prevent
#             # pyodbc.ProgrammingError errors. You can even do like this
#             values = (3, 'test 3')
#             await cur.execute('INSERT INTO t1(n, v) VALUES(?, ?);',
#                               *map(str, values))

#             # Retrieve id of last inserted row
#             await cur.execute('SELECT last_insert_rowid();')
#             result = await cur.fetchone()
#             print(result[0])