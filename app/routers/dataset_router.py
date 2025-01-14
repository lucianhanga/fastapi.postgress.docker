import logging
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.session import get_db
from app.db.models.dataset import Dataset
from app.schemas.dataset_schema import DatasetCreate, DatasetUpdate, DatasetResponse

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/", response_model=DatasetResponse, status_code=status.HTTP_201_CREATED)
async def create_dataset(dataset: DatasetCreate, db: AsyncSession = Depends(get_db)):
    logger.info("Received request to create dataset with name: %s", dataset.name)
    
    new_dataset = Dataset(
        name=dataset.name,
        description=dataset.description,
        images=dataset.images
    )
    db.add(new_dataset)
    await db.commit()
    await db.refresh(new_dataset)
    logger.info("Dataset created successfully with name: %s", dataset.name)
    return new_dataset

@router.put("/{dataset_id}", response_model=DatasetResponse)
async def update_dataset(dataset_id: uuid.UUID, dataset: DatasetUpdate, db: AsyncSession = Depends(get_db)):
    logger.info("Received request to update dataset with id: %s", dataset_id)
    
    existing_dataset = await db.execute(
        select(Dataset).where(Dataset.id == dataset_id)
    )
    dataset_obj = existing_dataset.scalar()
    if not dataset_obj:
        logger.warning("Dataset not found with id: %s", dataset_id)
        raise HTTPException(status_code=404, detail="Dataset not found")

    if dataset.name is not None:
        dataset_obj.name = dataset.name
    if dataset.description is not None:
        dataset_obj.description = dataset.description
    if dataset.images is not None:
        dataset_obj.images = dataset.images

    await db.commit()
    await db.refresh(dataset_obj)
    logger.info("Dataset updated successfully with id: %s", dataset_id)
    return dataset_obj

@router.delete("/{dataset_id}", response_model=DatasetResponse)
async def delete_dataset(dataset_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    logger.info("Received request to delete dataset with id: %s", dataset_id)
    
    existing_dataset = await db.execute(
        select(Dataset).where(Dataset.id == dataset_id)
    )
    dataset_obj = existing_dataset.scalar()
    if not dataset_obj:
        logger.warning("Dataset not found with id: %s", dataset_id)
        raise HTTPException(status_code=404, detail="Dataset not found")

    await db.delete(dataset_obj)
    await db.commit()
    logger.info("Dataset deleted successfully with id: %s", dataset_id)
    return dataset_obj

@router.get("/", response_model=list[DatasetResponse])
async def list_datasets(db: AsyncSession = Depends(get_db)):
    logger.info("Received request to list all datasets")
    
    result = await db.execute(select(Dataset))
    datasets = result.scalars().all()
    logger.info("Listed all datasets")
    return datasets

@router.get("/{dataset_id}", response_model=DatasetResponse)
async def get_dataset(dataset_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    logger.info("Received request to get dataset with id: %s", dataset_id)
    
    existing_dataset = await db.execute(
        select(Dataset).where(Dataset.id == dataset_id)
    )
    dataset_obj = existing_dataset.scalar()
    if not dataset_obj:
        logger.warning("Dataset not found with id: %s", dataset_id)
        raise HTTPException(status_code=404, detail="Dataset not found")

    logger.info("Dataset found with id: %s", dataset_id)
    return dataset_obj