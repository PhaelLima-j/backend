from pydantic import BaseModel

class MovieCreate(BaseModel):
    name: str
    duration: int
    director: str
    genre: str

class MovieResponse(MovieCreate):
    id: int

    class Config:
        from_attributes = True