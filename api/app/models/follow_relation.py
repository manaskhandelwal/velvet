import uuid
from sqlalchemy import UUID, Column

from db.session import Base


class FollowRelation(Base):
    __tablename__ = "follow_relation"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True)
    user_id = Column(UUID(as_uuid=True), index=True)
    followed_user_id = Column(UUID(as_uuid=True), index=True)
