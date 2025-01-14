from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

class Settings(BaseSettings):
    # DATABASE_URL: str = os.getenv("DATABASE_URL")
    DATABASE_URL: str = "postgresql+asyncpg://myuser:mypassword@localhost:5432/mydb"

settings = Settings()

# Print the DATABASE_URL to verify it's loaded correctly
print(f"DATABASE_URL: {settings.DATABASE_URL}")
