import sys

sys.dont_write_bytecode = True

from fastapi import FastAPI
import cloudinary
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from routes import auth, user, moment
from core.config import settings

load_dotenv()


def api(path: str):
    return settings.API_PREFIX + path


app = FastAPI(
    title=settings.PROJECT_NAME,
)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cloudinary.config(
    cloud_name=settings.CLOUDINARY_CLOUD_NAME,
    api_key=settings.CLOUDINARY_API_KEY,
    api_secret=settings.CLOUDINARY_API_SECRET,
)

app.include_router(auth.router, prefix=api("/auth"), tags=["auth"])
app.include_router(user.router, prefix=api("/user"), tags=["user"])
app.include_router(moment.router, prefix=api("/moment"), tags=["moment"])
