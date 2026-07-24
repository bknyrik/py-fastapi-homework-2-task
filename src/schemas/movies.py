import datetime

from pydantic import BaseModel, ConfigDict


class MovieListItemSchema(BaseModel):
    id: int
    name: str
    date: datetime.date
    score: float
    overview: str
    model_config = ConfigDict(from_attributes=True)
