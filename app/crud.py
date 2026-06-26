from sqlalchemy.orm import Session
from app import models, schemas

def get_movies(db: Session):
    return db.query(models.Movie).all()

def get_movie_by_id(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()

def create_movie(db: Session, movie: schemas.MovieCreate):
    db_movie = models.Movie(**movie.model_dump())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie