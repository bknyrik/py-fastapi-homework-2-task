import datetime

from pydantic import BaseModel, ConfigDict, Field

from src.database.models import MovieStatusEnum


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


class LanguageBaseSchema(BaseModel):
    id: int
    name: str
    model_config = ConfigDict(from_attributes=True)


class MovieBaseSchema(BaseModel):
    id: int
    name: str
    date: datetime.date
    score: float
    overview: str


class MovieListItemSchema(MovieBaseSchema):
    model_config = ConfigDict(from_attributes=True)


class MovieListResponseSchema(BaseModel):
    movies: list[MovieListItemSchema]
    prev_page: str | None
    next_page: str | None
    total_pages: int
    total_items: int


class MovieDetailSchema(MovieBaseSchema):
    status: MovieStatusEnum
    budget: float
    revenue: float
    country: CountryBaseSchema
    genres: list[GenreBaseSchema]
    actors: list[ActorBaseSchema]
    languages: list[LanguageBaseSchema]


class MovieCreateSchema(MovieBaseSchema):
    status: MovieStatusEnum
    budget: float = Field(ge=1)
    revenue: float= Field(ge=1)
    country: str
    genres: list[str]
    actors: list[str]
    languages: list[str]
