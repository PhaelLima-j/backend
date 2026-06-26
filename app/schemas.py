from pydantic import BaseModel, Field, ConfigDict

class MovieCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    duration: int = Field(gt=0)
    director: str = Field(min_length=1, max_length=100)
    genre: str = Field(min_length=1, max_length=50)

class MovieResponse(MovieCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)