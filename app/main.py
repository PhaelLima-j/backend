from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from app.routers import movies, health
from app.database import engine
from app import models

models.Base.metadata.create_all(bind=engine)

# Configuraçoes iniciais do FastAPI
app = FastAPI(
    title="Movies API",
    description="CRUD de Filmes",
    version="1.0.0",
    docs_url=None
)

# Inclusão das rotas
app.include_router(movies.router)
app.include_router(health.router)

# Inclusão do scalar, ao inves da documentaçao padrao do fastapi
@app.get("/docs", include_in_schema=False)
def scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title
    )