from model.db_requests import get_categories
from fastapi import APIRouter
from model.api_model import CategoriesResponse

router = APIRouter()


@router.get("/all_categories", response_model=CategoriesResponse)
async def product() -> CategoriesResponse:
    all_categories = await get_categories()
    return CategoriesResponse(
        **all_categories,
    )
