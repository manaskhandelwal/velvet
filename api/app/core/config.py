import os
from typing import Any, Dict, Optional
from pydantic import PostgresDsn, validator

from pydantic_settings import BaseSettings
from dotenv import dotenv_values

config = {
    **dotenv_values("../.env"),  # load shared development variables
    **dotenv_values("../.env.docker-compose"),  # load sensitive variables
    **os.environ,  # override loaded values with environment variables
}


class Settings(BaseSettings):
    PROJECT_NAME: str = "Velvet API"
    API_PREFIX: str = "/api"

    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v

        return PostgresDsn.build(
            scheme="postgresql",
            username=config.get("POSTGRES_USERNAME"),
            password=config.get("POSTGRES_PASSWORD"),
            host=config.get("POSTGRES_HOST"),
            port=int(config.get("POSTGRES_PORT")),
            path=config.get("POSTGRES_DATABASE_NAME"),
        )


settings = Settings()
