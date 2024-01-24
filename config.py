import os

from dotenv import find_dotenv, load_dotenv
from pydantic import BaseSettings

load_dotenv(find_dotenv(".env"))


class Settings(BaseSettings):
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "postgres")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "postgres")
    POSTGRES_PORT: int = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "postgres")
    PGADMIN_EMAIL: str = os.getenv("PGADMIN_EMAIL", "admin@admin.com")
    PGADMIN_PASSWORD: str = os.getenv("PGADMIN_PASSWORD", "admin")
    DOCKER_HOST: str = os.getenv("DOCKER_HOST", "localhost")
    DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DOCKER_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"  # noqa: E501


if __name__ == "__main__":
    print(Settings().DATABASE_URL)
