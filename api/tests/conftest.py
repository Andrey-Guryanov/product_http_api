import os
import yaml
from typing import Callable, Union, NoReturn
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.db_model import ProductsDB, CategoriesDB, ProductCategoryDB

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

test_products = ["product_1", "product_2", "product_3"]
test_categories = [
    "category_1",
    "category_2",
    "category_3",
]
test_products_category = [
    [1, 1],
    [1, 2],
    [2, 1],
]


def load_result(result_path="./tests/result_tests.yaml") -> dict:
    with open(result_path) as file_settings:
        result_tests = yaml.load(file_settings, Loader=yaml.FullLoader)
    return result_tests


RESULT_TESTS = load_result()


def new_product(product_name: str) -> ProductsDB:
    product = ProductsDB(product_name=product_name)
    return product


def new_category(category_name: str) -> CategoriesDB:
    category = CategoriesDB(category_name=category_name)
    return category


def new_product_category(products_category_id: list) -> ProductCategoryDB:
    product_category = ProductCategoryDB(
        product_id=products_category_id[0], category_id=products_category_id[1]
    )
    return product_category


def save_data_test_db(
    session, add_func: Callable, dataset: Union[str, list]
) -> NoReturn:
    for data in dataset:
        session.add(add_func(data))
    session.commit()


def load_test_data() -> NoReturn:
    Session = sessionmaker(bind=engine)
    session = Session()
    save_data_test_db(session, new_product, test_products)
    save_data_test_db(session, new_category, test_categories)
    save_data_test_db(session, new_product_category, test_products_category)
    session.close()
