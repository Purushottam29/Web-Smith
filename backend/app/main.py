from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def Status():
    return {"message": "Backend Started"}

