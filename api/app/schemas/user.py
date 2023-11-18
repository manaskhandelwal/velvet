from pydantic import BaseModel, EmailStr, Field


class UserCreateDto(BaseModel):
    full_name: str = Field(min_length=1)
    username: str = Field(min_length=2)
    email: EmailStr = Field()
    password: str = Field(min_length=1)


class UserOtpVerifyDto(BaseModel):
    email_otp: int = Field()


class UserLoginDto(BaseModel):
    username: str = Field(min_length=2)
    password: str = Field(min_length=1)