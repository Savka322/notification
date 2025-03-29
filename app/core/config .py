from pydantic import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Notification Service"
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./test.db"

    class Config:
        case_sensitive = True

settings = Settings()