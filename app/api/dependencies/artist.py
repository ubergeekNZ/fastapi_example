from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.artist import ArtistRepository
from app.db.errors import EntityDoesNotExist
from app.models.domain.artists import Artist
from app.resources import strings

async def get_artist_by_id_from_path(
    artist_id: int,
    artist_repo: ArtistRepository = Depends(get_repository(ArtistRepository)),
) -> Artist:
    try:
        return await artist_repo.get_by_id(id=artist_id)
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.ARTIST_DOES_NOT_EXIST_ERROR,
        )
