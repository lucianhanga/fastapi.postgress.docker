import uuid
from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.models.base_class import Base

class Generation(Base):
    __tablename__ = 'generations'

    generation_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    prompt = Column(String, nullable=False)
    description = Column(String, nullable=True)
    start_date = Column(DateTime, default=func.now(), nullable=False)
    time_taken = Column(Float, nullable=False)
    model = Column(String, nullable=False)  # Temporary field for now until the model is defined
    image = Column(String, nullable=False)
    owner_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)

    owner = relationship("User", back_populates="generations")