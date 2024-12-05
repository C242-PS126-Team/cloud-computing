from io import BytesIO
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse, JSONResponse
import json

from pydantic import BaseModel
from service import predict_color
from service import loadModel
from utils import generate_unique_id

# from google.cloud import storage
from typing import Optional
import requests
import os

app = FastAPI()
model, criteria_color = loadModel()
color_dict = criteria_color.set_index('Color Name').to_dict(orient='index')

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
    try:
        # Validate file
        if not file or file.filename == "":
            raise HTTPException(status_code=400, detail="No file uploaded")
        
        # Check file size (optional, example limit 10MB)
        file.file.seek(0, 2)  # Move to end of file
        file_size = file.file.tell()
        file.file.seek(0)  # Reset file pointer
        
        if file_size > 10 * 1024 * 1024:  # 10MB limit
            raise HTTPException(status_code=413, detail="File too large. Maximum 10MB allowed")
        
        # Validate file type (optional)
        # allowed_types = ['image/jpeg', 'image/png']
        # if file.content_type not in allowed_types:
        #     raise HTTPException(status_code=400, detail="Invalid file type. Only JPEG, PNG, and GIF are allowed")
        
        # Generate unique ID
        id = generate_unique_id()
        
        # Read image data
        image_data = await file.read()
        img = BytesIO(image_data)
        
        # Predict color
        try:
            data = predict_color(uploaded_file=img, model=model, color_dict=color_dict)
        except Exception as predict_error:
            raise HTTPException(status_code=500, detail=f"Prediction error: {str(predict_error)}")
        
        # Parse prediction result
        prediction_result = json.loads(data)
        
        # Check if prediction was successful
        if prediction_result.get('status') == 'error':
            raise HTTPException(status_code=400, detail=prediction_result.get('message', 'Prediction failed'))
        
        return JSONResponse(content={
            "status_code": 201,
            "status": "ok",
            "id": id,
            "predictions": prediction_result, 
        })
    
    except HTTPException as http_error:
        return JSONResponse(
            status_code=http_error.status_code, 
            content={
                "status_code": http_error.status_code,
                "status": "error",
                "message": http_error.detail
            }
        )
    
    except Exception as unexpected_error:
        return JSONResponse(
            status_code=500, 
            content={
                "status_code": 500,
                "status": "error",
                "message": f"Unexpected error: {str(unexpected_error)}"
            }
        )
    

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
    uvicorn.run(app, host="0.0.0.0", port=8080)
