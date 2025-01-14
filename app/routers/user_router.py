import logging
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.session import get_db
from app.db.models import User
from app.schemas.user_schema import UserCreate, UserUpdate, UserResponse

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    logger.info("Received request to create user with email: %s", user.email)
    
    existing_user = await db.execute(
        select(User).where(User.email == user.email)
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

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserUpdate, db: AsyncSession = Depends(get_db)):
    logger.info("Received request to update user with id: %d", user_id)
    
    existing_user = await db.execute(
        select(User).where(User.id == user_id)
    )
    user_obj = existing_user.scalar()
    if not user_obj:
        logger.warning("User not found with id: %d", user_id)
        raise HTTPException(status_code=404, detail="User not found")

    if user.name is not None:
        user_obj.name = user.name
    if user.description is not None:
        user_obj.description = user.description

    await db.commit()
    await db.refresh(user_obj)
    logger.info("User updated successfully with id: %d", user_id)
    return user_obj

@router.delete("/{user_id}", response_model=UserResponse)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    logger.info("Received request to delete user with id: %d", user_id)
    
    existing_user = await db.execute(
        select(User).where(User.id == user_id)
    )
    user_obj = existing_user.scalar()
    if not user_obj:
        logger.warning("User not found with id: %d", user_id)
        raise HTTPException(status_code=404, detail="User not found")

    await db.delete(user_obj)
    await db.commit()
    logger.info("User deleted successfully with id: %d", user_id)
    return user_obj

@router.get("/", response_model=list[UserResponse])
async def list_users(db: AsyncSession = Depends(get_db)):
    logger.info("Received request to list all users")
    
    result = await db.execute(select(User))
    users = result.scalars().all()
    logger.info("Listed all users")
    return users

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    logger.info("Received request to get user with id: %d", user_id)
    
    existing_user = await db.execute(
        select(User).where(User.id == user_id)
    )
    user_obj = existing_user.scalar()
    if not user_obj:
        logger.warning("User not found with id: %d", user_id)
        raise HTTPException(status_code=404, detail="User not found")

    logger.info("User found with id: %d", user_id)
    return user_obj
