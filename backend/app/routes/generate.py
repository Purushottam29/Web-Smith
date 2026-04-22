from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm_service import generate_response
from app.utils.file_handler import save_code_to_file

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

@router.post("/generate")
def generate_code(request: PromptRequest):
    ai_output = generate_response(request.prompt)
    file_path = save_code_to_file(ai_output)
    return{
            "message":"Code generated and saved successfully",
            "file_output": file_path,
            "output": ai_output
            }
