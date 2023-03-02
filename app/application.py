"""Application Entry Point"""
from fastapi import FastAPI
from app.v1.routers import restaurants as restaurants_v1

app = FastAPI()

app.include_router(restaurants_v1.router, prefix="/v1")


@app.get("/")
async def root():
    """Root path"""
    return {"message": "Hallo :)"}


@app.get("/info")
async def info():
    """Info path"""
    return {"version": "1.0.0"}
