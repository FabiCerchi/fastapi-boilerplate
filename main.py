from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.v1.endpoints.user import user_router
from app.api.v1.endpoints.auth import auth_router
from app.db.initialize_db import create_superuser

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_superuser()
    yield
app = FastAPI(lifespan=lifespan)
app.include_router(user_router)
app.include_router(auth_router)

