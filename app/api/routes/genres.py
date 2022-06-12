from fastapi import APIRouter, Depends, HTTPException, Query, Response, Body
from starlette import status
from app.api.dependencies.database import get_repository
from app.db.repositories.genre import GenreRepository
from app.db.errors import EntityDoesNotExist
from app.models.domain.genres import Genre
from app.models.schemas.genres import (
    ListOfGenresInResponse,
    GenreInCreate,
    GenreInResponse,
    GenreInUpdate,
    DEFAULT_GENRES_LIMIT,
    DEFAULT_GENRES_OFFSET
)
from app.resources import strings
from app.api.dependencies.genre import (
    get_genre_by_id_from_path
)

router = APIRouter()


@router.get("", response_model=ListOfGenresInResponse, name="genres:get-all")
async def get_all(
    limit: int = Query(DEFAULT_GENRES_LIMIT, ge=1),
    offset: int = Query(DEFAULT_GENRES_OFFSET, ge=0),
    genre_repo: GenreRepository = Depends(get_repository(GenreRepository)),
) -> ListOfGenresInResponse:
    records = await genre_repo.get_all(limit=limit, offset=offset)
    print(records)
    return ListOfGenresInResponse(genres=records)


@router.get("/{genre_id}", response_model=GenreInResponse, name="genres:get-by-id")
async def get_by_id(
    genre: Genre = Depends(get_genre_by_id_from_path),
) -> GenreInResponse:
    return GenreInResponse(genre=genre)


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=GenreInResponse,
    name="genres:create-genre",
)
async def create_genre(
    genre_create: GenreInCreate = Body(..., embed=True, alias="genre"),
    genre_repo: GenreRepository = Depends(get_repository(GenreRepository)),
) -> GenreInResponse:
    genre = await genre_repo.create_genre(genre_create.genre)
    return GenreInResponse(genre=genre)


@router.delete(
    "/{genre_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    name="genres:delete-genre",
    response_class=Response,
)
async def delete_comment_from_article(
    genre: Genre = Depends(get_genre_by_id_from_path),
    genre_repo: GenreRepository = Depends(get_repository(GenreRepository)),
) -> None:
    await genre_repo.delete(data=genre)

@router.put("", response_model=GenreInResponse, name="genres:update-genre")
async def update_genre(
    genre_update: GenreInUpdate = Body(..., embed=True, alias="genre"),
    genre_repo: GenreRepository = Depends(get_repository(GenreRepository)),
) -> GenreInResponse:
    await genre_repo.update(data=genre_update.genre)
    return GenreInResponse(genre=genre_update.genre)