import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    email = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    datasets = relationship("Dataset", back_populates="owner")  # New relationship

class Dataset(Base):
    __tablename__ = 'datasets'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    images = Column(String, nullable=False)
    owner_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))  # New foreign key
    owner = relationship("User", back_populates="datasets")  # New relationship