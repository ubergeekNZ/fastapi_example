from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.artist import ArtistRepository
from app.db.errors import EntityDoesNotExist
from app.models.schemas.artists import (
    ListOfArtistsInResponse
)
from app.resources import strings

router = APIRouter()

# @router.get(
#     "",
#     response_model=ListOfCommentsInResponse,
#     name="comments:get-comments-for-article",
# )
# @router.get("/", status_code=200) 
# async def root():
#     return {"message": "Hello World"}

@router.get("", response_model=ListOfArtistsInResponse, name="artist:get-all")
async def get_all(
    artist_repo: ArtistRepository = Depends(get_repository(ArtistRepository)),
) -> ListOfArtistsInResponse:
    records = await artist_repo.get_all()
    print(records)
    return ListOfArtistsInResponse(artists=records)