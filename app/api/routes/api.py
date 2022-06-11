from fastapi import APIRouter

from app.api.routes import artists, customers, employees, genres, media_types, tracks
from app.api.routes import albums
from app.api.routes.invoices import api as invoices
from app.api.routes.playlists import api as playlists

router = APIRouter()

router.include_router(albums.router, tags=["albums"], prefix="/albums")
router.include_router(artists.router, tags=["artists"], prefix="/artist")
router.include_router(customers.router, tags=["customers"], prefix="/customer")
router.include_router(employees.router, tags=["employees"], prefix="/employee")
router.include_router(genres.router, tags=["genres"], prefix="/genres")
router.include_router(media_types.router, tags=["media_types"], prefix="/media_types")
router.include_router(tracks.router, tags=["tracks"], prefix="/tracks")
router.include_router(invoices.router, tags=["invoices"])
router.include_router(playlists.router, tags=["playlists"])

