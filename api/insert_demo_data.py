import csv

from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.sql import insert
from sqlalchemy.orm import sessionmaker
from model.db_model import ProductsDB, CategoriesDB, ProductCategoryDB
from constants import DB_USER, DB_PASSWORD, DB_NAME
from typing import NoReturn


def insert_data_demo() -> NoReturn:
    engine = create_engine(
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@postgres_db:5432/{DB_NAME}"
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    demo_files = {
        "CategoriesDB": [CategoriesDB, "category.csv"],
        "ProductsDB": [ProductsDB, "products.csv"],
        "ProductCategoryDB": [ProductCategoryDB, "product_category.csv"],
    }

    demo_folder = Path("./demo_data/")
    for table_name in demo_files.keys():
        insert_data = []
        with open(
            demo_folder / demo_files[table_name][1], "r", newline="", encoding="utf-8"
        ) as csvfile:
            csv_reader = csv.DictReader(csvfile, delimiter=";")
            for data in csv_reader:
                insert_data.append(data)

        insert_table = insert(demo_files[table_name][0])
        insert_table = insert_table.values(insert_data)

        try:
            session.execute(insert_table)
        except:
            pass
        else:
            session.commit()

    session.close()


if __name__ == "__main__":
    insert_data_demo()
