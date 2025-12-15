from fastapi import FastAPI
import uvicorn
from app import endpoints
import os

string = 'i am callable in the world'
new_winter = 'cool'

app = FastAPI(description="Hello world")

app.include_router(endpoints.router)


if __name__ == "__main__":
    uvicorn.run(app)
