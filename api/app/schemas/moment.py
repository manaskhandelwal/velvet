from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class MomentCreateDto(BaseModel):
    message: Optional[str] = Field(min_length=1)
    photo: Optional[str] = Field(min_length=2)
