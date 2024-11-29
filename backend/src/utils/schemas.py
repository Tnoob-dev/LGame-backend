from pydantic import BaseModel
from typing import List

class Response(BaseModel):
    message: str
    
class GameModel(BaseModel):
    name: str
    image: str
    main_platform: str
    platforms: List[str]
    description: str
    trailer: str