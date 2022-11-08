from starlette.testclient import TestClient
from run_api import app_api
from model.db_model import Base
from tests.conftest import engine, load_test_data, RESULT_TESTS
import pytest

client = TestClient(app_api)


class TestHome:
    def test_home(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == RESULT_TESTS["result_home"]


class TestNoDataAPI:
    @pytest.fixture()
    def test_db_no_data(self):
        Base.metadata.create_all(bind=engine)
        yield
        Base.metadata.drop_all(bind=engine)

    def test_all_products_no_data(self, test_db_no_data):
        response = client.get("/api/v1.0/all_products")
        assert response.status_code == 200
        assert response.json() == RESULT_TESTS["result_all_products_no_data"]

    def test_all_categories_no_data(self, test_db_no_data):
        response = client.get("/api/v1.0/all_categories")
        assert response.status_code == 200
        assert response.json() == RESULT_TESTS["result_all_categories_no_data"]

    def test_all_product_category_no_data(self, test_db_no_data):
        response = client.get("/api/v1.0/product_category")
        assert response.status_code == 200
        assert response.json() == RESULT_TESTS["test_all_product_category_no_data"]


class TestDataAPI:
    @pytest.fixture()
    def test_db_data(self):
        Base.metadata.create_all(bind=engine)
        load_test_data()
        yield
        Base.metadata.drop_all(bind=engine)

    def test_all_products_data(self, test_db_data):
        response = client.get("/api/v1.0/all_products")
        assert response.status_code == 200
        assert response.json() == RESULT_TESTS["result_all_products_data"]

    def test_all_product_category_data(self, test_db_data):
        response = client.get("/api/v1.0/all_categories")
        assert response.status_code == 200
        assert response.json() == RESULT_TESTS["result_all_categories_data"]

    def test_all_product_category_data(self, test_db_data):
        response = client.get("/api/v1.0/product_category")
        assert response.status_code == 200
        assert response.json() == RESULT_TESTS["test_all_product_category_data"]
