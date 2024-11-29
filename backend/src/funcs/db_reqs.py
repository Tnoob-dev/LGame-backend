from sqlmodel import Session, select
from fastapi.responses import JSONResponse
from ..utils.db import engine, Game


class DB_Queries:
    def __init__(self) -> None:
        self.engine = engine
    
    def insert(self, game: Game) -> str:
        try:
            if not self.check_if_exists(game.name):
                with Session(self.engine) as session:
                    session.add(game)
                    session.commit()
                return JSONResponse({"": ""})
            else:
                return JSONResponse({"message": "Game Already Exists"})
        except Exception as e:
            raise str(e)
    
    def get_game_by_name(self, game_name: str):
         with Session(self.engine) as session:
            statement = select(self.object).where(Game.name == game_name)
            result = session.exec(statement).first()
            return result
                
    def check_if_exists(self, game_name: str) -> bool:
        return bool(self.get_game_by_name(game_name))