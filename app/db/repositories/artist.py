from uuid import UUID
from typing import Dict
from aioodbc.cursor import Cursor
from app.db.repositories.base import BaseRepository
from app.db.errors import EntityDoesNotExist
from app.models.domain.artists import Artist
from pypika import Query, Table, Field

# TODO - create queries

class ArtistRepository(BaseRepository):
    
    def __init__(self, cursor: Cursor) -> None:
        super().__init__(cursor)

    async def get_all(self, offset, limit):
        q = Query.from_('artist').select('*')[offset:limit]
        db = self.cursor
        await db.execute(str(q)+';')
        records = await db.fetchall()
        out = []
        for record in records:
            out.append(record)
        return out        

    async def get_by_id(self, id: int) -> Artist:
        artist = Table('artist')
        q = Query.from_('artist').select('*').where(
            artist.artist_id == id
        )
        db = self.cursor
        await db.execute(str(q)+';')
        record = await db.fetchall()
        if len(record):
            return Artist(artist_id=record[0][0], name=record[0][1])
        else:
            raise EntityDoesNotExist("artist with id {0} does not exist".format(id))

    async def create_artist(self, data: Artist):
        artist = Table('artist')
        q = Query.into(artist).insert(data.artist_id, data.name)
        db = self.cursor
        await db.execute(str(q)+";")
        q = Query.from_('artist').select('*').where(
            artist.artist_id == data.Artist_id
        )
        await db.execute(str(q)+";")
        record = await db.fetchone()
        if len(record):
            return Artist(artist_id=record[0], name=record[1])
        else:
            raise EntityDoesNotExist("Artist with id {0} does not exist".format(id))

    async def update(self, data: Artist):

        # customers = Table('customers')

        # Query.update(customers).set(customers.last_login, '2017-01-01 10:00:00')

        # Query.update(customers).set(customers.lname, 'smith').where(customers.id == 10)
        pass

    async def delete(self, data: Artist):
        artist = Table('artist')
        # t = Table("abc")
        # q = Query.from_(
        #     t.for_portion(t.valid_period.from_to('2020-01-01', '2020-02-01'))
        # ).delete()
        pass

