from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Annotated

from models.moment import Moment
from utils.helpers import get_db, success_responce
from schemas.moment import MomentCreateDto
from core.security import get_current_user



router = APIRouter()
db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.post("/")
async def create_moment(user_dep: user_dependency, db: db_dependency, dto: MomentCreateDto):
    # FIX: Use NLP to check for negative content
    
    moment = Moment(message=dto.message, user_id=user_dep.get("id"))
    
    db.add(moment)
    db.commit()
    db.refresh(moment)
    
    return success_responce()



