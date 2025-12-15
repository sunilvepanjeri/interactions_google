from fastapi import FastAPI
import uvicorn


app = FastAPI(description="Hello world")


if __name__ == "__main__":
    uvicorn.run(app)
