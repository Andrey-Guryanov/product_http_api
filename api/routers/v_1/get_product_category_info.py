from model.db_requests import get_product_category
from fastapi import APIRouter
from model.api_model import ProductsCategoriesResponse

router = APIRouter()


@router.get("/product_category", response_model=ProductsCategoriesResponse)
async def product() -> ProductsCategoriesResponse:
    all_product_category = await get_product_category()
    return ProductsCategoriesResponse(
        **all_product_category,
    )
