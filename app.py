from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

from fastapi import UploadFile, File
import shutil
from defense import detect_poisoning

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_location = f"uploads/{file.filename}"
    
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = detect_poisoning(file_location)

    return {
    "filename": file.filename,
    "risk_score": result["risk_score"],
    "status": result["status"]
}