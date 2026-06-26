from sqlalchemy.orm import Session
from app import models, schemas

import logging

logger = logging.getLogger(__name__)

# Busca todos os filmes do banco (nao precisa de id)
def get_movies(db: Session):
    logger.info("Buscando todos os filmes")
    return db.query(models.Movie).all()

# Busca os filmes do banco (precisa de id)
def get_movie_by_id(db: Session, movie_id: int):
    logger.info(f"Buscando filme com id {movie_id}")
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()

# Cria um filme dentro do banco
def create_movie(db: Session, movie: schemas.MovieCreate):
    logger.info(f"Criando filme: {movie.name}")
    db_movie = models.Movie(**movie.model_dump())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

# Atualiza os dados de um filme criado (precisa de id)
def update_movie(db: Session, movie_id: int, movie: schemas.MovieCreate):
    logger.info(f"Atualizando filme com id {movie_id}")
    db_movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if not db_movie:
        return None
    for key, value in movie.model_dump().items():
        setattr(db_movie, key, value)
    db.commit()
    db.refresh(db_movie)
    return db_movie

# Deleta um filme do banco (precisa de id)
def delete_movie(db: Session, movie_id: int):
    logger.info(f"Deletando filme com id {movie_id}")
    db_movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if not db_movie:
        return None
    db.delete(db_movie)
    db.commit()
    return db_movie