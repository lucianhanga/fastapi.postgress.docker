from fastapi import FastAPI
from app.db.models import Base
from app.db.session import engine
from app.routers import user_router
import os

# Set up logging
LOG_DIR = "/app/logs"
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=f"{LOG_DIR}/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Application has started")

@app.on_event("shutdown")
async def shutdown():
    logger.info("Application has stopped")

# Add your routers
app.include_router(user_router.router, prefix="/users", tags=["Users"])
