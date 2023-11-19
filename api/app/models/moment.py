from sqlalchemy import UUID, Column, String, Boolean, Integer
from .base_table import BaseTable


class Moment(BaseTable):
    __tablename__ = "moments"

    user_id = Column(UUID(as_uuid=True), index=True)

    message = Column(String, nullable=True)
    photo = Column(String, nullable=True)

    total_cherishes = Column(Integer, default=0)

    private = Column(Boolean, default=False)
