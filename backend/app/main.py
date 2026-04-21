from fastapi import FastAPI
from app.routes.generate import router as generate_router

app = FastAPI()

@app.get("/")
def Status():
    return {"message": "Backend Started"}

app.include_router(generate_router)
