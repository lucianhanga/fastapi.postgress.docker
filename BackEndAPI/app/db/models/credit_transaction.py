import uuid
from sqlalchemy import Column, Integer, DateTime, ForeignKey, String, func, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.models.base_class import Base

class CreditTransaction(Base):
    __tablename__ = 'credit_transactions'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    owner_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    amount = Column(Integer, nullable=False)
    transaction_date = Column(DateTime, default=func.now(), nullable=False)
    feature = Column(String, nullable=False)  # Temporary field for now until the features are defined

    owner = relationship("User", back_populates="credit_transactions")

    __table_args__ = (
        CheckConstraint('amount > 0', name='check_amount_positive'),
    )