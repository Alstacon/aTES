import uvicorn
from fastapi import FastAPI
from api.endpoints import users, tokens

app = FastAPI()
app.include_router(users.router)
app.include_router(tokens.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
