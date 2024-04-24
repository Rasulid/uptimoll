import pathlib
from typing import Any
from pydantic import PostgresDsn, field_validator
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

BASE_DIR = pathlib.Path(__file__).parents[1]


class Settings(BaseSettings):
    load_dotenv()

    DATABASE_PORT: int
    DATABASE_PASSWORD: str
    DATABASE_USER: str
    DATABASE_NAME: str
    DATABASE_HOST: str

    SECRET_KEY: str
    AlGORITHM: str

    CLIENT_ID: str
    CLIENT_SECRET: str
    SUBDAMAIN: str
    REDIRECT_URL: str
    TOKEN_CODE: str

    DATABASE_URI: str | None = None

    @field_validator("DATABASE_URI", check_fields=False)
    def database_uri(cls, v: str, values: dict[str, Any]) -> str:
        return PostgresDsn.build(
            scheme="postgresql",
            username=values.data.get("DATABASE_USER"),
            password=values.data.get("DATABASE_PASSWORD"),
            host=values.data.get("DATABASE_HOST"),
            port=values.data.get("DATABASE_PORT"),
            path=f"{values.data.get('DATABASE_NAME') or ''}",
        )

    class Config:
        env_file = ".env"


settings = Settings()
