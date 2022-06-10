from fastapi import APIRouter, Depends, HTTPException, Query
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.playlist import PlaylistRepository
from app.db.errors import EntityDoesNotExist
from app.models.schemas.playlists import (
    ListOfPlaylistsInResponse
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

@router.get("", response_model=ListOfPlaylistsInResponse, name="playlists:get-all")
async def get_all(
    plyalist_repo: PlaylistRepository = Depends(get_repository(PlaylistRepository)),
) -> ListOfPlaylistsInResponse:
    records = await plyalist_repo.get_all()
    print(records)
    return ListOfPlaylistsInResponse(playlists=records)