Example of FastAPI
------------------

This example is based on the following github project but modified to use the chinook database and aiodbc. (Still WIP)

https://github.com/nsidnev/fastapi-realworld-example-app

An explanation of the architecture and repository pattern is decribed in this blog.

https://www.jeffastor.com/blog/hooking-fastapi-endpoints-up-to-a-postgres-database


Run
---

poetry run uvicorn --host=0.0.0.0 app.main:app

Web routes
----------

All routes are available on ``/docs`` or ``/redoc`` paths with Swagger or ReDoc.


Project structure
-----------------

Files related to application are in the ``app`` or ``tests`` directories.
Application parts are:

::

    app
    ├── api              - web related stuff.
    │   ├── dependencies - dependencies for routes definition.
    │   ├── errors       - definition of error handlers.
    │   └── routes       - web routes.
    ├── core             - application configuration, startup events, logging.
    ├── db               - db related stuff.
    │   ├── migrations   - manually written alembic migrations.
    │   └── repositories - all crud stuff.
    ├── models           - pydantic models for this application.
    │   ├── domain       - main models that are used almost everywhere.
    │   └── schemas      - schemas for using in web routes.
    ├── resources        - strings that are used in web responses.
    ├── services         - logic that is not just crud related.
    └── main.py          - FastAPI application creation and configuration.
