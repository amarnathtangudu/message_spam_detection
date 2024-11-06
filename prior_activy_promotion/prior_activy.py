import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def classify_prior_activity(message):
    # Load the model and vectorizer
    with open("models/promotional_classifier_model.pkl", "rb") as file:
        loaded_data = pickle.load(file)

    loaded_classifier = loaded_data["classifier"]
    loaded_vectorizer = loaded_data["vectorizer"]

    # Example test messages
    # test_messages = [
    #     "Here’s a 10% discount on your next purchase!",
    #     "Meeting scheduled for next week.",
    #     "We have special offers on products related to your last order!",
    #     "Your request has been processed successfully.",
    #     "Take advantage of this deal on items you viewed recently."
    # ]
    test_messages = [message]

    # Vectorize the test messages
    test_vectorized = loaded_vectorizer.transform(test_messages)

    # Predict and get confidence scores
    predictions = loaded_classifier.predict(test_vectorized)
    confidence_scores = loaded_classifier.predict_proba(test_vectorized)

    # Print results with confidence scores
    for message, prediction, confidence in zip(test_messages, predictions, confidence_scores):
        label = "Promotional Message based on prior activity" if prediction == 1 else "Non-Promotional Message"
        confidence_score = max(confidence)  # Get the confidence for the predicted class
        print(f"Message: {message}\nPredicted Label: {label}\nConfidence Score: {confidence_score:.2f}\n")
