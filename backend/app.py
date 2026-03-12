from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from datetime import datetime
import pandas as pd

app = FastAPI()
#CORS
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Load saved model and vectorizer
model = joblib.load("model/ssl_model.pkl")
log_file = "data/prediction_logs.csv"
vectorizer = joblib.load("model/vectorizer.pkl")


# Request body structure
class NewsInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "News Authenticity API is running"}

@app.post("/predict")
def predict_news(news: NewsInput):

    text_vector = vectorizer.transform([news.text])

    prediction = model.predict(text_vector)[0]
    probabilities = model.predict_proba(text_vector)[0]
    confidence = float(np.max(probabilities))

    label = "Real" if prediction == 1 else "Fake"

    timestamp = datetime.now()

    # Create log entry
    new_entry = pd.DataFrame([{
        "text": news.text,
        "prediction": label,
        "confidence": confidence,
        "timestamp": timestamp
    }])

    # Append to CSV
    new_entry.to_csv(log_file, mode="a", header=False, index=False)

    return {
        "prediction": label,
        "confidence": confidence,
        "timestamp": timestamp
    }