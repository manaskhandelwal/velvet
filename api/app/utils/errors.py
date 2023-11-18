from fastapi import HTTPException
from starlette import status

def gen_error_obj(target:str, msg:str):
    return {"target": target, "msg": msg}

def duplicate_error(target:str, msg:str):
    return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=gen_error_obj(target, msg))