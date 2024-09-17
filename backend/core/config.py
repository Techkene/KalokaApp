from pydantic import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Kaloka"
    SQLALCHEMY_DATABASE_URI: str = "postgresql://user:password@localhost/dbname"
    SECRET_KEY: str = "" #create later
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
