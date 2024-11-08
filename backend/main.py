from fastapi import FastAPI, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from download_model import download_model

download_model() 

from model_handler import generate_image_feedback

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class FeedbackRequest(BaseModel):
    image_url: Optional[str] = None
    image_base64: Optional[str] = None
    prompt: Optional[str] = None

@app.post("/api/feedback")
async def feedback_endpoint(
    file: Optional[UploadFile] = None,  
    request_data: Optional[FeedbackRequest] = None  
):

    image_data = None
    user_prompt = request_data.prompt if request_data else ""
    
    if file:

        if not file.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="Uploaded file is not an image.")
        image_data = await file.read()
    else:
        raise HTTPException(status_code=400, detail="No valid image input provided.")

    feedback = generate_image_feedback(image_data, user_prompt)

    return {"feedback": feedback}