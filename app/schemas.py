# app/schemas.py
from pydantic import BaseModel, Field

class MovieCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    duration: int = Field(gt=0)
    director: str = Field(min_length=1, max_length=100)
    genre: str = Field(min_length=1, max_length=50)

class MovieResponse(MovieCreate):
    id: int

    class Config:
        from_attributes = True