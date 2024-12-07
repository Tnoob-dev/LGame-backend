from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from .src.routes import home, games
from .src.utils import logs, db

log = logs.Logger()

@asynccontextmanager
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

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(home.router)
app.include_router(games.router)