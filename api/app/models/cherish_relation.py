from sqlalchemy import UUID, Column
from .base_table import BaseTable


class CherishRelation(BaseTable):
    __tablename__ = "cherish_relation"

    user_id = Column(UUID(as_uuid=True), index=True)
    moment_id = Column(UUID(as_uuid=True), index=True)
