import os

from fastapi import FastAPI
from app.config import get_settings, Settings

from tortoise.contrib.fastapi import register_tortoise

from app.api import ping, summaries

from app.db import init_db



app =  FastAPI()


def create_application() -> FastAPI:
    
    application = FastAPI()
    
    application.include_router(ping.router)
    application.include_router(summaries.router, prefix = "/summaries", tags = ["summaries"])
    
    return application


app = create_application()
    
init_db(app)

