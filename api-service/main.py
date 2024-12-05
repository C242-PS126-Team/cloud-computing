from io import BytesIO
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse, JSONResponse

from pydantic import BaseModel
from service.inferenceService import predict_color
from service.loadModel import loadModel
from utils import generate_unique_id

# from google.cloud import storage
from typing import Optional
import requests
import os

app = FastAPI()
model, color_dict = loadModel()

class ImageRequest(BaseModel):
    # Menentukan parameter dengan nilai default
    radioSubmitway: str = "numberoption"  # Default ke 'numberoption'
    numberselector: int = 69  # Default ke 69
    background_colorslider: str = "#ffffff"  # Default ke warna putih
    iterationslider: int = 30000  # Default ke 30000
    min_radius: int = 4  # Default ke 4
    max_radius: int = 15  # Default ke 15
    use_shift: str = "on"  # Default ke 'on'
    shiftslider: int = 30  # Default ke 30
    use_light: str = "on"  # Default ke 'on'
    lightschwiftslider: int = 120  # Default ke 120
    use_blackwhite: str = "on"  # Default ke 'on'
    first_colorslider: str = "#89af23"  # Default ke warna hijau
    second_colorslider: str = "#db5e2e"  # Default ke warna merah
    use_grad: str = "on"  # Default ke 'on'
    gradientshiftslider: int = 25  # Default ke 25
    doCrop: str = "on"  # Default ke 'on'

@app.get("/api/")
async def read_root():
    return {"message": "Welcome to API"}

@app.post("/api/predicted")
async def predicted(file: UploadFile = File(...)):
    id = generate_unique_id()
    image_data = await file.read()
    img = BytesIO(image_data)
    data = predict_color(uploaded_file=image_data, model=model, color_dict=color_dict)

    return JSONResponse(content={
        "status_code": 201,
        "status": "ok",
        "id": id,
        "predictions": data, 
    })
    

@app.post("/api/generate-plate")
async def get_image(data: ImageRequest):
    url = "https://imagetocircle.pythonanywhere.com/"

    payload = data.dict()
    response = requests.post(url, data=payload)
    
    # Mengecek respon dari server
    if response.status_code == 200:
        # Mengembalikan gambar sebagai StreamingResponse
        return StreamingResponse(BytesIO(response.content), media_type="image/jpeg")
    else:
        return {"message": "Failed to submit form", "status_code": response.status_code}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
