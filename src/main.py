import uvicorn
from fastapi import FastAPI


app = FastAPI()



@app.get("/")
async def root():
    return {"INFO": "/docs# for Swagger documentation"}


if __name__ == "__main__":
    uvicorn.run("main:app")