
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/movies", tags=["Movies"])

@router.get("/", response_model=list[schemas.MovieResponse])
def get_movies(db: Session = Depends(get_db)):
    return crud.get_movies(db)

@router.get("/{movie_id}", response_model=schemas.MovieResponse)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = crud.get_movie_by_id(db, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return movie

@router.post("/", response_model=schemas.MovieResponse, status_code=201)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    return crud.create_movie(db, movie)

@router.put("/{movie_id}", response_model=schemas.MovieResponse)
def update_movie(movie_id: int, movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    db_movie = crud.update_movie(db, movie_id, movie)
    if not db_movie:
        raise HTTPException(status_code=404, detail="Filme não encontrado")
    return db_movie

@router.delete("/{movie_id}", status_code=204)
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = crud.delete_movie(db, movie_id)
    if not db_movie:
        raise HTTPException(status_code=404, detail="Filme não encontrado")