import uuid
from sqlalchemy import UUID, Boolean, Column, Integer, String, Table, ForeignKey
from db.session import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True)

    full_name = Column(String, index=True)
    username = Column(String, unique=True, index=True)
    pronouns = Column(String, nullable=True)
    bio = Column(String, nullable=True)
    profile_photo = Column(String, nullable=True)

    email = Column(String, unique=True)
    email_otp = Column(Integer, nullable=True)
    email_verified = Column(Boolean, default=False)

    hashed_password = Column(String, nullable=False)
