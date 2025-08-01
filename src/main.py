from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.api.main import api_router
from src.core.db import create_db_and_tables
from fastapi.middleware.cors import CORSMiddleware 

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Porta do React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
