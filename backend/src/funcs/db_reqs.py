from sqlmodel import Session, select
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from ..utils import db, logs
from typing import List, Any, Type

log = logs.Logger()

class DB_Queries:
    def __init__(self, engine: Any, object: Type[db.Game]) -> None:
        self.engine = engine
        self.object = object
    
    def insert(self, game: db.Game) -> str:
        try:
            log.info("Inserting new game...")
            with Session(self.engine) as session:
                session.add(game)
                session.commit()
            log.info("Success")  
        except Exception as e:
            log.error(f"Error -> {e}")
            raise str(e)

    def get_all(self) -> List[db.Game]:
        try:
            log.info("Obtaining all the games")
            with Session(self.engine) as session:
                statement = select(self.object)
                result = session.exec(statement).all()
                return [games for games in result]
        except Exception as e:
            log.error(f"Error -> {e}")
            raise str(e)
    
    def get_game_by_name(self, game_name: str) -> db.Game | None:
        try:
            log.info(f"Obtaining {game_name}")    
            with Session(self.engine) as session:
                statement = select(self.object).where(db.Game.name == game_name)
                result = session.exec(statement).first()
                return result
        except Exception as e:
            log.error(f"Error -> {e}")
            raise str(e)
    
    def delete_game(self, game_id: int) -> JSONResponse:
        try:
            log.info("Deleting Game by ID")
            with Session(self.engine) as session:
                statement = select(self.object).where(
                    self.object.id == game_id)
                result = session.exec(statement)
                game = result.first()

                if game:
                        session.delete(game)
                        log.info("Game Deleted")
                        session.commit()
                        return {"message": "Game deleted"}
                else:
                    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            session.rollback()
            log.error(f"Error -> {e}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"ERROR: {e}")