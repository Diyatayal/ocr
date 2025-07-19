from fastapi import FastAPI, UploadFile, File
from PIL import Image
import pytesseract
import io

# ❌ REMOVE or COMMENT this line below
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = FastAPI()

@app.post("/ocr")
async def extract_text(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    text = pytesseract.image_to_string(image)
    return {"text": text}
