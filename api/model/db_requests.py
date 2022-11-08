from sqlalchemy import select
from constants import DB_DATABASE
from .api_model import (
    ProductResponse,
    CategoryResponse,
    ProductCategoryResponse,
)
from .db_model import ProductsDB, CategoriesDB, ProductCategoryDB


async def _db_get_categories(database=DB_DATABASE) -> list:
    query = (
        select([CategoriesDB.category_name, ProductsDB.product_name])
        .join(
            ProductCategoryDB,
            ProductCategoryDB.category_id == CategoriesDB.id,
            isouter=True,
        )
        .join(ProductsDB, ProductsDB.id == ProductCategoryDB.product_id, isouter=True)
        .order_by(CategoriesDB.category_name)
        .group_by(CategoriesDB.category_name, ProductsDB.product_name)
    )
    return await database.fetch_all(query)


async def _db_get_products(database=DB_DATABASE) -> list:
    query = (
        select([ProductsDB.product_name, CategoriesDB.category_name])
        .join(
            ProductCategoryDB,
            ProductCategoryDB.product_id == ProductsDB.id,
            isouter=True,
        )
        .join(
            CategoriesDB, CategoriesDB.id == ProductCategoryDB.category_id, isouter=True
        )
        .order_by(ProductsDB.product_name)
        .group_by(ProductsDB.product_name, CategoriesDB.category_name)
    )
    return await database.fetch_all(query)


async def _db_get_product_category(database=DB_DATABASE) -> list:
    query = (
        select([ProductsDB.product_name, CategoriesDB.category_name])
        .join(ProductCategoryDB, ProductCategoryDB.product_id == ProductsDB.id)
        .join(CategoriesDB, CategoriesDB.id == ProductCategoryDB.category_id)
        .order_by(ProductsDB.product_name)
        .order_by(ProductsDB.product_name)
        .group_by(ProductsDB.product_name, CategoriesDB.category_name)
    )
    return await database.fetch_all(query)


async def get_products() -> dict:
    products_result = []
    categories = []
    products_select = await _db_get_products()
    try:
        products_previous = products_select[0].product_name
    except IndexError:
        products_previous = ""
    for products in products_select:
        if products.product_name != products_previous:
            products_result.append(
                ProductResponse(product_name=products_previous, categories=categories)
            )
            products_previous = products.product_name
            categories = []
        if products.category_name is not None:
            categories.append(products.category_name)
    if products_previous != "":
        products_result.append(
            ProductResponse(product_name=products_previous, categories=categories)
        )
    return {"products": products_result}


async def get_categories() -> dict:
    categories_result = []
    products = []
    categories_select = await _db_get_categories()
    try:
        categories_previous = categories_select[0].category_name
    except IndexError:
        categories_previous = ""
    for categories in categories_select:
        if categories.category_name != categories_previous:
            categories_result.append(
                CategoryResponse(category_name=categories_previous, products=products)
            )
            categories_previous = categories.category_name
            products = []
        if categories.product_name is not None:
            products.append(categories.product_name)
    if categories_previous != "":
        categories_result.append(
            CategoryResponse(category_name=categories_previous, products=products)
        )
    return {"categories": categories_result}


async def get_product_category() -> dict:
    product_category_result = []
    product_category_select = await _db_get_product_category()
    for products in product_category_select:
        product_category_result.append(
            ProductCategoryResponse(
                product_name=products.product_name, category_name=products.category_name
            )
        )
    return {"products_categories": product_category_result}
