from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db

# Banco de teste (esta separado)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_movie():
    response = client.post("/movies/", json={
        "name": "The Godfather",
        "duration": 175,
        "director": "Francis Ford Coppola",
        "genre": "Crime"
    })
    assert response.status_code == 201
    assert response.json()["name"] == "The Godfather"

def test_get_movies():
    response = client.get("/movies/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_movie():
    response = client.get("/movies/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_get_movie_not_found():
    response = client.get("/movies/999")
    assert response.status_code == 404

def test_delete_movie():
    response = client.delete("/movies/1")
    assert response.status_code == 204