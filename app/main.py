from fastapi import FastAPI
# from routes import router as UserRouter
from app.routes import users

app = FastAPI()



app.include_router(users.router, tags=["User"], prefix="/user")

@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI with MongoDB"}