from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from ..funcs import db_reqs
from ..utils import logs, db

log = logs.Logger()

router = APIRouter(
    prefix="/games",
    tags=["/games"]
)

queries = db_reqs.DB_Queries()

@router.post("/add_game/", status_code=status.HTTP_201_CREATED)
async def add(game: db.Game):
    try:
        queries.insert(game)
        log.info("Success")
        return JSONResponse({"message": "Game Added Successfully"}, 
                            status_code=status.HTTP_201_CREATED)
    except Exception as e:
        log.error(f"Error -> {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                            detail=str(e))