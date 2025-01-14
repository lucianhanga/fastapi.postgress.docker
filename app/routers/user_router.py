import logging
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.db.models import User
from app.schemas.user_schema import UserCreate, UserResponse

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    logger.info("Received request to create user with email: %s", user.email)
    
    existing_user = await db.execute(
        User.__table__.select().where(User.email == user.email)
    )
    if existing_user.scalar():
        logger.warning("Email already registered: %s", user.email)
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        email=user.email,
        name=user.name,
        description=user.description  # New field
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    logger.info("User created successfully with email: %s", user.email)
    return new_user
