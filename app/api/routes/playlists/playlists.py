from app.models.domain.playlists import Playlist
from fastapi import APIRouter, Depends, HTTPException, Query, Body, Response
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.playlist import PlaylistRepository
from app.db.errors import EntityDoesNotExist
from app.models.schemas.playlists import (
    ListOfPlaylistsInResponse,
    PlaylistInResponse,
    PlaylistInCreate,
    PlaylistInUpdate,
    DEFAULT_PLAYLIST_LIMIT,
    DEFAULT_PLAYLIST_OFFSET
)
from app.resources import strings
from app.api.dependencies.playlist import (
    get_playlist_by_id_from_path
)


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


@router.get("/{playlist_id}", response_model=PlaylistInResponse, name="playlists:get-by-id")
async def get_by_id(
    playlist: Playlist = Depends(get_playlist_by_id_from_path),
) -> PlaylistInResponse:
    return PlaylistInResponse(playlist=playlist)


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=PlaylistInResponse,
    name="playlists:create-playlist",
)
async def create_playlist(
    playlist_create: PlaylistInUpdate = Body(..., embed=True, alias="playlist"),
    playlist_repo: PlaylistRepository = Depends(get_repository(PlaylistRepository)),
) -> PlaylistInResponse:
    playlist = await playlist_repo.create_playlist(playlist_create.playlist)
    return PlaylistInResponse(playlist=playlist)


@router.delete(
    "/{playlist_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    name="playlists:delete-playlist",
    response_class=Response,
)
async def delete_comment_from_article(
    playlist: Playlist = Depends(get_playlist_by_id_from_path),
    playlist_repo: PlaylistRepository = Depends(get_repository(PlaylistRepository)),
) -> None:
    await playlist_repo.delete(data=playlist)

@router.put("", response_model=PlaylistInResponse, name="playlists:update-playlist")
async def update_playlist(
    playlist_update: PlaylistInUpdate = Body(..., embed=True, alias="playlist"),
    playlist_repo: PlaylistRepository = Depends(get_repository(PlaylistRepository)),
) -> PlaylistInResponse:
    await playlist_repo.update(data=playlist_update.playlist)
    return PlaylistInResponse(playlist=playlist_update.playlist)