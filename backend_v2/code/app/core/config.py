import pathlib
import socket
from typing import Union, List, Optional, Dict, Any

from pydantic import BaseSettings, AnyHttpUrl, validator, PostgresDsn, EmailStr


class Settings(BaseSettings):
    SVC_PORT: int
    # Database
    DATABASE_PORT: int
    DATABASE_PASSWORD: str
    DATABASE_USER: str
    DATABASE_NAME: str
    DATABASE_HOST: str

    # @validator("ASYNC_DATABASE_URI", pre=True)
    # def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
    #     # if isinstance(v, str):
    #     #     return v
    #     # return PostgresDsn.build(
    #     #     scheme="postgresql+asyncpg",
    #     #     user=values.get("DATABASE_USER"),
    #     #     password=values.get("DATABASE_PASSWORD"),
    #     #     host=values.get("DATABASE_HOST"),
    #     #     port=str(values.get("DATABASE_PORT")),
    #     #     path=f"/{values.get('DATABASE_NAME') or ''}",
    #     # )
    #     return "postgresql://postgres:123rasulQq@localhost/UpTemAll"

    TEST_DATABASE: str = "test_db"
    ASYNC_TEST_DATABASE_URI: Optional[str] = "postgresql://postgres:123rasulQq@localhost/UpTemAll"

    @validator("ASYNC_TEST_DATABASE_URI", pre=True)
    def assemble_test_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=values.get("DATABASE_USER"),
            password=values.get("DATABASE_PASSWORD"),
            host=values.get("DATABASE_HOST"),
            port=str(values.get("DATABASE_PORT")),
            path=f"/{values.get('TEST_DATABASE') or ''}?prepared_statement_cache_size=0",
        )

    BACKEND_CORS_ORIGINS: Union[List[str], List[AnyHttpUrl]]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:

        env_file = f"{pathlib.Path(__file__).parents[3]}\.env"
        env_file_encoding = "utf-8"
        check_fields = False


settings = Settings()
