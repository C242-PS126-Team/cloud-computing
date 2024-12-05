import pandas as pd
import requests
from tensorflow.keras.models import load_model
from tempfile import NamedTemporaryFile
import os
from config import *

criteria_color = pd.read_excel(CRITERIA_COLOR_URL)

def loadModel():
    # Download model file
    response = requests.get(MODEL_URL)
    if response.status_code == 200:
        # Store the model in a temporary file
        model_file_path = os.path.join(os.getcwd(), 'model.h5')
        
        # Save the model file to the root directory
        with open(model_file_path, 'wb') as model_file:
            model_file.write(response.content)
        
        # Load the model
        model = load_model(model_file_path)
        return model, criteria_color
    else:
        raise Exception(f"Failed to download model. Status code: {response.status_code}")