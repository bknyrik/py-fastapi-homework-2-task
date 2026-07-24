from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from database import get_db, MovieModel
from database.models import CountryModel, GenreModel, ActorModel, LanguageModel
from schemas import movies


router = APIRouter()


@router.get("/movies/{movie_id}/", response_model=movies.MovieDetailSchema)
async def get_movie_by_id(
    movie_id: int,
    db: AsyncSession = Depends(get_db)
) -> MovieModel:
    result = await db.execute(
        select(MovieModel)
        .where(MovieModel.id == movie_id)
        .options(joinedload(MovieModel.genres))
        .options(joinedload(MovieModel.actors))
        .options(joinedload(MovieModel.languages))
        .options(joinedload(MovieModel.country))
    )
    movie_item: MovieModel = result.unique().scalar_one_or_none()

    if not movie_item:
        raise HTTPException(
            status_code=404,
            detail="Movie with the given ID was not found."
        )

    return movie_item


@router.delete("/movies/{movie_id}/")
async def delete_movie_by_id(
    movie_id: int,
    db: AsyncSession = Depends(get_db)
) -> None:
    result = await db.execute(
        select(MovieModel)
        .where(MovieModel.id == movie_id)
    )
    movie_item = result.scalar_one_or_none()

    if not movie_item:
        raise HTTPException(
            status_code=404,
            detail="Movie with the given ID was not found."
        )

    await db.delete(movie_item)
    await db.commit()
