from fastapi import APIRouter

from app.api.routes.playlists import playlist_tracks, playlists

router = APIRouter()

router.include_router(playlists.router, prefix="/playlists")
router.include_router(playlist_tracks.router, prefix="/playlists")
