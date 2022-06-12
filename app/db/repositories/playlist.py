from uuid import UUID
from typing import Dict
from aioodbc.cursor import Cursor
from app.db.repositories.base import BaseRepository
from app.db.errors import EntityDoesNotExist
from app.models.domain.playlists import Playlist
from pypika import Query, Table, Field

# TODO - create queries

class PlaylistRepository(BaseRepository):
    
    def __init__(self, cursor: Cursor) -> None:
        super().__init__(cursor)

    async def get_all(self, offset, limit):
        q = Query.from_('playlist').select('*')[offset:limit]
        db = self.cursor
        await db.execute(str(q)+';')
        records = await db.fetchall()
        out = []
        for record in records:
            out.append(record)
        return out        

    async def get_by_id(self, id: int) -> Playlist:
        playlist = Table('playlist')
        q = Query.from_('playlist').select('*').where(
            playlist.playlist_id == id
        )
        db = self.cursor
        await db.execute(str(q)+';')
        record = await db.fetchall()
        if len(record):
            return Playlist(playlist_id=record[0][0], name=record[0][1])
        else:
            raise EntityDoesNotExist("playlist with id {0} does not exist".format(id))

    async def create_playlist(self, data: Playlist):
        playlist = Table('playlist')
        q = Query.into(playlist).insert(data.playlist_id, data.name)
        db = self.cursor
        await db.execute(str(q)+";")
        q = Query.from_('playlist').select('*').where(
            playlist.playlist_id == data.playlist_id
        )
        await db.execute(str(q)+";")
        record = await db.fetchone()
        if len(record):
            return Playlist(playlist_id=record[0], name=record[1])
        else:
            raise EntityDoesNotExist("playlist with id {0} does not exist".format(id))

    async def update(self, data: Playlist):

        # customers = Table('customers')

        # Query.update(customers).set(customers.last_login, '2017-01-01 10:00:00')

        # Query.update(customers).set(customers.lname, 'smith').where(customers.id == 10)
        pass

    async def delete(self, data: Playlist):
        playlist = Table('playlist')
        # t = Table("abc")
        # q = Query.from_(
        #     t.for_portion(t.valid_period.from_to('2020-01-01', '2020-02-01'))
        # ).delete()
        pass

