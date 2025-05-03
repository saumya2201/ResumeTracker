from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os
from app.config import Config

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "healthy"}

@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    # Validate file type
    if file.content_type not in Config.ALLOWED_FILE_TYPES:
        raise HTTPException(status_code=400, detail="Only PDF and DOCX files are supported.")

    # Create temp folder if it doesn't exist
    os.makedirs(Config.TEMP_DIR, exist_ok=True)

    # Save file to temp directory
    file_path = os.path.join(Config.TEMP_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename, "message": "Resume uploaded successfully."}
