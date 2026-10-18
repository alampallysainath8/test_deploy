import os
from fastapi import FastAPI

APP_NAME = os.getenv("APP_NAME", "fastapi-devops-lab")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
)


@app.get("/")
def read_root():
    return {"message": f"Welcome to {APP_NAME}!"}


@app.get("/health")
def get_health():
    return {"status": "healthy"}


@app.get("/info")
def get_info():
    return {
        "name": APP_NAME,
        "version": APP_VERSION,
    }
