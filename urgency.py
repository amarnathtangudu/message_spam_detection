# Load the model and vectorizer
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

with open("urgency_classifier_model.pkl", "rb") as file:
    loaded_data = pickle.load(file)

# Extract the classifier and vectorizer
loaded_classifier = loaded_data["classifier"]
loaded_vectorizer = loaded_data["vectorizer"]

# Example prediction using loaded model and vectorizer
test_message = "Final notice: Complete the survey within 24 hours."
test_vectorized = loaded_vectorizer.transform([test_message])
prediction = loaded_classifier.predict(test_vectorized)
predicted_label = "Urgent" if prediction[0] == 1 else "Non-Urgent"

print(f"Test message: {test_message}")
print(f"Predicted label: {predicted_label}")
