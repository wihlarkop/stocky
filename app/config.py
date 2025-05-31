from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "FastAPI"
    APP_VERSION: str = "0.1.0"
    HOST: str = "localhost"
    PORT: int = 8000
    DEBUG: bool = 1
    SECRET_KEY: str = "secret"

settings = Settings()