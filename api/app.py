from fastapi import FastAPI, UploadFile, File
from PIL import Image
import tensorflow as tf
import numpy as np
import io

# Create the FastAPI application
app = FastAPI()

# Load the trained model
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model" / "best_model.keras"

model = tf.keras.models.load_model(MODEL_PATH)

# Flower class names
class_names = [
    "daisy",
    "dandelion",
    "rose",
    "sunflower",
    "tulip"
]

# Image size used during training
IMG_SIZE = (224, 224)


# Function to prepare an uploaded image
def preprocess_image(image):
    image = image.resize(IMG_SIZE)
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image


# Home page
@app.get("/")
def home():
    return {
        "message": "Flower Classification API is running successfully!"
    }


# Prediction endpoint
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read())).convert("RGB")

    image = preprocess_image(image)

    prediction = model.predict(image)

    predicted_class = class_names[np.argmax(prediction)]

    confidence = float(np.max(prediction))

    return {
        "prediction": predicted_class,
        "confidence": round(confidence, 4)
    }