import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import json

def predict_color(uploaded_file, model, color_dict):
    # Load and preprocess the image
    image_size = (256, 256)
    IMG_HEIGHT, IMG_WIDTH = image_size
    img = image.load_img(uploaded_file, target_size=(IMG_HEIGHT, IMG_WIDTH))
    img_array = image.img_to_array(img) / 255.0  # Normalize image
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    
    # Get model predictions
    predictions = model.predict(img_array)
    
    # Get the predicted class
    class_names = list(['Black', 'Blue', 'Brown', 'Cyan', 'Gray', 'Green', 'Purple', 'Red', 'Teal', 'White', 'Yellow'])
    preditced_class_idx = np.argmax(predictions)
    predicted_class = class_names[preditced_class_idx]
    
    # Retrieve color information from the dictionary
    color_info = color_dict.get(predicted_class, None)
    
    if color_info:
        # Construct a dictionary with the color information
        result = {
            "predicted_class": predicted_class,
            "rgb": color_info['RGB'],
            "hue": color_info['Hue (HSL/HSV)'],
            "saturation": color_info['Saturation (HSL)'],
            "lightness": color_info.get('Lightness (HSL)', None),
            "saturation_hsv": color_info.get('Saturation (HSV)', None),
            "value_hsv": color_info.get('Value (HSV)', None),
            "confidence": float(predictions[0][preditced_class_idx])
        }
    else:
        result = {
            "error": "Informasi warna tidak ditemukan untuk kelas yang diprediksi."
        }
    
    return json.dumps(result, indent=4)

