from typing import List
from pydantic import BaseModel


class ProductResponse(BaseModel):
    product_name: str
    categories: List


class CategoryResponse(BaseModel):
    category_name: str
    products: List


class CategoriesResponse(BaseModel):
    categories: List[CategoryResponse]


class ProductsResponse(BaseModel):
    products: List[ProductResponse]


class ProductCategoryResponse(BaseModel):
    product_name: str
    category_name: str


class ProductsCategoriesResponse(BaseModel):
    products_categories: list[ProductCategoryResponse]
