# FastAPI
from fastapi import FastAPI

# Routers
from routers.auth import router as auth_router
from routers.user import router as user_router
from routers.tweet import router as tweet_router

# Database
from config.db import meta
from config.db import engine

# Initialize database
meta.create_all(engine)

# Initialize the app
app = FastAPI()

app.include_router(auth_router, prefix='/auth')
app.include_router(user_router, prefix='/users')
app.include_router(tweet_router, prefix='/tweets')