from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.playlist import PlaylistRepository
from app.db.errors import EntityDoesNotExist
from app.models.schemas.playlists import (
    ListOfPlaylistsInResponse,
    DEFAULT_PLAYLIST_LIMIT,
    DEFAULT_PLAYLIST_OFFSET
)
from app.resources import strings

router = APIRouter()

@router.get("", response_model=ListOfPlaylistsInResponse, name="playlists:get-all")
async def get_all(
    limit: int = Query(DEFAULT_PLAYLIST_LIMIT, ge=1),
    offset: int = Query(DEFAULT_PLAYLIST_OFFSET, ge=0),
    plyalist_repo: PlaylistRepository = Depends(get_repository(PlaylistRepository)),
) -> ListOfPlaylistsInResponse:
    records = await plyalist_repo.get_all(limit=limit, offset=offset)
    print(records)
    return ListOfPlaylistsInResponse(playlists=records)