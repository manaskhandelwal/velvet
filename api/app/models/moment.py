import uuid
from sqlalchemy import UUID, Column, String, Boolean

from db.session import Base


class Moment(Base):
    __tablename__ = "moments"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True)
    user_id = Column(UUID(as_uuid=True), index=True)

    message = Column(String, nullable=True)
    photo = Column(String, nullable=True)

    private = Column(Boolean, default=False)
