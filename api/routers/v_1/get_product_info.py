from model.db_requests import get_products
from fastapi import APIRouter
from model.api_model import ProductsResponse

router = APIRouter()


@router.get("/all_products", response_model=ProductsResponse)
async def product() -> ProductsResponse:
    all_product = await get_products()
    return ProductsResponse(
        **all_product,
    )
