from fastapi import HTTPException
from starlette import status



def gen_error_obj(target:str, msg:str):
    return {"target": target, "msg": msg}


def duplicate_error(target:str, msg:str):
    return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=gen_error_obj(target, msg))


def not_found_error(target:str, msg:str):
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=gen_error_obj(target, msg))


def conflit_error(target:str, msg:str):
    return HTTPException(status_code=status.HTTP_409_CONFLICT, detail=gen_error_obj(target, msg))


def unauthorized_error(target:str):
    return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=gen_error_obj(target, "You are not authorized to access that."))