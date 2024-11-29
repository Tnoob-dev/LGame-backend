from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter(
    tags=["/"]
)

@router.get("/", status_code=status.HTTP_200_OK)
async def home():
    return JSONResponse({"Hello": "World!"})