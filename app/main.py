from fastapi import FastAPI
from app.db.models import Base
from app.db.session import engine
from app.routers import user_router, machines
import os
import logging

# Determine if running in Docker
in_docker = os.getenv('IN_DOCKER', 'False') == 'True'

# Set log directory based on environment
log_dir = '/app/logs' if in_docker else './logs'

# Ensure log directory exists
os.makedirs(log_dir, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=os.path.join(log_dir, 'app.log'),
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

logger = logging.getLogger(__name__)
logger.info('Logging setup complete.')

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
app.include_router(user_router.router, prefix="/users", tags=["users"])
app.include_router(machines.router, prefix="/machines", tags=["machines"])
