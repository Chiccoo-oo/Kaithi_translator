from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from translate import translate
from converter import hindi_to_kaithi
import uvicorn
import os

app = FastAPI(title="Kaithi Translator API")

# Models for request/response
class TranslationRequest(BaseModel):
    text: str

class TranslationResponse(BaseModel):
    original: str
    translated: str

@app.post("/api/kaithi-to-hindi", response_model=TranslationResponse)
async def k_to_h(request: TranslationRequest):
    try:
        result = translate(request.text)
        return TranslationResponse(original=request.text, translated=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/hindi-to-kaithi", response_model=TranslationResponse)
async def h_to_k(request: TranslationRequest):
    try:
        result = hindi_to_kaithi(request.text)
        return TranslationResponse(original=request.text, translated=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Mount static files
if os.path.exists("static"):
    app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
