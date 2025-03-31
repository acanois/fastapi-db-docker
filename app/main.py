"""API Main"""

from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse

from sqlmodel import Session

from .routers import user, auth

from .database import get_session

SessionDep = Annotated[Session, Depends(get_session)]


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
async def home():
    return RedirectResponse("/docs")
