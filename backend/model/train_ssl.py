import pandas as pd
import numpy as np
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load SSL training data
train_data = pd.read_csv("../data/ssl_train_data.csv")

# Load test data
test_data = pd.read_csv("../data/test_data.csv")

print("Training samples:", len(train_data))
print("Test samples:", len(test_data))

#separate Features and labels
X_train_text = train_data["text"]
y_train = train_data["label"]

X_test_text = test_data["text"]
y_test = test_data["label"]

#Apply TF-IDF vectorizer
vectorizer = TfidfVectorizer(
    stop_words="english",
    max_df=0.7,
    max_features=5000
)

X_train = vectorizer.fit_transform(X_train_text)
X_test = vectorizer.transform(X_test_text)

#Build semi-supervised learning 
base_model = LogisticRegression(max_iter=1000, class_weight='balanced')

ssl_model = SelfTrainingClassifier(
    base_model,
    threshold=0.8  # confidence threshold
)

ssl_model.fit(X_train, y_train)

#Evaluate model
y_pred = ssl_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("SSL Model Accuracy:", accuracy)
print(classification_report(y_test, y_pred))

#save model and vectorizer
joblib.dump(ssl_model, "ssl_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model and vectorizer saved successfully!")