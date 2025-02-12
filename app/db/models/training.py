import uuid
from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.models.base_class import Base

class Training(Base):
    __tablename__ = 'trainings'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, nullable=False)
    base_model = Column(String, nullable=False)
    imgs_count = Column(Integer, nullable=False)
    time_taken = Column(Float, nullable=False)
    start_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    owner_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    dataset_id = Column(UUID(as_uuid=True), ForeignKey('datasets.id'))
    owner = relationship("User", back_populates="trainings")
    dataset = relationship("Dataset", back_populates="trainings")