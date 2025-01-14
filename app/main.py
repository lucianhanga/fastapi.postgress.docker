from fastapi import FastAPI
from app.db.models import Base, engine
from app.routers import user_router

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(user_router.router, prefix="/users", tags=["Users"])
