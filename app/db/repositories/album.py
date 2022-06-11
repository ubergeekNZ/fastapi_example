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

    async def create(self, data: Dict):
        album = Table('album')

        q = Query.into(album).insert(1, 'Jane', 'Doe', 'jane@example.com')

    async def update(self, id: int, data: Dict):
        pass

    async def delete(self, id: int):
        pass

