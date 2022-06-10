from aioodbc.cursor import Cursor


class BaseRepository:
    def __init__(self, cursor: Cursor) -> None:
        self._cursor = cursor

    @property
    def cursor(self) -> Cursor:
        return self._cursor