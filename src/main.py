from fastapi import FastAPI
from pydantic import BaseModel
from src.evaluator import evaluate_candidate
import uvicorn

app = FastAPI()

class RecruitmentRequest(BaseModel):
    resume_text: str
    job_description: str

@app.post("/analyze")
async def analyze_resume(data: RecruitmentRequest):
    # This endpoint will be called by n8n or Make.com
    result = evaluate_candidate(data.resume_text, data.job_description)
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)