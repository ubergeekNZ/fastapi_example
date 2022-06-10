import asyncio
import aioodbc
from typing import AsyncGenerator, Callable, Type
from concurrent.futures import ThreadPoolExecutor
from aioodbc.cursor import Cursor
from fastapi import HTTPException
from fastapi import Depends
from pyodbc import OperationalError
from starlette import status
from app.db.repositories.base import BaseRepository

loop = asyncio.get_event_loop()

# TODO -  create db string - probably get this working for sqlite database first
# dsn = rf'Driver={DB_DRIVER};Server={DB_SERVER},{DB_PORT};Database={DB_DATABASE};UID={DB_USERNAME};PWD={DB_PASSWORD};Trusted_Connection=no;'
# dsn = 'Driver=ODBC Driver 11 for SQL Server;Server=123.456.789.55,1000/mycompany;\
#            Database=Asia_client;User=myname;\
#            Password=mypass'
dsn = 'Driver=SQLite3;Database=database/chinook.db'

async def _get_cursor(self) -> Cursor:
        
    try:
        async with aioodbc.connect(dsn=dsn, loop=loop, executor=ThreadPoolExecutor(max_workers=50)) as conn:
            async with conn.cursor() as cur:
                yield cur
    except OperationalError:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY,
                            detail="DB connectivity failed")

def get_repository(
    repo_type: Type[BaseRepository],
) -> Callable[[Cursor], BaseRepository]:
    def _get_repo(
        conn: Cursor = Depends(_get_cursor),
    ) -> BaseRepository:
        return repo_type(conn)

    return _get_repo
