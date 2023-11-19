from sqlalchemy import UUID, Column
from .base_table import BaseTable


class FollowRelation(BaseTable):
    __tablename__ = "follow_relation"

    user_id = Column(UUID(as_uuid=True), index=True)
    followed_user_id = Column(UUID(as_uuid=True), index=True)
