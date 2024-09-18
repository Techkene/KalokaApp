from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv('DB_CONNECTION_STRING')
secret = os.getenv('SECRET_KEY')

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Kaloka"
    SQLALCHEMY_DATABASE_URI: str = database_url
    SECRET_KEY: str = secret
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
