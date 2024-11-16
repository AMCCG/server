from fastapi import FastAPI

from database import engine
from model.base import Base
from routes import auth

app = FastAPI()

app.include_router(auth.roter, prefix='/auth')

Base.metadata.create_all(engine)
