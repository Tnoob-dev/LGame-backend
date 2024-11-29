from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from ..utils import schemas

router = APIRouter(
    tags=["/"]
)

@router.get("/", status_code=status.HTTP_200_OK, response_model=schemas.Response)
async def home():
    return JSONResponse(content={"Hello": "World!"}, status_code=status.HTTP_200_OK)