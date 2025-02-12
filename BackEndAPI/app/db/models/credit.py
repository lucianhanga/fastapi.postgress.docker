import uuid
from sqlalchemy import Column, Integer, DateTime, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.models.base_class import Base

class Credit(Base):
    __tablename__ = 'credits'

    owner_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), primary_key=True)
    total_credits = Column(Integer, nullable=False)
    last_update = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    owner = relationship("User", back_populates="credits")
    
    
