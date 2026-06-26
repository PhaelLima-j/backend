from app.database import SessionLocal
from app import models


def seed():
    db = SessionLocal()

    movies = [
        models.Movie(name="The Godfather", duration=175, director="Francis Ford Coppola", genre="Crime"),
        models.Movie(name="The Dark Knight", duration=152, director="Christopher Nolan", genre="Ação"),
        models.Movie(name="Pulp Fiction", duration=154, director="Quentin Tarantino", genre="Crime"),
    ]

    db.add_all(movies)
    db.commit()
    db.close()
    print("Seed concluído!")


if __name__ == "__main__":
    seed()