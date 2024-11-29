from fastapi import FastAPI
from .src.routes import home, games
from .src.utils import logs, db

log = logs.Logger()

async def lifespan(app: FastAPI):
    try:
        log.info("App Started")
        db.create_tables()
        yield
    finally:
        log.info("App Closed")

app = FastAPI(
    title="LGame-Backend",
    version="1.0.0",
    lifespan=lifespan
)


app.include_router(home.router)
app.include_router(games.router)