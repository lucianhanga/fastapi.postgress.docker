import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.models.base_class import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    email = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    datasets = relationship("Dataset", back_populates="owner")
    trainings = relationship("Training", back_populates="owner")
    credits = relationship("Credit", back_populates="owner", uselist=False)
    credit_transactions = relationship("CreditTransaction", back_populates="owner")  # New relationship


