from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.album import AlbumRepository
from app.db.errors import EntityDoesNotExist
from app.models.schemas.albums import (
    ListOfAlbumsInResponse
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

@router.get("", response_model=ListOfAlbumsInResponse, name="albums:get-all")
async def get_all(
    album_repo: AlbumRepository = Depends(get_repository(AlbumRepository)),
) -> ListOfAlbumsInResponse:
    records = await album_repo.get_all()
    print(records)
    return ListOfAlbumsInResponse(albums=records)