import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.models.base_class import Base

class Dataset(Base):
    __tablename__ = 'datasets'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    images = Column(String, nullable=False)
    owner_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    owner = relationship("User", back_populates="datasets")
    trainings = relationship("Training", back_populates="dataset")