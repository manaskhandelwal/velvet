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

    ACCESS_TOKEN_SECRET_KEY: str = config.get("ACCESS_TOKEN_SECRET_KEY")
    ACCESS_TOKEN_ALGORITHM: str = "HS256"
    # 60 minutes * 24 hours * 15 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 15
    
    BREVO_API_ENDPOINT: str = config.get("BREVO_API_ENDPOINT")
    BREVO_API_KEY: str = config.get("BREVO_API_KEY")


settings = Settings()
