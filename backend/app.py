from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from datetime import datetime

# Load saved model and vectorizer
model = joblib.load("model/ssl_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

app = FastAPI()

# Request body structure
class NewsInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "News Authenticity API is running"}

@app.post("/predict")
def predict_news(news: NewsInput):
    # Transform input text
    text_vector = vectorizer.transform([news.text])
    
    # Predict
    prediction = model.predict(text_vector)[0]
    probabilities = model.predict_proba(text_vector)[0]
    confidence = np.max(probabilities)

    label = "Real" if prediction == 1 else "Fake"

    return {
        "prediction": label,
        "confidence": float(confidence),
        "timestamp": datetime.now()
    }