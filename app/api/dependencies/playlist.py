from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.playlist import PlaylistRepository
from app.db.errors import EntityDoesNotExist
from app.models.domain.playlists import Playlist
from app.resources import strings

async def get_playlist_by_id_from_path(
    playlist_id: int,
    playlist_repo: PlaylistRepository = Depends(get_repository(PlaylistRepository)),
) -> Playlist:
    try:
        return await playlist_repo.get_by_id(id=playlist_id)
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.PLAYLIST_DOES_NOT_EXIST_ERROR,
        )
