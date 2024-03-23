import uvicorn
from fastapi import FastAPI
from api import api_router as v1_api_router
from config import settings

app = FastAPI()
app.include_router(v1_api_router, prefix=settings.api_v1_prefix)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
