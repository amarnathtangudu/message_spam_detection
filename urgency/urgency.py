# Load the model and vectorizer
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from constants import models_folder_path
import os


def get_urgency_classification(message):
    with open(os.path.join(models_folder_path, "urgency_classifier_model.pkl"), "rb") as file:
        loaded_data = pickle.load(file)

    # Extract the classifier and vectorizer
    loaded_classifier = loaded_data["classifier"]
    loaded_vectorizer = loaded_data["vectorizer"]

    # Example prediction using loaded model and vectorizer
    # test_message = "Final notice: Complete the survey within 24 hours."
    test_vectorized = loaded_vectorizer.transform([message])
    prediction = loaded_classifier.predict(test_vectorized)
    confidence_scores = loaded_classifier.predict_proba(test_vectorized)
    predicted_label = "Urgent" if prediction[0] == 1 else "Non-Urgent"
    confidence_score = confidence_scores[0][prediction[0]]

    # print(f"Test message: {message}")
    print(f"Predicted label: {predicted_label}")
    print(f"Confidence score: {confidence_score:.2f}")
    print("-" * 50)
