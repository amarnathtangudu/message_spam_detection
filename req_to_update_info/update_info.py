import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def classify_update_info(message):
    # Load the model and vectorizer
    with open("models/bill_update_classifier_model.pkl", "rb") as file:
        loaded_data = pickle.load(file)

    loaded_classifier = loaded_data["classifier"]
    loaded_vectorizer = loaded_data["vectorizer"]

    # Example test messages
    # test_messages = [
    #     "Please update your payment details for the gas bill.",
    #     "Looking forward to our meeting next week.",
    #     "Your bank details need to be updated for the billing system.",
    #     "Thanks for shopping with us!",
    #     "Remember to update your phone bill payment information."
    # ]
    test_messages = [message]

    # Vectorize the test messages
    test_vectorized = loaded_vectorizer.transform(test_messages)

    # Predict and get confidence scores
    predictions = loaded_classifier.predict(test_vectorized)
    confidence_scores = loaded_classifier.predict_proba(test_vectorized)

    # Print results with confidence scores
    for message, prediction, confidence in zip(test_messages, predictions, confidence_scores):
        label = "Bill Update Request" if prediction == 1 else "Not a Bill Update Request"
        confidence_score = max(confidence)  # Get the confidence for the predicted class
        print(f"Message: {message}\nPredicted Label: {label}\nConfidence Score: {confidence_score:.2f}\n")
