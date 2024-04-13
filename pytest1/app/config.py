from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

API_PREFIX = "/api"

POSTGRES_USER = config("POSTGRES_USER", cast=str)
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=str)
POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="db")
POSTGRES_PORT = config("POSTGRES_PORT", cast=str, default="5432")
POSTGRES_DB = config("POSTGRES_DB", cast=str)
DATABASE_URL = config(
    "DATABASE_URL",
    default="postgresql://"
            f"{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
            f"{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
)
