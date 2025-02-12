from fastapi import FastAPI
from app.routers import filemanager

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

@app.get("/")
async def read_root():
    return {"message": "Welcome to FileMgrAPI"}

# Include the filemanager router
app.include_router(filemanager.router, prefix="/filemanager", tags=["filemanager"])

