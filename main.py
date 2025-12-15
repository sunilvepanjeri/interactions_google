from fastapi import FastAPI
import uvicorn
from app import endpoints
import numpy


app = FastAPI(description="Hello world")

app.include_router(endpoints.router)


if __name__ == "__main__":
    uvicorn.run(app)
