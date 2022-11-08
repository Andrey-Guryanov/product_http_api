import os

from dotenv import load_dotenv
from model.db_model import connect_db

load_dotenv()

LOG_LEVEL = os.environ.get("LOG_LEVEL")
LOG_ROTATION = os.environ.get("LOG_ROTATION")

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")
DB_PORT = int(os.environ.get("DB_PORT"))
DB_TYPE = os.environ.get("DB_TYPE")

if DB_TYPE is None:
    DB_TYPE = "PostgreSQL"

DB_DATABASE = connect_db(DB_USER, DB_PASSWORD, DB_NAME, DB_TYPE)

if LOG_LEVEL is None:
    LOG_LEVEL = "ERROR"

if LOG_ROTATION is None:
    LOG_ROTATION = "100 MB"