from sqlmodel import SQLModel, Field, create_engine, JSON, Column, Relationship, Session, select
from typing import Optional, List
from .logs import Logger
import os

log = Logger()

class Game(SQLModel, table=True):
    id: Optional[int] | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    image: str = Field()
    genre: List[str] = Field(sa_column=Column(JSON))
    description: str = Field()
    trailer: str = Field()
    console: str = Field(default=None)

lgame_sqliteDB = "sqlite:///./backend/src/core/GamesDB.db"

engine = create_engine(lgame_sqliteDB)

def create_tables():
    try:
        for table in SQLModel.metadata.tables.values():
            if not engine.dialect.has_table(engine.connect(), table.name):    
                log.info(f"Creating Table {table.name}")
                table.create(engine)
                
        log.info("All Tables created")
    
    except Exception as e:
        log.error(e)