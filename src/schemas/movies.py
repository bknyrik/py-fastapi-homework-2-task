import datetime

from pydantic import BaseModel, ConfigDict


class CountryBaseSchema(BaseModel):
    id: int
    code: str
    name: str | None
    model_config = ConfigDict(from_attributes=True)


class GenreBaseSchema(BaseModel):
    id: int
    name: str
    model_config = ConfigDict(from_attributes=True)


class ActorBaseSchema(BaseModel):
    id: int
    name: str
    model_config = ConfigDict(from_attributes=True)


class MovieListItemSchema(BaseModel):
    id: int
    name: str
    date: datetime.date
    score: float
    overview: str
    model_config = ConfigDict(from_attributes=True)


class MovieListResponseSchema(BaseModel):
    movies: list[MovieListItemSchema]
    prev_page: str | None
    next_page: str | None
    total_pages: int
    total_items: int
