from uuid import UUID
from typing import Dict
from aioodbc.cursor import Cursor
from app.db.repositories.base import BaseRepository
from app.db.errors import EntityDoesNotExist
from app.models.domain.tracks import Track
from pypika import Query, Table, Field

# TODO - create queries

class TrackRepository(BaseRepository):
    
    def __init__(self, cursor: Cursor) -> None:
        super().__init__(cursor)

    async def get_all(self, offset, limit):
        q = Query.from_('track').select('*')[offset:limit]
        db = self.cursor
        await db.execute(str(q)+';')
        records = await db.fetchall()
        out = []
        for record in records:
            out.append(record)
        return out        

    async def get_by_id(self, id: int) -> Track:
        track = Table('track')
        q = Query.from_('track').select('*').where(
            track.track_id == id
        )
        db = self.cursor
        await db.execute(str(q)+';')
        record = await db.fetchall()
        if len(record):
            return Track(
                track_id=record[0][0],
                name=record[0][1],
                album_id=record[0][2],
                media_type_id=record[0][3],
                genre_id=record[0][4],
                composer=record[0][5],
                milliseconds=record[0][6],
                bytes=record[0][7],
                unit_price=record[0][8],
            )
        else:
            raise EntityDoesNotExist("Track with id {0} does not exist".format(id))

    async def create_track(self, data: Track):
        track = Table('track')
        q = Query.into(track).insert(
            data.track_id,
            data.name,
            data.album_id,
            data.media_type_id,
            data.genre_id,
            data.composer,
            data.milliseconds,
            data.bytes,
            data.unit_price,
        )
        db = self.cursor
        await db.execute(str(q)+";")
        q = Query.from_('track').select('*').where(
            track.track_id == data.track_id
        )
        await db.execute(str(q)+";")
        record = await db.fetchone()
        if len(record):
            return Track(
                track_id=record[0][0],
                name=record[0][1],
                album_id=record[0][2],
                media_type_id=record[0][3],
                genre_id=record[0][4],
                composer=record[0][5],
                milliseconds=record[0][6],
                bytes=record[0][7],
                unit_price=record[0][8],
            )
        else:
            raise EntityDoesNotExist("Track with id {0} does not exist".format(id))

    async def update(self, data: Track):

        # customers = Table('customers')

        # Query.update(customers).set(customers.last_login, '2017-01-01 10:00:00')

        # Query.update(customers).set(customers.lname, 'smith').where(customers.id == 10)
        pass

    async def delete(self, data: Track):
        track = Table('track')
        # t = Table("abc")
        # q = Query.from_(
        #     t.for_portion(t.valid_period.from_to('2020-01-01', '2020-02-01'))
        # ).delete()
        pass

