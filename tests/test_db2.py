import asyncio
import aioodbc

from functools import partial


dsn = 'Driver=SQLite3;Database=chinook.db'


# Sometimes you may want to reuse same connection parameters multiple times.
# This can be accomplished in a way below using partial function
connect = partial(aioodbc.connect, dsn=dsn, echo=True, autocommit=True)



async def test_error_without_context_managers(loop=None):
    """
    When not using context manager you may end up having unclosed connections
    in case of any error which lead to resource leakage. To avoid
    `Unclosed connection` errors in your code always close after yourself.
    """
    conn = await aioodbc.connect(dsn=dsn, loop=loop)
    cur = await conn.cursor()

    try:
        q = '''
        SELECT
            name,
            type
        FROM sqlite_master
        WHERE type IN ("table","view");
        '''
        await cur.execute(q)
        rows = await cur.fetchall()
        print(rows)
    except Exception:
        pass
    finally:
        await cur.close()
        await conn.close()


async def select_album(loop=None):
    """
    When not using context manager you may end up having unclosed connections
    in case of any error which lead to resource leakage. To avoid
    `Unclosed connection` errors in your code always close after yourself.
    """
    conn = await aioodbc.connect(dsn=dsn, loop=loop)
    cur = await conn.cursor()

    try:
        q = '''
        SELECT *
        FROM album;
        '''
        await cur.execute(q)
        rows = await cur.fetchall()
        print(rows)
    except Exception:
        pass
    finally:
        await cur.close()
        await conn.close()


async def select_artist(loop=None):
    """
    When not using context manager you may end up having unclosed connections
    in case of any error which lead to resource leakage. To avoid
    `Unclosed connection` errors in your code always close after yourself.
    """
    conn = await aioodbc.connect(dsn=dsn, loop=loop)
    cur = await conn.cursor()

    try:
        q = '''
        SELECT *
        FROM artist;
        '''
        await cur.execute(q)
        rows = await cur.fetchall()
        print(rows)
    except Exception:
        pass
    finally:
        await cur.close()
        await conn.close()


async def select_customer(loop=None):
    """
    When not using context manager you may end up having unclosed connections
    in case of any error which lead to resource leakage. To avoid
    `Unclosed connection` errors in your code always close after yourself.
    """
    conn = await aioodbc.connect(dsn=dsn, loop=loop)
    cur = await conn.cursor()

    try:
        q = '''
        SELECT *
        FROM customer;
        '''
        await cur.execute(q)
        rows = await cur.fetchall()
        print(rows)
    except Exception:
        pass
    finally:
        await cur.close()
        await conn.close()


async def select_employee(loop=None):
    """
    When not using context manager you may end up having unclosed connections
    in case of any error which lead to resource leakage. To avoid
    `Unclosed connection` errors in your code always close after yourself.
    """
    conn = await aioodbc.connect(dsn=dsn, loop=loop)
    cur = await conn.cursor()

    try:
        q = '''
        SELECT *
        FROM employee;
        '''
        await cur.execute(q)
        rows = await cur.fetchall()
        print(rows)
    except Exception:
        pass
    finally:
        await cur.close()
        await conn.close()


async def select_genre(loop=None):
    """
    When not using context manager you may end up having unclosed connections
    in case of any error which lead to resource leakage. To avoid
    `Unclosed connection` errors in your code always close after yourself.
    """
    conn = await aioodbc.connect(dsn=dsn, loop=loop)
    cur = await conn.cursor()

    try:
        q = '''
        SELECT *
        FROM genre;
        '''
        await cur.execute(q)
        rows = await cur.fetchall()
        print(rows)
    except Exception:
        pass
    finally:
        await cur.close()
        await conn.close()


async def select_invoice(loop=None):
    """
    When not using context manager you may end up having unclosed connections
    in case of any error which lead to resource leakage. To avoid
    `Unclosed connection` errors in your code always close after yourself.
    """
    conn = await aioodbc.connect(dsn=dsn, loop=loop)
    cur = await conn.cursor()

    try:
        q = '''
        SELECT *
        FROM invoice;
        '''
        await cur.execute(q)
        rows = await cur.fetchall()
        print(rows)
    except Exception:
        pass
    finally:
        await cur.close()
        await conn.close()


async def select_invoice_line(loop=None):
    """
    When not using context manager you may end up having unclosed connections
    in case of any error which lead to resource leakage. To avoid
    `Unclosed connection` errors in your code always close after yourself.
    """
    conn = await aioodbc.connect(dsn=dsn, loop=loop)
    cur = await conn.cursor()

    try:
        q = '''
        SELECT *
        FROM invoice_line;
        '''
        await cur.execute(q)
        rows = await cur.fetchall()
        print(rows)
    except Exception:
        pass
    finally:
        await cur.close()
        await conn.close()

async def select_media_type(loop=None):
    """
    When not using context manager you may end up having unclosed connections
    in case of any error which lead to resource leakage. To avoid
    `Unclosed connection` errors in your code always close after yourself.
    """
    conn = await aioodbc.connect(dsn=dsn, loop=loop)
    cur = await conn.cursor()

    try:
        q = '''
        SELECT *
        FROM media_type;
        '''
        await cur.execute(q)
        rows = await cur.fetchall()
        print(rows)
    except Exception:
        pass
    finally:
        await cur.close()
        await conn.close()


async def select_playlist(loop=None):
    """
    When not using context manager you may end up having unclosed connections
    in case of any error which lead to resource leakage. To avoid
    `Unclosed connection` errors in your code always close after yourself.
    """
    conn = await aioodbc.connect(dsn=dsn, loop=loop)
    cur = await conn.cursor()

    try:
        q = '''
        SELECT *
        FROM playlist;
        '''
        await cur.execute(q)
        rows = await cur.fetchall()
        print(rows)
    except Exception:
        pass
    finally:
        await cur.close()
        await conn.close()


async def select_playlist_track(loop=None):
    """
    When not using context manager you may end up having unclosed connections
    in case of any error which lead to resource leakage. To avoid
    `Unclosed connection` errors in your code always close after yourself.
    """
    conn = await aioodbc.connect(dsn=dsn, loop=loop)
    cur = await conn.cursor()

    try:
        q = '''
        SELECT *
        FROM playlist_track;
        '''
        await cur.execute(q)
        rows = await cur.fetchall()
        print(rows)
    except Exception:
        pass
    finally:
        await cur.close()
        await conn.close()

async def select_track(loop=None):
    """
    When not using context manager you may end up having unclosed connections
    in case of any error which lead to resource leakage. To avoid
    `Unclosed connection` errors in your code always close after yourself.
    """
    conn = await aioodbc.connect(dsn=dsn, loop=loop)
    cur = await conn.cursor()

    try:
        q = '''
        SELECT *
        FROM track;
        '''
        await cur.execute(q)
        rows = await cur.fetchall()
        print(rows)
    except Exception:
        pass
    finally:
        await cur.close()
        await conn.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(test_error_without_context_managers(loop))
    # loop.run_until_complete(select_album(loop))
    # loop.run_until_complete(select_artist(loop))
    # loop.run_until_complete(select_customer(loop))
    # loop.run_until_complete(select_employee(loop))
    # loop.run_until_complete(select_genre(loop))
    # loop.run_until_complete(select_invoice(loop))
    # loop.run_until_complete(select_invoice_line(loop))
    loop.run_until_complete(select_media_type(loop))
    # loop.run_until_complete(select_playlist(loop))
    # loop.run_until_complete(select_playlist_track(loop))
    # loop.run_until_complete(select_track(loop))
