from datetime import datetime
import uuid
from sqlalchemy import UUID, Column, DateTime
from db.session import Base


class BaseTable(Base):
    __abstract__ = True

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
