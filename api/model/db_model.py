from sqlalchemy import (
    Integer,
    String,
    Column,
    ForeignKey,
    UniqueConstraint,
)
import databases
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ProductsDB(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    product_name = Column(String(100), nullable=False, unique=True)


class CategoriesDB(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    category_name = Column(String(100), nullable=False, unique=True)


class ProductCategoryDB(Base):
    __tablename__ = "product_category"
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    __table_args__ = (
        UniqueConstraint("product_id", "category_id", name="unique_product_category"),
    )


def connect_db(
    user: str,
    password: str,
    db_name: str,
    db_type: str,
    port=5432,
    host="postgres_db",
    path="./test.db",
) -> databases.core.Database:
    match db_type:
        case "PostgreSQL":
            db_connect = databases.Database(
                f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}"
            )
        case "SQLite":
            db_connect = databases.Database(f"sqlite+aiosqlite:///{path}")
    return db_connect
