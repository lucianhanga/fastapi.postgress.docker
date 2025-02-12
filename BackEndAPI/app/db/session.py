from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Create the async database engine
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Create a sessionmaker for async sessions
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Dependency to get the database session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
