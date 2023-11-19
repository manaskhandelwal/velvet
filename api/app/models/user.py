from sqlalchemy import Boolean, Column, Integer, String
from .base_table import BaseTable


class User(BaseTable):
    __tablename__ = "users"

    full_name = Column(String, index=True)
    username = Column(String, unique=True, index=True)
    pronouns = Column(String, nullable=True)
    bio = Column(String, nullable=True)
    profile_photo = Column(String, nullable=True)

    email = Column(String, unique=True)
    email_otp = Column(Integer, nullable=True)
    email_verified = Column(Boolean, default=False)

    total_following = Column(Integer, default=0)
    total_followers = Column(Integer, default=0)

    hashed_password = Column(String, nullable=False)

    private = Column(Boolean, default=False)
