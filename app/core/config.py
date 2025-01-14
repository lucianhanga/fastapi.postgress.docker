from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://myuser:mypassword@db/mydb"

settings = Settings()
