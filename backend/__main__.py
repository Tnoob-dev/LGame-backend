from collections.abc import AsyncIterator
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from redis import asyncio as aioredis
from contextlib import asynccontextmanager
from .src.routes import home, games
from .src.utils import logs, db

log = logs.Logger()

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    try:
        log.info("App Started")
        db.create_tables()
        redis = aioredis.from_url("redis://localhost")
        FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
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

@cache()
async def get_cache():
    return 1

app.include_router(home.router)
app.include_router(games.router)