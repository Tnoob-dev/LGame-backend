from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from ..funcs import db_reqs
from ..utils import logs, db, schemas
from typing import List

log = logs.Logger()

router = APIRouter(
    prefix="/games",
    tags=["games"]
)

queries = db_reqs.DB_Game_Queries(db.engine, db.Game)

@router.get("/all", status_code=status.HTTP_200_OK, response_model=List[schemas.GameModel])
async def get_all_games():
    
    try:
        games = queries.get_all()
        all_games = []
        for game in games:
            all_games.append({
                "id": game.id,
                "name": game.name,
                "image": game.image,
                "description": game.description,
                "genre": game.genre,
                "console": game.console,
                "trailer": game.trailer
            })
            
        return JSONResponse(content=all_games,
                            status_code=status.HTTP_200_OK)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=str(e))

@router.get("/{game_name}", status_code=status.HTTP_200_OK, response_model=List[schemas.GameModel])
async def get_game(game_name: str):
    
    try:
        games = queries.get_game_by_name(game_name)
        all_games = []
        for game in games:
            all_games.append({
                "id": game.id,
                "name": game.name,
                "image": game.image,
                "description": game.description,
                "genre": game.genre,
                "console": game.console,
                "trailer": game.trailer
            })
            
        return JSONResponse(content=all_games,
                            status_code=status.HTTP_200_OK)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=str(e))

@router.get("/console/{console}", status_code=status.HTTP_200_OK, response_model=List[schemas.GameModel])
async def get_game_console(console: str):
    try:
        games = queries.get_games_by_console(console)
        all_games = []
        for game in games:
            all_games.append({
                "id": game.id,
                "name": game.name,
                "image": game.image,
                "description": game.description,
                "genre": game.genre,
                "console": game.console,
                "trailer": game.trailer
            })
            
        return JSONResponse(content=all_games,
                            status_code=status.HTTP_200_OK)
    except Exception as e:
        print(e)

@router.post("/add_game", status_code=status.HTTP_201_CREATED, response_model=schemas.Response)
async def add_games(game: schemas.GameModel):
    
    try:
        game = db.Game(name=game.name, image=game.image, genre=game.genre,
                       description=game.description, trailer=game.trailer, console=game.console)
        
        queries.insert(game)
        return JSONResponse(content={"message": "Game Added Successfully"}, 
                            status_code=status.HTTP_201_CREATED)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                            detail=str(e))

@router.delete("/delete/{game_id}", status_code=status.HTTP_200_OK, response_model=schemas.Response)
async def delete_game(game_id: int):
    
    try:
        queries.delete_game(game_id)
        return JSONResponse(content={"message": "Game deleted"},
                            status_code=status.HTTP_200_OK)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=str(e))