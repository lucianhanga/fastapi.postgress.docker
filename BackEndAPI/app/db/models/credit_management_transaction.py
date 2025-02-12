import uuid
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db.models.base_class import Base

class CreditManagementTransaction(Base):
    __tablename__ = 'credit_management_transactions'

    transaction_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    owner_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    amount = Column(Integer, nullable=False)
    transaction_type = Column(String, nullable=False)
    external_reference = Column(String, nullable=True)
    status = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    processed_at = Column(DateTime, nullable=True)

    owner = relationship("User", back_populates="credit_management_transactions")

    __table_args__ = (
        CheckConstraint('amount != 0', name='check_amount_nonzero'),
        CheckConstraint("transaction_type IN ('credit_purchase', 'refund', 'manual_adjustment')", name='check_transaction_type'),
        CheckConstraint("status IN ('pending', 'completed', 'failed', 'reversed')", name='check_status'),
    )