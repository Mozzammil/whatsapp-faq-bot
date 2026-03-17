import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from app.db.base import Base


class FAQ(Base):
    __tablename__ = "faqs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    business_id = Column(UUID(as_uuid=True), ForeignKey("businesses.id"), nullable=False)

    keywords = Column(String, nullable=False)  # comma-separated
    answer = Column(Text, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)