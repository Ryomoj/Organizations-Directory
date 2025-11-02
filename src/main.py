import uvicorn
from fastapi import FastAPI

from src.api.organizations import router as organization_router

app = FastAPI()
app.include_router(organization_router)


@app.get("/")
async def root():
    return {"INFO": "/docs# for Swagger documentation"}


if __name__ == "__main__":
    uvicorn.run("main:app")