# product_http_api
HTTP API - FastAPI (async),  SQLAlchemy, PostgreSQL (+ асинхронный драйвер Databases), Nginx.
Разворачивается в docker-compose.

## Быстрый старт

1. В директории с проектом создаёте файл ".env" со следующим содержанием:
```
API_PORT=<порт для api - например 8088>

DB_USER=<имя пользователя базы данных>
DB_PASSWORD=<пароль пользователя базы данных>
DB_NAME=<наименование базы>
DB_PORT=<порт для базы данных - например 5432>
````
В качестве примера можно использовать файл ".env_example".

2.
   * В директории с проектом выполните ```docker-compose up -d --build```.
   * Для запуска тестов выполните ```docker-compose exec api_service pytest -v .```
   * Для загрузки в базу тестовых данных выполните ```docker-compose exec api_service python insert_demo_data.py```

### Методы

После запуска документация Swagger доступна по ```http://host:api_port/api/v1.0/docs``` (например http://localhost:8088/api/v1.0/docs)

* GET ```http://host:api_port/api/v1.0/all_products``` - список продуктов с категориями, отсортированы по алфавиту
* GET ```http://host:api_port/api/v1.0/all_categories```- список категорий с продуктами, отсортированы по алфавиту
* GET ```http://host:api_port/api/v1.0/product_category``` - список пар продукт - категория, отсортированы по алфавиту (по продукту)
