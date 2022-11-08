from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/")
async def home_page(request: Request) -> dict:
    return {"key": "Hi bro!"}
