from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

@router.post("/generate")
def generate_code(request: PromptRequest):
    return{
            "message":"Prompt received",
            "Prompt":request.prompt
            }
