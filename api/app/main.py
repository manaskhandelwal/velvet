import sys

sys.dont_write_bytecode = True

from fastapi import FastAPI

from dotenv import load_dotenv

from routes import auth, user, moment
from core.config import settings

load_dotenv()


def api(path: str):
    return settings.API_PREFIX + path


app = FastAPI(
    title=settings.PROJECT_NAME,
)

app.include_router(auth.router, prefix=api("/auth"), tags=["auth"])
app.include_router(user.router, prefix=api("/user"), tags=["user"])
app.include_router(moment.router, prefix=api("/moment"), tags=["moment"])
