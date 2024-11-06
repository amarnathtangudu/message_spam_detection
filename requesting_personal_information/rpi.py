import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


def get_rpi_classification(message):
    # Load the model and vectorizer
    with open("models/personal_info_classifier_model.pkl", "rb") as file:
        loaded_data = pickle.load(file)

    loaded_classifier = loaded_data["classifier"]
    loaded_vectorizer = loaded_data["vectorizer"]

    # Example test messages
    # test_messages = [
    #     "Please provide your bank account number.",
    #     "Thank you for your order!",
    #     "Send your credit card information for confirmation.",
    #     "Your package has been shipped.",
    #     "We need your social security number for verification."
    # ]
    test_messages = [message]

    # Vectorize the test messages
    test_vectorized = loaded_vectorizer.transform(test_messages)

    # Predict and get confidence scores
    predictions = loaded_classifier.predict(test_vectorized)
    confidence_scores = loaded_classifier.predict_proba(test_vectorized)

    # Print results with confidence scores
    for message, prediction, confidence in zip(
        test_messages, predictions, confidence_scores
    ):
        label = (
            "Requesting Personal Information"
            if prediction == 1
            else "Not Requesting Personal Information"
        )
        confidence_score = max(confidence)  # Get the confidence for the predicted class
        print(
            f"Message: {message}\nPredicted Label: {label}\nConfidence Score: {confidence_score:.2f}\n"
        )
