import sys

sys.dont_write_bytecode = True

from fastapi import FastAPI

from dotenv import load_dotenv

from routes import auth
from core.config import settings

load_dotenv()


def api(path: str):
    return settings.API_PREFIX + path


app = FastAPI(
    title=settings.PROJECT_NAME,
)

app.include_router(auth.router, prefix=api("/auth"), tags=["auth"])
